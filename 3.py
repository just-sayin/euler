x = 2
large = 600851475143 
factors = []

while x < 10000000: #get factors, put them in an array, i would like a more efficient way but couldnt think of one
	while large % x != 0:
		x+=1
	factors.append(x)
	x+=1

y = 0

while y<10:  #i iterated the while loop 10 times, this was chosen at random.
	for num in factors: #this finds out whether any numbers in the array are multiples of others, then gets rid of them.
		if factors[-1]!=num:
			if factors[-1]%num==0:
				del factors[-1]
	y+=1

print max(factors)













