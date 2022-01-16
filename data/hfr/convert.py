from rdflib import Graph

# names = ['fibo-skos', 'fibo-owl', 'fro', 'hfr', 'lkif', 'bro', 'figi', 'stw', 'stw-mappings', 'jel', 'fund']
names = ['Hedge_Fund_Financial_Reference.ttl',
'Hedge_Fund_Legal_Reference.ttl',
'Hedge_Fund_Reasoning.ttl',
'PFFormFiling.ttl',
'PFRD_Example_PF.ttl',
'PFRD_Example_PF_Amended.ttl',
'PFRD_Example_PF_Final.ttl',
'PFRD_Example_PF_Initial.ttl',
'PFRD_Example_PF_Transition.ttl',
'PFRD_Example_PF_Updating.ttl',
'PrivateFundSampleData.ttl',
'Rules_Investment_Adviser_Act_Private_Fund.ttl']

g = Graph()
for name in names:
	print ('working on ', name)
	g.parse(name, format="ttl")

# g.serialize(destination='./hfr.ttl', format="ttl")
g.serialize(destination='./hfr.nt', format="nt")
