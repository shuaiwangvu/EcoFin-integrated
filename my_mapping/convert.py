import os

skos_exactMatch = "http://www.w3.org/2004/02/skos/core#exactMatch"


pairs = set()
directory = os.fsencode('./')
output_file = open('alignment.nt', 'w')

# skos_exactMatch

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
			pairs_this_file.append((s,t))
			if (s, t) not in pairs and (t, s) not in pairs:
				pairs.add((s,t))
				output_file.write('<'+s+'> <'+ skos_exactMatch +'> <'+ t +'> .\n')
			# print ('s = ', s)
			# print ('t = ', t)
		print ('\t has ', len (pairs_this_file), ' pairs')

print ('overall num of pairs = ', len(pairs))
