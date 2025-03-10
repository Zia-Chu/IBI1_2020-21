import re
import os
os.chdir('C:\cygwin64\home\wjw\Practical11')

fName1=input('Please enter human sequence filename: ')
fName2=input('Please enter mouse sequence filename: ')
fName3=input('Please enter random sequence filename: ')
blosum62 = {
     'WF': 1,'LR': -2,'SP': -1, 'VT': 0,
    'QQ': 5, 'NA': -2,'ZY': -2, 'WR': -3,
    'QA': -1,'SD': 0, 'HH': 8, 'SH': -1,
    'HD': -1,'LN': -3, 'WA': -3, 'YM': -1,
    'GR': -2, 'YI': -1, 'YE': -2, 'BY': -3,
    'YA': -2, 'VD': -3, 'BS': 0, 'YY': 7,
    'GN': 0, 'EC': -4, 'YQ': -1, 'ZZ': 4,
    'VA': 0, 'CC': 9, 'MR': -1, 'VE': -2,
    'TN': 0, 'PP': 7, 'VI': 3, 'VS': -2,
    'ZP': -1, 'VM': 1, 'TF': -2, 'VQ': -2,
    'KK': 5, 'PD': -1, 'IH': -3, 'ID': -3,
    'TR': -1, 'PL': -3, 'KG': -2, 'MN': -2,
    'PH': -2, 'FQ': -3, 'ZG': -2, 'XL': -1,
    'TM': -1, 'ZC': -3, 'XH': -1, 'DR': -2,
    'BW': -4, 'XD': -1, 'ZK': 1, 'FA': -2,
    'ZW': -3, 'FE': -3, 'DN': 1, 'BK': 0,
    'XX': -1, 'FI': 0, 'BG': -1, 'XT': 0,
    'FM': 0, 'BC': -3, 'ZI': -3, 'ZV': -2,
    'SS': 4, 'LQ': -2, 'WE': -3, 'QR': 1,
    'NN': 6, 'WM': -1, 'QC': -3, 'WI': -3,
    'SC': -1, 'LA': -1, 'SG': 0, 'LE': -3,
    'WQ': -2, 'HG': -2, 'SK': 0, 'QN': 0,
    'NR': 0, 'HC': -3, 'YN': -2, 'GQ': -2,
    'YF': 3, 'CA': 0, 'VL': 1, 'GE': -2,
    'GA': 0, 'KR': 2, 'ED': 2, 'YR': -2,
    'MQ': 0, 'TI': -1, 'CD': -3, 'VF': -1,
    'TA': 0, 'TP': -1, 'BP': -2, 'TE': -1,
    'VN': -3, 'PG': -2, 'MA': -1, 'KH': -1,
    'VR': -3, 'PC': -3, 'ME': -2, 'KL': -2,
    'VV': 4, 'MI': 1, 'TQ': -1, 'IG': -4,
    'PK': -1, 'MM': 5, 'KD': -1, 'IC': -1,
    'ZD': 1, 'FR': -3, 'XK': -1, 'QD': 0,
    'XG': -1, 'ZL': -3, 'XC': -2, 'ZH': 0,
    'BL': -4, 'BH': 0, 'FF': 6, 'XW': -2,
    'BD': 4, 'DA': -2, 'SL': -2, 'XS': 0,
    'FN': -3, 'SR': -1, 'WD': -4, 'VY': -1,
    'WL': -2, 'HR': 0, 'WH': -2, 'HN': 1,
    'WT': -2, 'TT': 5, 'SF': -2, 'WP': -4,
    'LD': -4, 'BI': -3, 'LH': -3, 'SN': 1,
    'BT': -1, 'LL': 4, 'YK': -2, 'EQ': 2,
    'YG': -3, 'ZS': 0, 'YC': -2, 'GD': -1,
    'BV': -3, 'EA': -1, 'YW': 2, 'EE': 5,
    'YS': -2, 'CN': -3, 'VC': -1, 'TH': -2,
    'PR': -2, 'VG': -3, 'TL': -1, 'VK': -2,
    'KQ': 1, 'RA': -1, 'IR': -3, 'TD': -1,
    'PF': -4, 'IN': -3, 'KI': -3, 'MD': -3,
    'VW': -3, 'WW': 11, 'MH': -2, 'PN': -2,
    'KA': -1, 'ML': 2, 'KE': 1, 'ZE': 4,
    'XN': -1, 'ZA': -1, 'ZM': -1, 'XF': -1,
    'KC': -3, 'BQ': 0, 'XB': -1, 'BM': -3,
    'FC': -2, 'ZQ': 3, 'XZ': -1, 'FG': -3,
    'BE': 1, 'XV': -1, 'FK': -3, 'BA': -2,
    'XR': -1, 'DD': 6, 'WG': -2, 'ZF': -3,
    'SQ': 0, 'WC': -2, 'WK': -3, 'HQ': 0,
    'LC': -1, 'WN': -4, 'SA': 1, 'LG': -4,
    'WS': -3, 'SE': 0, 'HE': 0, 'SI': -2,
    'HA': -2, 'SM': -1, 'YL': -1, 'YH': 2,
    'YD': -3, 'ER': 0, 'XP': -2, 'GG': 6,
    'GC': -3, 'EN': 0, 'YT': -2, 'YP': -3,
    'TK': -1, 'AA': 4, 'PQ': -1, 'TC': -1,
    'VH': -3, 'TG': -2, 'IQ': -3, 'ZT': -1,
    'CR': -3, 'VP': -2, 'PE': -1, 'MC': -1,
    'KN': 0, 'II': 4, 'PA': -1, 'MG': -3,
    'TS': 1, 'IE': -3, 'PM': -2, 'MK': -1,
    'IA': -1, 'PI': -3, 'RR': 5, 'XM': -1,
    'LI': 2, 'XI': -1, 'ZB': 1,'XE': -1,
    'ZN': 0, 'XA': 0, 'BR': -1, 'BN': 3,
    'FD': -3, 'XY': -1, 'ZR': 0, 'FH': -1,
    'BF': -3, 'FL': 0, 'XQ': -1, 'BB': 4}

alignment1=''
alignment2=''
alignment3=''
edit_distance1 = 0
edit_distance2 = 0
edit_distance3 = 0

with open(fName1, 'r') as f1:
    seq1 = f1.read()
with open(fName2,'r') as f2:
    seq2=f2.read()
with open(fName3, 'r') as f3:
    seq3 = f3.read()
with open('blosum62.txt', 'r') as f3:
    seq3 = f3.read()

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        edit_distance1 += 1
print(edit_distance1)


