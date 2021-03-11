#Name the first two number and assign them 1
#The third number is the sum of the first two
#Regard the second number as the first number
#How many times changed the first number?
#	if less than 12: Keep changing
#	if 12: Done	


a,b=1,1
for i in range(12):
	a,b =b,a+b
	print(a)
