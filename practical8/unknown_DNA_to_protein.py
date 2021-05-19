import os
import re
# find and open the file we created in last task
os.chdir('C:\cygwin64\home\wjw\Practical8')
f=open('unknown_function.fa','r')
# create two list to store sequence and name seperately
DNA=[]
name=[]
for line in f:
    if re.search(r'^[AGCT]',line):
        DNA.append(line)
    else:
        newline=re.findall(r'(^\S+)\s+',line)
        name.append(line)
f.close()
# use a dictionary to store transcription information
table={'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }
aminostr=''
amino=[]
for i in DNA:
    seq=str(i)
    valid=len(seq)-len(seq)%3 # read sequence 3 by 3 and assign the codon
    for j in range(0,valid,3):
        key=seq[j:j+3]
        aminostr=aminostr+table[key]
    amino.append(aminostr)
    aminostr=''
#caculate the length
protein_length=[]
for i in amino:
    protein_length.append(len(i))
# allow to rename the FASTA file
# the new name is still end with .fa
file_name=input('Please input filename: ')
if file_name.endswith('.fa'):
    f2=open(file_name,'w')
    for i in range(0,len(name)):
        newname=str(name[i]).strip("'[]")
        line1='Name: '+newname+'\n'
        line2='Protein length: '+str(protein_length[i])+'\n'
        line3='Protein: '+str(amino[i])+'\n'
        f2.write(line1)
        f2.write(line2)
        f2.write(line3)
    f2.close()
    f2=open(file_name,'r')
    print(f2.read())
else:
    print('Please enter a FASTA filename with " .fa": ')
