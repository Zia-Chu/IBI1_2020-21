import re
#load an XML document and create a minidom object
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import matplotlib.pyplot as plt
import pandas as pd
# find the xml file
os.chdir('C:\cygwin64\home\wjw\Practical14')
go_obo=open('go_obo.xml','r')
#use dom to form a tree structure
DOMTree=xml.dom.minidom.parse('go_obo.xml')
# define the document element because obo is ended at the end of file and start initially
obo=DOMTree.documentElement
#get the term element
terms=obo.getElementsByTagName('term')
# initialise the needed variables
DNA_number=0
RNA_number=0
Protein_number=0
Glycoprotein_number=0
i=0
#create a list longer than 2000000
loc=[0]*3000000
#create a function to find the childnodes or parentnodes
def find(j,term):
    is_a = []
    flag = False
    is_a = term.getElementsByTagName('is_a')# find every element'is_a'
    if is_a == []:
        flag = False
    else:
        for a in is_a:
            parentid = a.childNodes[0].data
#find the parentid of is_a
            s = re.findall(':(\d.*)$',parentid)
#turn the parentid into numbers
            digitid = int(s[0])
#localise the parentterm
            parentterm = terms[loc[digitid]]
#find defstr
            defstr = parentterm.getElementsByTagName('defstr')[0]
            d = defstr.childNodes[0].data
#find specific types of gene by text contents
            if re.search(j,d):
                flag = True
            elif find(j,parentterm):
                flag = True
    return flag


for term in terms:
 termid=term.getElementsByTagName('id')[0].childNodes[0].data
 p=re.findall(':(\d.*)$',termid)
 q=int(p[0])
 loc[q]=i
 i=i+1

#find the number of childnodes associated with DNA
for term in terms:
 if find('DNA',term):
  DNA_number+=1 # count step by step

#find the number of childnodes associated with RNA
for term in terms:
 if find('RNA',term):
  RNA_number+=1

#find the number of childnodes associated with protein
for term in terms:
 if find('protein',term):
  Protein_number+=1

#find the number of childnodes associated with glycoprotein
for term in terms:
 if find('glycoprotein',term):
  Glycoprotein_number+=1

print('The number of childnodes associated with DNA:',DNA_number)
print('The number of childnodes associated with RNA:',RNA_number)
print('The number of childnodes associated with Protein:',Protein_number)
print('The number of childnodes associated with Carbohydrate:',Glycoprotein_number)

#draw a pie chart showing these four numbers
labels='DNA-associated\n'+str(DNA_number),'RNA-associated\n'+str(RNA_number),'Protein-associated\n'+str(Protein_number),'Carbohydrate-associated\n'+str(Glycoprotein_number)
plt.pie([DNA_number,RNA_number,Protein_number,Glycoprotein_number],explode=None,labels=labels,colors=('y','r','b','c'),autopct='%1.2f%%',pctdistance=0.8,shadow=False, labeldistance=1.0,startangle=30,radius=1.2,counterclock=False,wedgeprops=None,textprops=None,center=(0,0),frame=False)
plt.title('Numbers of Childnodes')
plt.axis('equal')
plt.show()




