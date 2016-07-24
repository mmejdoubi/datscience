import os
import numpy  as np
import csv as csv
from sklearn import preprocessing as prep
from collections import Counter

# Move to the data folder
os.chdir('/home/git/datscience/axa')

# Importe data file
# You need to remove 2 lines that aer corrupted with this command: sed -e '207773d;300849d' axa/data/ech_apprentissage.csv > data.csv

data = np.genfromtxt('data/ech_apprentissage.csv', delimiter=';', dtype='string')

# Columns
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
print marque[:5]


# Modifiing codepostal colum to keep only the first 2 caracters in a format with 5 caracters
postalCode = []
for code in data[:,6]:
    if len(code) == 4:
        postalCode.append(("0"+code)[:2])
    else:
        postalCode.append(code[:2])

letter_counts = Counter(postalCode)
print letter_counts
