from owlready2 import *



# onto_path.append("./")
onto = get_ontology('fro.rdf')
onto.load()
onto.save()
