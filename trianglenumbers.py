# Functions related to triangle numbers

def checkfortrianglenumber(score):
	
	# tn = (0.5*n)*(n-1)

	for n in range(1, score, 1):

		if (0.5*n) * (n-1) == score:
			return True