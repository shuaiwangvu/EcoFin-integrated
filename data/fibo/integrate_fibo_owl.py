import os
rootdir = './fibo/'

from rdflib import Graph

# count = 0
# g = Graph()
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if '.ttl' in file:
			print (subdir+ '/' +file)
# 			count += 1
# 			file_name = str(os.path.join(subdir, file))
# 			print ('file at ', file_name)
# 			g.parse(file_name, format="ttl")
#
# # g.serialize(destination='./fibo-owl.ttl', format="ttl")
# g.serialize(destination='./fibo-owl.nt', format="nt")
#
# print ('a total of ', count, ' files were integrated')


# h = Graph()
# h.parse('fibo-vD.ttl', format="ttl")
# h.serialize(destination='fibo-vD.nt', format='nt')
