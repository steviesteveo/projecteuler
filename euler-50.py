# Which prime, below one-million, can be written as the sum of the most consecutive primes?



# A fast prime number list generator (Python recipe)   
# http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/ 

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

print primes(1000000)
