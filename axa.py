# Add volume to the docker : docker run -ti -v /home/rave/Documents/git:/home/git continuumio/anaconda:version1 /bin/bash

import os
import numpy  as np
import csv as csv
from sklearn import preprocessing as prep
from collections import Counter

# Move to the data folder
os.chdir('/home/git/datscience/axa')


with open('data/ech_apprentissage.csv') as f:
    lines = f.readlines()

# Importe data file
# You need to remove 2 lines that aer corrupted with this command: sed -e '207773d;300849d' axa/data/ech_apprentissage.csv > data.csv

data_raw = np.genfromtxt('data/ech_apprentissage.csv', delimiter=';', dtype='string')

header = data_raw[0, :]
data = data_raw[1:, :]


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
# 'var7',
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
# print marque[:5]


# Modifiing codepostal column to keep only the first 2 caracters in a format with 5 caracters
# Trop de valeurs
postalCode = []
for code in data[:,6]:
    if len(code) == 4:
        postalCode.append(("0"+code)[:2])
    elif not code.isdigit():
        postalCode.append("00")
    else:
        postalCode.append(code[:2])

print "code postal"
letter_counts = Counter(postalCode)
print letter_counts


# Encoding energie_veh
# labeliser
le_energie_veh = prep.LabelEncoder()
energie_veh = le_energie_veh.fit_transform(data[:,7])

print "energie_veh"
letter_counts = Counter(data[:,7])
print letter_counts

# Encoding profession
# labeliser
le_prof = prep.LabelEncoder()
prof = le_prof.fit_transform(data[:,10])

print "profession"
letter_counts = Counter(data[:,10])
print letter_counts


# Encoding var1
# Trop de valeurs
le_var1 = prep.LabelEncoder()
var1 = le_var1.fit_transform(data[:,11])

print "var1"
letter_counts = Counter(data[:,11])
print letter_counts


# Encoding var2
# ok
le_var2 = prep.LabelEncoder()
var2 = le_var2.fit_transform(data[:,12])

print "var2"
letter_counts = Counter(data[:,12])
print letter_counts


# Encoding var3
# ok
le_var3 = prep.LabelEncoder()
var3 = le_var3.fit_transform(data[:,13])

print "var3"
letter_counts = Counter(data[:,13])
print letter_counts

# Encoding var4
# ok
le_var4 = prep.LabelEncoder()
var4 = le_var4.fit_transform(data[:,14])

print "var4"
letter_counts = Counter(data[:,14])
print letter_counts


# Encoding var5
# ok
le_var5 = prep.LabelEncoder()
var5 = le_var5.fit_transform(data[:,15])

print "var5"
letter_counts = Counter(data[:,15])
print letter_counts


# Encoding var6
# a labeliser
le_var6 = prep.LabelEncoder()
var6 = le_var6.fit_transform(data[:,16])

print "var6"
letter_counts = Counter(data[:,16])
print letter_counts


# Encoding var7
# Remplacer NR par 0
le_var7 = prep.LabelEncoder()
var7 = le_var7.fit_transform(data[:,17])

print "var7"
letter_counts = Counter(data[:,17])
print letter_counts


# Encoding var8
# A labeliser
le_var8 = prep.LabelEncoder()
var8 = le_var8.fit_transform(data[:,18])

print "var8"
letter_counts = Counter(data[:,18])
print letter_counts


# Encoding var9
# Trop de valeurs
le_var9 = prep.LabelEncoder()
var9 = le_var9.fit_transform(data[:,19])

print "var9"
letter_counts = Counter(data[:,19])
print letter_counts


# Encoding var10
# Trop de valeurs
le_var10 = prep.LabelEncoder()
var10 = le_var10.fit_transform(data[:,20])

print "var10"
letter_counts = Counter(data[:,20])
print letter_counts


# Encoding var11
# Trop de valeurs
le_var11 = prep.LabelEncoder()
var11 = le_var11.fit_transform(data[:,21])

print "var11"
letter_counts = Counter(data[:,21])
print letter_counts


# Encoding var12
# Trop de valeurs
le_var12 = prep.LabelEncoder()
var12 = le_var12.fit_transform(data[:,22])

print "var12"
letter_counts = Counter(data[:,22])
print letter_counts


# Encoding var13
# ok
le_var13 = prep.LabelEncoder()
var13 = le_var13.fit_transform(data[:,23])

print "var13"
letter_counts = Counter(data[:,23])
print letter_counts


# Encoding var14
# A labeliser
le_var14 = prep.LabelEncoder()
var14 = le_var14.fit_transform(data[:,24])

print "var14"
letter_counts = Counter(data[:,24])
print letter_counts



# Encoding var15
# ok
le_var15 = prep.LabelEncoder()
var15 = le_var15.fit_transform(data[:,25])

print "var15"
letter_counts = Counter(data[:,25])
print letter_counts


# Encoding var16
# A labeliser
le_var16 = prep.LabelEncoder()
var16 = le_var16.fit_transform(data[:,26])

print "var16"
letter_counts = Counter(data[:,26])
print letter_counts

# Encoding var17
# ok
le_var17 = prep.LabelEncoder()
var17 = le_var17.fit_transform(data[:,27])

print "var17"
letter_counts = Counter(data[:,27])
print letter_counts


# Encoding var18
# ok
le_var18 = prep.LabelEncoder()
var18 = le_var18.fit_transform(data[:,28])

print "var18"
letter_counts = Counter(data[:,28])
print letter_counts


# Encoding var19
# ok
le_var19 = prep.LabelEncoder()
var19 = le_var19.fit_transform(data[:,29])

print "var19"
letter_counts = Counter(data[:,29])
print letter_counts



# Encoding var20
# ok
le_var20 = prep.LabelEncoder()
var20 = le_var20.fit_transform(data[:,30])

print "var20"
letter_counts = Counter(data[:,30])
print letter_counts


# Encoding var21
# ok
le_var21 = prep.LabelEncoder()
var21 = le_var21.fit_transform(data[:,31])

print "var21"
letter_counts = Counter(data[:,31])
print letter_counts


# Encoding var22
# ok
le_var22 = prep.LabelEncoder()
var22 = le_var22.fit_transform(data[:,32])

print "var22"
letter_counts = Counter(data[:,32])
print letter_counts


# Encoding prime
# Trop de valeurs
# le_prime = prep.LabelEncoder()
# prime = le_prime.fit_transform(data[:,33])
#
# print "prime"
# letter_counts = Counter(data[:,33])
# print letter_counts
