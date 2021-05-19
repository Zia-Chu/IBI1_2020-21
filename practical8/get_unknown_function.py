import re
import os
os.chdir('C:\cygwin64\home\wjw\Practical8')
# open and read the FASTA file
# create and write a new FASTA file
f1=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
f2=open('inter.fa','w')
# delete the \n to avoid changing line within sequence but not delete the \n at the end of each sequence
for line in f1:
    if line.startswith('>'):
        line1=re.sub(r'>','\n>',line)
        f2.write(line1)
    else:
        line2=re.sub(r'\n','',line)
        f2.write(line2)
f1.close()
f2.close()
f2=open('inter.fa','r')
function=[]
gene=[]
#seperate the name and description
for line in f2:
    if line.startswith('>'):
        function.append(line)
    elif line.startswith('\n'):
        del(line)
    else:
        gene.append(line)
f2.close()
# make index for unknown function gene
unknown_gene_index=[]
count=-1
for item in function:
    count+=1
    if re.search(r'unknown function',item):
        unknown_gene_index.append(count)
    else:
        continue
# caculate the length of unknown gene by index
length=[]
for i in unknown_gene_index:
    length.append(len(gene[i])-1)
# create a blank list to store name
name=[]
for i in unknown_gene_index:
    name.append(re.findall(r'>([a-zA-Z0-9\-]+)',function[i]))
# create a list for gene sequences
unknown_gene=[]
for i in unknown_gene_index:
    unknown_gene.append(gene[i])
# create and write a FASTA file
# write the name, length and sequence into the new file
f3=open('unknown_function.fa','w')
for i in range(0,len(unknown_gene_index)):
    x1=str(name[i])
    x2=x1.strip("'[]")
    y=str(length[i])+'\n'
    f3Line1=' '.join([x2,y])
    f3Line2=str(unknown_gene[i])
    f3.write(f3Line1)
    f3.write(f3Line2)
f3.close()





