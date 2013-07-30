fib = [0,1,2]

x=2

while x <4000000:
	x = x + fib[-2]
	fib.append(x)

y = range(0,len(fib),2)


new_fib = []

for x in fib:
	if x%2==0:
		new_fib.append(x)
	
print sum (new_fib)


		



	


