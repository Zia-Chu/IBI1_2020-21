a=29862124
b=11285561
c=11205972
d=4360823
e=4234924
x=a+b+c+d+e
#assign the total number for five countries and respective numbers for each 
countries={'USA':a/x,'India':b/x,'Brazil':c/x,'Russia':d/x,'UK':e/x}
#assign a dictionary called countries
print(countries)
#print the frequency dictionary
import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
#name five parts of pie chart counter-clockwise 
sizes=[100*a/x,100*b/x,100*c/x,100*d/x,100*e/x]
explode=(0,0,0,0,0.3)
#specify the part labeled 'UK' to offset the pie chart
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
#equal aspect ratio ensures that pie is drawn as a circle
plt.show()
