# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Answer : 4613732

a, b = 0, 1
w = b
answer = 0
while a < 4000000:
	a, b = b, a+b
	w = b
	if w%2 == 0:
		answer = answer + w
		
print 'Finished'					
print answer	