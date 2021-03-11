#Assign the total number n=84
#Assign the r rate m=1.2


n=84
m=2.2
a,b=n,m*n
for i in range(4):
	a,b=b,m*b
	print(b)
