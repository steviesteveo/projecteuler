# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

number1 = 100
bestyet = 0

def testPalindrome(candidate):
	
	ispalindrome = False
	
	# Reverse string, check for equivalence
	
	candidatestring = str(candidate)
	
	if candidatestring == candidatestring[::-1]:
		return True
		
# cycle all three digit numbers and test against a nested of all three digit numbers


for i in range(99, 1001, 1):
	for x in range(99, 1001, 1):		
		candidate = i * x
		if testPalindrome(candidate) == True:
			if bestyet < candidate:
				bestyet = candidate
				best_i = i
				best_x = x
				
print "i = %d, x = %d. %d" % (best_i, best_x, bestyet)