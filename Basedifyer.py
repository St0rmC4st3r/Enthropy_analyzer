# Made by St0rmC4st3r
# kinda based
# based on what?
# 64, duh

# After some debugging, I have committed a sloth sin. Instead of using binaries like a decent person....
# I am using literals.

import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
file = open(sys.argv[1], "rb")
raw = file.read()
the_end_is_nigh = False
literal_sin = ""
sin_count = 0
basedoutput = ""
quartet = ""

for i in raw:
	thebin = bin(i)[2:]
	literal_sin += "0"* (8-len(thebin)) + thebin # Don't ask. Edit: I'd better explain it. It makes all bytes 8 bits total, since senior 0's are ommited.

for i in range(0, len(literal_sin)):
	quartet += literal_sin[i]
	if len(quartet) == 24:
		for j in range(0, 3):
			basedoutput += alphabet[int(quartet[j*6:j*6+6], 2)]
			sin_count += 1
		quartet = ""
if len(quartet) == 8:
	while len(quartet) != 12:
		quartet += "0"
	basedoutput += alphabet[int(quartet[0:5], 2)]
	basedoutput += alphabet[int(quartet[6:11], 2)]
	basedoutput += "=="
if len(quartet) == 16:
	while len(quartet) != 18:
		quartet += "0"
	basedoutput += alphabet[int(quartet[0:5], 2)]
	basedoutput += alphabet[int(quartet[6:11], 2)]
	basedoutput += alphabet[int(quartet[12:17], 2)]
	basedoutput += "="

print("Sins commited:", sin_count)
newfile = open("based64_" + sys.argv[1], "w+", encoding='utf-8')
newfile.write(basedoutput)
file.close()
newfile.close()
