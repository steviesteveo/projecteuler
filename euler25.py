# What is the first term in the Fibonacci sequence to contain 1000 digits?
	
so_far = 0	
a, b = 0, 1
run = True
term = 0

while run == True:
	term += 1
	a, b = b, a + b
	so_far = len(str(a)) 
	print term
	print so_far
	print run
	if len(str(a)) == 1000:
		run == False

answer = term
	
print "Answer is: %d" % answer