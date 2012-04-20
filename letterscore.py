# A library to convert letters into numbers

# Currently implemented:
	# 1) capitalletterscore(char) : function that takes upper case A-Z characters and assigns A=1...Z=26 to them
	
# Proposed:
	# 2) lowercaseletterscore(char) : function that takes lower case a-z characters and assigns a=1...z=26 to them
	# 3) allletterscore(char) : function that takes upper and lower case A-Z and a-z characters and assigns a=1,A=1...z=26,Z=26 to them
	# 4) scrabblescore(char) : function that takes upper case A-Z and assigns Scrabble tile scoring to them.

def capitalletterscore(char):
	letterscore = 0
	
	if char == "A":
		letterscore = 1
	elif char == "B":
		letterscore = 2
	elif char == "C":
		letterscore = 3
	elif char == "D":
		letterscore = 4
	elif char == "E":
		letterscore = 5
	elif char == "F":
		letterscore = 6
	elif char == "G":
		letterscore = 7
	elif char == "H":
		letterscore = 8
	elif char == "I":
		letterscore = 9
	elif char == "J":
		letterscore = 10
	elif char == "K":
		letterscore = 11
	elif char == "L":
		letterscore = 12
	elif char == "M":
		letterscore = 13
	elif char == "N":
		letterscore = 14
	elif char == "O":
		letterscore = 15
	elif char == "P":
		letterscore = 16
	elif char == "Q":
		letterscore = 17
	elif char == "R":
		letterscore = 18
	elif char == "S":
		letterscore = 19
	elif char == "T":
		letterscore = 20
	elif char == "U":
		letterscore = 21
	elif char == "V":
		letterscore = 22
	elif char == "W":
		letterscore = 23
	elif char == "X":
		letterscore = 24
	elif char == "Y":
		letterscore = 25
	elif char == "Z":
		letterscore = 26
	else:
		break
	
	return letterscore