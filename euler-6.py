# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Answer : 25164150

# Sum of the squares of the first one hundred natural numbers

counter = 0
w = 0
sumofthesquares = 0
answer = 0

while counter < 100:
	counter = counter + 1
	w = counter * counter
	sumofthesquares = w + sumofthesquares
	
print 'Sum of the squares ', sumofthesquares

# Square of the sum

w = 0
counter = 0
while counter < 100:
	counter = counter + 1
	w = counter + w
w = w*w	
print 'Square of the sum ', w


# The difference

answer = w - sumofthesquares

print 'Finished'
print answer