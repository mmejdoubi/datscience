import os
import numpy  as np
import csv as csv
from sklearn import preprocessing as prep
from collections import Counter

# Move to the data folder
os.chdir('/home/git/datscience/axa')

# Importe data file
# csv_file_object = csv.reader(open('data/ech_apprentissage.csv', 'rb'), delimiter=';', quotechar='|') 
# header = csv_file_object.next() 
# data=[] 

data = np.genfromtxt('data/ech_apprentissage.csv',delimiter=',')

# for row in csv_file_object:
#    data.append(row)
    
# data = np.array(data).reshape() 
 
#['id', 
# 'annee_naissance',   
# 'annee_permis', 
# 'marque', 
# 'puis_fiscale', 
# 'anc_veh', 
# 'codepostal', 
# 'energie_veh', 
# 'kmage_annuel', 
# 'crm', 
# 'profession', 
# 'var1', 
# 'var2', 
# 'var3', 
# 'var4', 
# 'var5', 
# 'var6', 
# 'var7', 
# 'var8', 
# 'var9', 
# 'var10', 
# 'var11', 
# 'var12', 
# 'var13', 
# 'var14', 
# 'var15', 
# 'var16', 
# 'var17', 
# 'var18', 
# 'var19', 
# 'var20', 
# 'var21', 
# 'var22', 
# 'prime_tot_ttc']

# Encoding column marque
le_marque = prep.LabelEncoder()
marque = le_marque.fit_transform(data[:,3])
print type(data)
print data[0,0]


# Modifiing codepostal colum to keep only the first 2 caracters in a format with 5 caracters
postalCode = []

for row in data[:5,]:
    if len(row[6]) == 4:
        postalCode.append((\"0\"+row[6])[:2])
    else:
        postalCode.append(row[6][:2])

# letter_counts = Counter(postalCode)

# letter_counts = Counter([row[6] for row in data])

# print letter_counts\n"