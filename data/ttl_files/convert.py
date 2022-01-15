from rdflib import Graph

names = ['fibo-vD', 'fibo-owl', 'fro', 'hfr', 'lkif', 'bro', 'figi', 'stw', 'stw-mappings', 'jel', 'fund']





g = Graph()
for name in names:
	print ('working on ', name)
	g.parse(name+'.ttl', format="ttl")
	g.serialize(destination= name+'.rdf', format="xml")
# g.serialize(destination='./fro.ttl', format="ttl")
# g.serialize(destination='./fro.nt', format="nt")
