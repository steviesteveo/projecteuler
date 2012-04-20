# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer : 233168

i = 1
w = 0
answer = 0
while i < 1000:
	print i
	w = i%3
	if 0 == w:
			answer = answer + i
			print answer
	elif w > 0:	
			w = i%5
			if w == 0:
				answer = answer + i
				print answer
			else:
				print 'not a multiple of 5'
	else:
		print 'not a multiple of 3'
	i = i + 1