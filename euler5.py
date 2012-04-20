# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def checkifvalidtriplet(a, b, c):
	if a < b:
		if b < c:
			if (a**2) + (b**2) == (c**2):
				return True 
			else:
				return False
		else:
			return False
	else:
		return False
			
def equalstarget(target, a, b, c):			
	if a + b + c == target:
		getproduct(a, b, c)

def getproduct(a, b, c):
	answer = a*b*c
	print "%d + %d + %d = 1000" % (a, b, c)
	print "The answer is: %d" % answer	
		
# Use for all values for a, b and c	

for a in range(0, 500, 1):
	for b in range(0, 500, 1):
		for c in range(0, 500, 1):
			if checkifvalidtriplet(a, b, c) == True:
				equalstarget(1000, a, b, c)