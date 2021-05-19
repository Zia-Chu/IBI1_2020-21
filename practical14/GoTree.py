import re
#load an XML document and create a minidom object
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir('C:\cygwin64\home\wjw\Practical14')
go_obo=open('go_obo.xml','r')
#use dom to form a tree structure
DOMTree=xml.dom.minidom.parse('go_obo.xml')
# define the document element
obo=DOMTree.documentElement
#get the term element
terms=obo.getElementsByTagName('term')
DNA_number=0
RNA_number=0
Protein_number=0
Carbohydrate_number=0
i=0
#create a list longer than 2000000
loc=[0]*3000000
#create a function to find the childnodes or parentnodes
def find(j,term):
    is_a = []
    flag = False
    is_a = term.getElementsByTagName('is_a')
    if is_a == []:
        flag = False
    else:
        for a in is_a:
            parentid = a.childNodes[0].data
#get the parentid
            s = re.findall(':(\d.*)$',parentid)
#turn the parentid into numbers
            digitid = int(s[0])
#locate the fatherterm
            fatherterm = terms[loc[digitid]]
#find defstr
            defstr = fatherterm.getElementsByTagName('defstr')[0]
            d = defstr.childNodes[0].data
#find specific types of gene by text contents
            if re.search(j,d):
                flag = True
            elif find(j,fatherterm):
                flag = True
    return flag


for term in terms:
 termid=term.getElementsByTagName('id')[0].childNodes[0].data
 p=re.findall(':(\d.*)$',termid)
 q=int(p[0])
 loc[q]=i
 i=i+1
#count the number
#get the number of childnodes associated with DNA
for term in terms:
 if find('DNA',term):
  DNA_number+=1

#get the number of childnodes associated with RNA
for term in terms:
 if find('RNA',term):
  RNA_number+=1

#get the number of childnodes associated with protein
for term in terms:
 if find('protein',term):
  Protein_number+=1

#choose carbohydrate as the fourth macromolecule
#get the number of childnodes associated with it
for term in terms:
 if find('carbohydrate',term):
  Carbohydrate_number+=1

print('The Number of ChildNodes Associated with DNA:',DNA_number)
print('The Number of ChildNodes Associated with RNA:',RNA_number)
print('The Number of ChildNodes Associated with Protein:',Protein_number)
print('The Number of ChildNodes Associated with Carbohydrate:',Carbohydrate_number)

#draw a pie chart showing these four numbers
labels='DNA-associated\n'+str(DNA_number),'RNA-associated\n'+str(RNA_number),'Protein-associated\n'+str(Protein_number),'Carbohydrate-associated\n'+str(Carbohydrate_number)
plt.pie([DNA_number,RNA_number,Protein_number,Carbohydrate_number],explode=None,labels=labels,colors=('y','r','b','c'),autopct='%1.2f%%',pctdistance=0.7,shadow=True, labeldistance=1.0,startangle=0,radius=1.2,counterclock=False,wedgeprops=None,textprops=None,center=(0,0),frame=False)
plt.title('Numbers of ChildNodes')
plt.axis('equal')
plt.show()




