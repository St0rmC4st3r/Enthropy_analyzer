# Calculates frequency and entropy of the aphabet in the provided text.
# Created by St0rmC4st3r

import sys
import os
from math import log2
file = open(sys.argv[1], "r", encoding='utf-8')
fname = file.name
alphabet = {}
probdict = {}
flen = 0
enthropy = 0
fsize = os.path.getsize(sys.argv[1])

# Just a good thing to have, since excel has troubles when parsing string pairs

excel_parseability = False
if len(sys.argv) > 2:
	if sys.argv[2] == "excel":
		excel_parseability = True


for line in file:
	if not line:
		break  # By all means this should never happen, since an empty line should only return at EOF.
	for char in line:
		flen += 1
		if char in alphabet:
			alphabet[char] = alphabet[char]+1
		else:
			alphabet[char] = 1
for i, j in alphabet.items():
	prob = j/flen
	probdict[i] = prob
	enthropy += prob * log2(prob)
enthropy *= -1

# Too lazy to write functions
destfile = open(sys.argv[1]+"_analysis_result.txt", "w")
if excel_parseability:  # kinda not for readability at all.
	destfile.write("Alphabet and numbers. \n")
	for i, j in alphabet.items():
		destfile.write(("\\n" if i == "\n" else i) + "\n")
	for i, j in alphabet.items():
		destfile.write(str(j) + "\n")

	destfile.write("Alphabet and probabilities. \n")
	for i, j in probdict.items():
		destfile.write(("\\n" if i == "\n" else i) + "\n")
	for i, j in probdict.items():
		destfile.write(str(round(j, 9)) + "\n")
	destfile.write("Entropy. \n")
	destfile.write(str(enthropy) + "\n")
	destfile.write("Information amount. \n")
	destfile.write(str(enthropy * flen) + "\n")
	destfile.write("Information amount in bytes. \n")
	destfile.write(str(enthropy * flen/8) + "\n")
	destfile.write("File size. \n")
	destfile.write(str(fsize) + "\n")
else:
	destfile.write("Alphabet and numbers. \n")
	for i, j in alphabet.items():
		destfile.write("\""+("\\n" if i == "\n" else i)+"\"" + " " + str(j) + "\n")

	destfile.write("Alphabet and probabilities. \n")
	for i, j in probdict.items():
		destfile.write("\""+("\\n" if i == "\n" else i)+"\"" + " " + str(round(j, 9)) + "\n")
	destfile.write("Entropy. \n")
	destfile.write(str(enthropy) + "\n")
	destfile.write("Information amount. \n")
	destfile.write(str(enthropy * flen) + "\n")
	destfile.write("Information amount in bytes. \n")
	destfile.write(str(enthropy * flen / 8) + "\n")
	destfile.write("File size. \n")
	destfile.write(str(fsize) + "\n")


print(alphabet)
print(probdict)
print(enthropy)


