# What does this piece of code do?
# Answer: To draw ramdom number until a number<=50 is drawn. 

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
#Judge whether p satisfies "while" condition, the loop will continue if it does, otherwise the loop will break.
	n = randint(1,100)
#Draw number randomly in the range of (1,100)
	if n > 50:
		p = False
#If n > 50, the loops will continue.

print(n)
#The number breaks the loop will be printed
