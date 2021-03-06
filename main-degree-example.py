# This is a simple script that gives a few examples where the
# in-degree and out-degree has increased after integration

from hdt import HDTDocument, IdentifierPosition
import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
from collections import Counter
import networkx.algorithms.distance_measures as dm
import random

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


collect_big_in = {}
collect_big_out = {}

fig, axs = plt.subplots(2)
# axs[0].set_title('in-degree')
# axs[1].set_title('out-degree')
fig.set_figwidth(6)
fig.set_figheight(10)

files = ['fibo-vD', 'fibo-owl', 'fro', 'hfr', 'lkif', 'bro', 'figi', 'stw', 'stw-mappings', 'jel', 'fund']
kg_name = {'fibo-vD':'FIBO-vD', 'fibo-owl':'FIBO-OWL', 'fro':'FRO', 'hfr':'HFR', 'lkif':'LKIF', 'bro':'BRO', 'figi':'FIGI', 'stw':'STW', 'stw-mappings':'STW(mappings)', 'jel':'JEL', 'fund':'Fund'}
# files = []
in_degree_map = {}
out_degree_map = {}

markers = ["." , "," , "o" , "v" , "^" , "<", ">"]
colors = ['r','g','b','c','m', 'y', 'k']

node_file_indegree = Counter()
node_file_outdegree = Counter()
node_integrated_indegree = Counter()
node_integrated_outdegree = Counter()

for file in files:
	path_to_file = './data/'+file+'.hdt'
	hdt_kg = HDTDocument(path_to_file)
	triples, cardinality = hdt_kg.search_triples("", "", "")
	entities = set()
	g = nx.DiGraph()
	ct_in = Counter()
	ct_out = Counter()
	for s, p, o in triples:
		if str(s)[0] != '"'  and not (str(s)[0] == '_' and str(s)[1] == ':'):
			entities.add(s)
		# else:
			# print ('Subject - not an entity but a string/number',s)

		if str(o)[0] != '"'  and not (str(o)[0] == '_' and str(o)[1] == ':'):
			entities.add(o)
		# else:
			# print ('Object - not an entity but a string/number',o)
		if str(s)[0] != '"' and str(o)[0] != '"':
			g.add_edge(s, o)

	print ('\n\nKG ', file, 'has ', cardinality, 'triples')
	print ('\t with ', len (entities), ' entities')
	try:
		print ('\t diameter = ', dm.diameter(g))
	except Exception as e:
		print ('\t diameter = infinite')

	for n in g.nodes():
		d = g.in_degree(n)
		node_file_indegree[(n, file)] = d
		ct_in[d] += 1
		if d > 1000:
			collect_big_in[n] = d
		d = g.out_degree(n)
		node_file_outdegree[(n, file)] = d
		ct_out[d] += 1
		if d > 1000:
			collect_big_out[n] = d
	print ('in: ',ct_in)
	print ('out:', ct_out)
	color = random.choice(colors)
	shape = random.choice(markers)
	# in
	x = ct_in.keys()
	y = ct_in.values()
	axs[0].scatter(x, y, alpha = 0.4, label=kg_name[file], marker=shape, color=color)
	print ('max in = ', max(x))
	# out
	x = ct_out.keys()
	y = ct_out.values()
	axs[1].scatter(x, y, alpha = 0.4, label=kg_name[file], marker=shape, color=color)
	print ('max out = ', max(x))



print ('\n\n----------INTEGRATED----------\n')

path_to_file = './data/integrated.hdt'
hdt_kg = HDTDocument(path_to_file)
triples, cardinality = hdt_kg.search_triples("", "", "")
entities = set()



g = nx.DiGraph()
ct_in = Counter()
ct_out = Counter()
for s, p, o in triples:
	if str(s)[0] != '"'  and not (str(s)[0] == '_' and str(s)[1] == ':'):
		entities.add(s)
	# else:
		# print ('Subject - not an entity but a string/number',s)

	if str(o)[0] != '"'  and not (str(s)[0] == '_' and str(s)[1] == ':'):
		entities.add(o)
	# else:
		# print ('Object - not an entity but a string/number',o)
	if str(s)[0] != '"' and str(o)[0] != '"':
		g.add_edge(s, o)

print ('\n\nKG ', file, 'has ', cardinality, 'triples')
print ('\t with ', len (entities), ' entities')
try:
	print ('\t diameter = ', dm.diameter(g))
except Exception as e:
	print ('\t diameter = infinite')

for n in g.nodes():
	d = g.in_degree(n)
	node_integrated_indegree[n] = d
	ct_in[d] += 1
	if d > 1000:
		collect_big_in[n] = d
	d = g.out_degree(n)
	node_integrated_outdegree[n] = d
	ct_out[d] += 1
	if d > 1000:
		collect_big_out[n] = d



for n in g.nodes():
	i_in = node_integrated_indegree[n]
	i_out = node_integrated_outdegree[n]
	#
	# acc = []
	# if i_in > 3 :
	# 	for file in files:
	# 		d = node_file_indegree[(n, file)]
	# 		acc.append(d)
	# 	ct0 = acc.count(0)
	# 	if ct0 > 5 and ct0 < 9:
	# 		print ('node ', n)
	# 		print ('in degree ', i_in)
	# 		print('[in]the count list is ', acc)
	# 	# print (acc)

	acc = []
	if i_out > 3 :
		for file in files:
			d = node_file_outdegree[(n, file)]
			acc.append(d)
		ct0 = acc.count(0)
		if ct0 > 5 and ct0 < 9:
			print ('node ', n)
			print ('out degree ', i_out)
			print('[out]the count list is ', acc)
			print('neighbors: ', list(g.neighbors(n)))
			# print (acc)
