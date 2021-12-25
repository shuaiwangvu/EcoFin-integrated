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

files = ['fibo-skos', 'fibo-owl', 'fro', 'hfr', 'lkif', 'bro', 'figi', 'stw', 'stw-mappings', 'jel']
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

	# owl:sameAs
	triples, cardinality = hdt_kg.search_triples("", owl_sameas, "")
	print ('owl:sameAs ', cardinality)

	# skos:exactMatch
	triples, cardinality = hdt_kg.search_triples("", skos_exactMatch, "")
	print ('skos:exactMatch ', cardinality)


	# skos:broadMatch
	triples, cardinality = hdt_kg.search_triples("", skos_broadMatch, "")
	print ('skos:broadMatch ', cardinality)

	# skos:broader
	triples, cardinality = hdt_kg.search_triples("", skos_broader, "")
	print ('skos:broader ', cardinality)

	# skos:narrowMatch
	triples, cardinality = hdt_kg.search_triples("", skos_narrowMatch, "")
	print ('skos:narrowMatch ', cardinality)

	# skos:narrower
	triples, cardinality = hdt_kg.search_triples("", skos_narrower, "")
	print ('skos:narrower ', cardinality)

	# skos:closeMatch
	triples, cardinality = hdt_kg.search_triples("", skos_closeMatch, "")
	print ('skos:closeMatch ', cardinality)

	# skos:relatedMatch
	triples, cardinality = hdt_kg.search_triples("", skos_relatedMatch, "")
	print ('skos:relatedMatch ', cardinality)





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
# owl:sameAs
triples, cardinality = hdt_kg.search_triples("", owl_sameas, "")
print ('owl:sameAs ', cardinality)

# skos:relatedMatch
triples, cardinality = hdt_kg.search_triples("", skos_relatedMatch, "")
print ('skos:relatedMatch ', cardinality)

# skos:closeMatch
triples, cardinality = hdt_kg.search_triples("", skos_closeMatch, "")
print ('skos:closeMatch ', cardinality)


# skos:exactMatch
triples, cardinality = hdt_kg.search_triples("", skos_exactMatch, "")
print ('skos:exactMatch ', cardinality)


g_skos = nx.Graph()
for (s, p, o) in triples:
	g_skos.add_edge(s, o)

ccs = nx.connected_components(g_skos)

for cc in ccs:
	if len (cc) >= 13:
		print('size = ',len (cc))
		for c in cc:
			print ('\t', c)
			triples, cardinality = hdt_kg.search_triples(c, "http://www.w3.org/2004/02/skos/core#prefLabel", "")
			for (_, p, o) in triples:
				print ('\t\t',p,o)
ccs = nx.connected_components(g_skos)
len_summary = [len (cc) for cc in ccs]
ct = Counter(len_summary)
print ('connected components: ',ct)


# plot it out
x = ct.keys()
y = ct.values()

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(1.1)
ax = plt.subplot(111)
ax.bar(x, y, color ='grey', align='center')
ax.autoscale(tight=True)
# ax.legend()
plt.yscale('log')
plt.xlabel("size of connected components")
plt.ylabel("frequency")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.legend()
plt.savefig('connected_components_frequency.png', bbox_inches='tight', dpi = 300)
# plt.show()

# integrated BROADER
g_broader_integrated = nx.DiGraph()

# skos:broadMatch
triples, cardinality = hdt_kg.search_triples("", skos_broadMatch, "")
print ('skos:broadMatch ', cardinality)
g_broader = nx.DiGraph()
for (s, p, o) in triples:
	g_broader.add_edge(s, o)
	g_broader_integrated.add_edge(s, o)
sccs = nx.strongly_connected_components(g_broader)
len_summary = [len (scc) for scc in sccs]
ct = Counter(len_summary)
print ('strongly connected components: ',ct)

ccs = nx.strongly_connected_components(g_broader)
for cc in ccs:
	if len (cc) >= 3:
		print('size = ',len (cc))
		for c in cc:
			print ('\t', c)
			triples, cardinality = hdt_kg.search_triples(c, "http://www.w3.org/2004/02/skos/core#prefLabel", "")
			for (_, p, o) in triples:
				print ('\t\t',p,o)

# skos:broader
triples, cardinality = hdt_kg.search_triples("", skos_broader, "")
print ('skos:broader ', cardinality)

g_broader = nx.DiGraph()
for (s, p, o) in triples:
	g_broader.add_edge(s, o)
	g_broader_integrated.add_edge(s, o)
sccs = nx.strongly_connected_components(g_broader)
len_summary = [len (scc) for scc in sccs]
ct = Counter(len_summary)
print ('strongly connected components: ',ct)

# skos:narrowMatch
triples, cardinality = hdt_kg.search_triples("", skos_narrowMatch, "")
print ('skos:narrowMatch ', cardinality)
g_broader = nx.DiGraph()
for (s, p, o) in triples:
	g_broader.add_edge(s, o)
	g_broader_integrated.add_edge(o, s)
sccs = nx.strongly_connected_components(g_broader)
len_summary = [len (scc) for scc in sccs]
ct = Counter(len_summary)
print ('strongly connected components: ',ct)

ccs = nx.strongly_connected_components(g_broader)
for cc in ccs:
	if len (cc) >= 3:
		print('size = ',len (cc))
		for c in cc:
			print ('\t', c)
			triples, cardinality = hdt_kg.search_triples(c, "http://www.w3.org/2004/02/skos/core#prefLabel", "")
			for (_, p, o) in triples:
				print ('\t\t',p,o)

# skos:narrower
triples, cardinality = hdt_kg.search_triples("", skos_narrower, "")
print ('skos:narrower ', cardinality)
g_broader = nx.DiGraph()
for (s, p, o) in triples:
	g_broader.add_edge(s, o)
	g_broader_integrated.add_edge(o, s)
sccs = nx.strongly_connected_components(g_broader)
len_summary = [len (scc) for scc in sccs]
ct = Counter(len_summary)
print ('strongly connected components: ',ct)

print ('\n-------INTEGRATED BROADER------\n')
sccs = nx.strongly_connected_components(g_broader_integrated)
len_summary = [len (scc) for scc in sccs]
ct = Counter(len_summary)
print ('[integrated broader] strongly connected components: ',ct)
ccs = nx.strongly_connected_components(g_broader_integrated)
for cc in ccs:
	if len (cc) >= 3:
		print('size = ',len (cc))
		for c in cc:
			print ('\t', c)
			triples, cardinality = hdt_kg.search_triples(c, "http://www.w3.org/2004/02/skos/core#prefLabel", "")
			for (_, p, o) in triples:
				print ('\t\t',p,o)
