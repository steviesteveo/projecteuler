# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Answer : 232792560 

answer = 0
counter = 0

while answer == 0: 
	counter = counter + 2520
	if counter%19 == 0:
		if counter%18 == 0:
			if counter%17 == 0:
				if counter%16 == 0:
					if counter%15 == 0:
						if counter%14 == 0:
							if counter%13 == 0:								
								if counter%11 == 0:
									answer = counter												
												
print 'Finished'											
print answer	
							

# Factors
# 20 (2, 4, 5, 10, 20)
# 19 prime
# 18 (2, 3, 6, 9)
# 17 prime
# 16 (2, 4, 8)
# 15 (3, 5)
# 14 (2, 7)
# 13 prime
# 12 (2, 3, 4, 6)
# 11 prime
# 10 (2, 5)
# 9 (3)
# 8 (2, 4)
# 7 prime
# 6 (2, 3)
# 5 prime
# 4 (2)
# 3 prime
# 2 prime
# 1 
# 
# 2520 = smallest positive number divisible by numbers 1 - 10 (also 11 - 20)