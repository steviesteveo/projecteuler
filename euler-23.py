# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.



def find_abundant_number(x):
	
	sum_of_divisors = 0
	
	for i in range(1, x+1, 1):
		if x % i == 0:
			sum_of_divisors += i
	
	if sum_of_divisors > x:
		return True # Is an abundant number
		
def 
		
# Upper limit on problem: 28123
# Lower limit on problem: 24

for x in range(23, 28124, 1):
	
# Nest a loop of all abundant numbers inside another? Add 

# Work out the sum of 1 -> 28123, work out the sum of the numbers that can be	