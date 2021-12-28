from hdt import HDTDocument, IdentifierPosition
import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt


owl_sameas = "http://www.w3.org/2002/07/owl#sameAs"
skos_exactMatch = "http://www.w3.org/2004/02/skos/core#exactMatch"
skos_broadMatch = "http://www.w3.org/2004/02/skos/core#broadMatch"
skos_broader = "http://www.w3.org/2004/02/skos/core#broader"
skos_narrowMatch = "http://www.w3.org/2004/02/skos/core#narrowMatch"
skos_narrower = "http://www.w3.org/2004/02/skos/core#narrower"
skos_relatedMatch = "http://www.w3.org/2004/02/skos/core#relatedMatch"
skos_closeMatch = "http://www.w3.org/2004/02/skos/core#closeMatch"
subPropertyOf = 'http://www.w3.org/2000/01/rdf-schema#subPropertyOf'
inv = 'http://www.w3.org/2002/07/owl#inverseOf'

files = ['fibo-skos', 'fibo-owl', 'fro', 'hfr', 'lkif', 'bro', 'figi', 'stw', 'stw-mappings', 'jel', 'fund']
# files = []

for file in files:
	path_to_file = './data/'+file+'.hdt'
	hdt_kg = HDTDocument(path_to_file)
	triples, cardinality = hdt_kg.search_triples("", "", "")
	entities = set()
	for s, p, o in triples:
		entities.add(s)
		entities.add(o)
	print ('\n\nKG ', file, 'has ', cardinality, 'triples')
	print ('\t with ', len (entities), ' entities')

	# # owl:sameAs
	# triples, cardinality = hdt_kg.search_triples("", owl_sameas, "")
	# print ('owl:sameAs ', cardinality)
	#
	# # skos:exactMatch
	# triples, cardinality = hdt_kg.search_triples("", skos_exactMatch, "")
	# print ('skos:exactMatch ', cardinality)
	#
	#
	# # skos:broadMatch
	# triples, cardinality = hdt_kg.search_triples("", skos_broadMatch, "")
	# print ('skos:broadMatch ', cardinality)
	#
	# # skos:broader
	# triples, cardinality = hdt_kg.search_triples("", skos_broader, "")
	# print ('skos:broader ', cardinality)
	#
	# # skos:narrowMatch
	# triples, cardinality = hdt_kg.search_triples("", skos_narrowMatch, "")
	# print ('skos:narrowMatch ', cardinality)
	#
	# # skos:narrower
	# triples, cardinality = hdt_kg.search_triples("", skos_narrower, "")
	# print ('skos:narrower ', cardinality)
	#
	# # skos:closeMatch
	# triples, cardinality = hdt_kg.search_triples("", skos_closeMatch, "")
	# print ('skos:closeMatch ', cardinality)
	#
	# # skos:relatedMatch
	# triples, cardinality = hdt_kg.search_triples("", skos_relatedMatch, "")
	# print ('skos:relatedMatch ', cardinality)


t = "http://www.w3.org/2002/07/owl#TransitiveProperty"
type = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'

print ('\n\n----------INTEGRATED----------\n')

path_to_file = './data/integrated.hdt'
hdt_kg = HDTDocument(path_to_file)
triples, cardinality = hdt_kg.search_triples("", "", "")
entities = set()
for s, p, o in triples:
	entities.add(s)
	entities.add(o)
print ('the integrated KG has ', cardinality, 'triples')
print ('\t with ', len (entities), ' entities')

set_transitive_relations = set()
# triples, cardinality = hdt_kg.search_triples("", type, t)
# for t_relation, _, _ in triples:
# 	set_transitive_relations.add(t_relation)
trans_collect = set()
# inv_collect = set()

triples, direct_trans_relations = hdt_kg.search_triples("", type, t)
print ('There are ', direct_trans_relations, 'as typed by owl:transitive properties')
for (s,p ,o) in triples:
	trans_collect.add(str(s))
	print ('\t', s)
#

count_trans_rel_triples = 0
for trans_rel in trans_collect:
	triples, cardinality = hdt_kg.search_triples("", trans_rel, "")
	count_trans_rel_triples += cardinality


record = 0
closure_coll = trans_collect.copy()
while len(closure_coll) != record : # untill the size does not expand anymore.
	record = len(closure_coll)
	newly_found = set()
	for t in closure_coll:
		triples, cardinality = hdt_kg.search_triples("", subPropertyOf, t)
		for (s,p,o) in triples:
			# print('new:',s,p,o)
			newly_found.add(str(s))

		triples1, cardinality1 = hdt_kg.search_triples("" ,inv, t)
		for (s,p,o) in triples1:
			# print('new:',s,p,o)
			newly_found.add(str(s))
	closure_coll = closure_coll.union (newly_found)

print ('After computing the closure, there are in total', len (closure_coll), ' relations in the set')


# print ('there are ', len (closure_coll), ' transitive_relations')
for tr in closure_coll:
	print ('transitive relation: ', tr)
	t_triples, t_cardinality = hdt_kg.search_triples("", tr, "")
	print ('\t has ', t_cardinality, ' triples')

	g_skos = nx.DiGraph()
	for (s, p, o) in t_triples:
		g_skos.add_edge(s, o)

	ccs = nx.strongly_connected_components(g_skos)
	len_summary = [len (cc) for cc in ccs]
	ct = Counter(len_summary)
	print ('\tstrongly connected components: ',ct)
