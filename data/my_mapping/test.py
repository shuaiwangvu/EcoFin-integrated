#alignment.nt
import os

skos_exactMatch = "http://www.w3.org/2004/02/skos/core#exactMatch"


pairs = set()
directory = os.fsencode('./')
output_file = open('alignment.nt', 'w')

# skos_exactMatch

entities = set ()
for file in os.listdir(directory):
	pairs_this_file = []
	filename = os.fsdecode(file)
	if 'txt' in filename:
		print ('file = ', filename)
		f = open(filename, 'r')
		lines = f.readlines()


		for l in lines:
			sp = l.split('|')
			s = sp[0]
			t = sp[1]
			entities.add(s)
			entities.add(t)

print ('total entities = ', len (entities))
