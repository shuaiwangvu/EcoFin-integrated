# This is a Python script for the analysis of Strongly Connected Components (SCC)
# and Weakly Connected Components (WCC) regarding the following relations:

# skos:broader
# skos:broadMatch
# skos:narrower
# skos:narrowMatch

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

files = ['fibo-vD', 'fibo-owl', 'fro', 'hfr', 'lkif', 'bro', 'figi', 'stw', 'jel', 'fund', 'stw-mapping', 'my_mapping']


for file in files:
	path_to_file = './data/integrated_files/'+file+'.hdt'
	hdt_kg = HDTDocument(path_to_file)
	triples, cardinality = hdt_kg.search_triples("", "", "")
	entities = set()
	g = nx.DiGraph()
	for s, p, o in triples:
		if str(s)[0] != '"'  and not (str(s)[0] == '_' and str(s)[1] == ':'):
			entities.add(s)
		# else:
			# print ('Subject - not an entity but a string/number',s)

		if str(o)[0] != '"'  and not (str(o)[0] == '_' and str(o)[1] == ':'):
			entities.add(o)
		# else:
			# print ('Object - not an entity but a string/number',o)
			g.add_edge(s, o)
	print ('\n\nKG ', file, 'has ', cardinality, 'triples')
	print ('\t with ', len (entities), ' entities')
	print ('the graph has', g.number_of_nodes(),'entities')
	largest_cc = max(nx.strongly_connected_components(g), key=len)
	print ('the biggest scc has ', len(largest_cc), 'nodes')
	print ('\t{:06.2f}'.format(len(largest_cc)/ g.number_of_nodes()*100))

	largest_cc = max(nx.weakly_connected_components(g), key=len)
	print ('the biggest wcc has ', len(largest_cc), 'nodes')
	print ('\t{:06.2f}'.format(len(largest_cc)/ g.number_of_nodes()*100))

print ('\n\n----------INTEGRATED----------\n')

path_to_file = './data/integrated_files/integrated.hdt'
hdt_kg = HDTDocument(path_to_file)
triples, cardinality = hdt_kg.search_triples("", "", "")
entities = set()
g = nx.DiGraph()
for s, p, o in triples:
	if str(s)[0] != '"'  and not (str(s)[0] == '_' and str(s)[1] == ':'):
		entities.add(s)
	# else:
		# print ('Subject - not an entity but a string/number',s)

	if str(o)[0] != '"'  and not (str(o)[0] == '_' and str(o)[1] == ':'):
		entities.add(o)
	# else:
		# print ('Object - not an entity but a string/number',o)
		g.add_edge(s, o)
print ('the integrated KG has ', cardinality, 'triples')
print ('\t with ', len (entities), ' entities')

largest_cc = max(nx.strongly_connected_components(g), key=len)
print ('the biggest scc has ', len(largest_cc), 'nodes')
print ('\t{:06.2f}'.format(len(largest_cc)/ g.number_of_nodes()*100))

largest_cc = max(nx.weakly_connected_components(g), key=len)
print ('the biggest wcc has ', len(largest_cc), 'nodes')
print ('\t{:06.2f}'.format(len(largest_cc)/ g.number_of_nodes()*100))
