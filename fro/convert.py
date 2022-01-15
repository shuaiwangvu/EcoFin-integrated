from rdflib import Graph

# names = ['fibo-skos', 'fibo-owl', 'fro', 'hfr', 'lkif', 'bro', 'figi', 'stw', 'stw-mappings', 'jel', 'fund']
names = ['AnnotationProperty.ttl',
'CFR-2012-title17-vol3-part275.ttl',
'CFR-2013-title12-vol4-part252.ttl',
'CFR-2015-title12-vol2-part217.ttl',
'CFR-2015-title12-vol3-part225.ttl',
'CFR_FDSys_Schema.ttl',
'Code_Federal_Regulations.ttl',
'FIBO_EthOn_Alignment.ttl',
'FIBO_LKIF_Alignment.ttl',
'FIBO_import.ttl',
'FRO_Banking.ttl',
'FRO_CFR_Banking.ttl',
'FRO_CFR_Title_12_Part_217.ttl',
'FRO_CFR_Title_12_Part_225.ttl',
'FRO_CFR_Title_12_Part_252.ttl',
'FRO_CFR_Title_17_Part_275.ttl',
'FRO_USC_Banking.ttl',
'FRO_USC_Title_12_Chapter_17.ttl',
'FinancialReference.ttl',
'Investment_Adviser_Act_USC_CFR.ttl',
'Judging_Contracts_Core.ttl',
'LLC_import.ttl',
'LegalReference.ttl',
'Reference.ttl',
'USC-2015-title12-chapter17.ttl',
'USC-2015-title12-chapter53 (1).ttl',
'USC-2015-title12-chapter53.ttl',
'USC-2015-title15-chapter2D (1).ttl',
'USC-2015-title15-chapter2D.ttl',
'USC_USLM_Schema.ttl',
'US_LegalReference.ttl',
'United_States_Code.ttl']




g = Graph()
for name in names:
	print ('working on ', name)
	g.parse(name, format="ttl")

g.serialize(destination='./fro.rdf', format="xml")
# g.serialize(destination='./fro.ttl', format="ttl")
# g.serialize(destination='./fro.nt', format="nt")
