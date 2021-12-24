from hdt import HDTDocument, IdentifierPosition




files = [fibo-skos, fibo-owl,fro, hfr, lkif, bro, figi, stw, stw-mappings]


for file in files:
	path_to_file = './'+file+'.hdt'
	hdt_kg = HDTDocument(path_to_file)
	triples, cardinality = hdt_metalink.search_triples("", rdf_subject, subject)
