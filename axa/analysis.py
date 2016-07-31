# docker run -ti -v /home/rave/Documents/git:/home/git continuumio/anaconda:version1 /bin/bash

import os
import numpy  as np
import csv as csv
from sklearn import preprocessing as prep
from collections import Counter
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import KFold
from sklearn import cross_validation
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error

# Move to the data folder
os.chdir('/home/git/datscience/axa')

data_raw = np.genfromtxt('data/ech_apprentissage.csv', delimiter=';', dtype='string')

header = data_raw[0, :]
data = data_raw[1:, :-2]
target = data_raw[1:, -1]


X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, target, test_size=0.4, random_state=0)


def postalCodeProcess( column ):

    postalCode = []
    for code in column:
        if len(code) == 4:
            postalCode.append(("0"+code)[:2])
        elif not code.isdigit():
            postalCode.append("00")
        else:
            postalCode.append(code[:2])


# label encoding
le_birthday = prep.LabelEncoder()
le_birthday.fit(data[:,1])

le_year = prep.LabelEncoder()
le_year.fit(data[:,2])

le_marque = prep.LabelEncoder()
le_marque.fit(data[:,3])

le_energie_veh = prep.LabelEncoder()
le_energie_veh.fit(data[:,7])

le_prof = prep.LabelEncoder()
le_prof.fit(data[:,10])

le_var1 = prep.LabelEncoder()
le_var1.fit(data[:,11])

le_var6 = prep.LabelEncoder()
le_var6.fit(data[:,16])

le_var8 = prep.LabelEncoder()
le_var8.fit(data[:,18])

le_var14 = prep.LabelEncoder()
le_var14.fit(data[:,24])

le_var16 = prep.LabelEncoder()
le_var16.fit(data[:,26])

# annee_naissance
# le_birthday = prep.LabelEncoder()
X_train[:,1] = le_birthday.transform(X_train[:,1])
X_test[:,1] = le_birthday.transform(X_test[:,1])

# annee_permis
# le_year = prep.LabelEncoder()
X_train[:,2] = le_year.transform(X_train[:,2])
X_test[:,2] = le_year.transform(X_test[:,2])

# marque
# le_marque = prep.LabelEncoder()
X_train[:,3] = le_marque.transform(X_train[:,3])
X_test[:,3] = le_marque.transform(X_test[:,3])

# code postal
X_train[:,6] = postalCodeProcess(X_train[:,6])
X_test[:,6] = postalCodeProcess(X_test[:,6])

# energie_veh
# le_energie_veh = prep.LabelEncoder()
X_train[:,7] = le_energie_veh.transform(X_train[:,7])
X_test[:,7] = le_energie_veh.transform(X_test[:,7])

# profession
# le_prof = prep.LabelEncoder()
X_train[:,10] = le_prof.transform(X_train[:,10])
X_test[:,10] = le_prof.transform(X_test[:,10])

# var1
# normalizer
# le_var1 = prep.LabelEncoder()
X_train[:,11] = le_var1.transform(X_train[:,11])
X_test[:,11] = le_var1.transform(X_test[:,11])

# var2
# ok

# var3
# ok

# var4
# ok

# var5
# ok

# var6
# le_var6 = prep.LabelEncoder()
X_train[:,16] = le_var6.transform(X_train[:,16])
X_test[:,16] = le_var6.transform(X_test[:,16])

# var7
# Remplacer NR par 0
for i in range(len(X_train)):
    if X_train[i,17] == 'NR':
        X_train[i,17] = '0.0'

for i in range(len(X_test)):
    if X_test[i,17] == 'NR':
        X_test[i,17] = '0.0'

# var8
# le_var8 = prep.LabelEncoder()
X_train[:,18] = le_var8.transform(X_train[:,18])
X_test[:,18] = le_var8.transform(X_test[:,18])

# var9
# Trop de valeurs

# var10
# Trop de valeurs

# var11
# Trop de valeurs

# var12
# Trop de valeurs

# var13
# ok

# var14
# le_var14 = prep.LabelEncoder()
X_train[:,24] = le_var14.transform(X_train[:,24])
X_test[:,24] = le_var14.transform(X_test[:,24])

# var15
# ok

# var16
# le_var16 = prep.LabelEncoder()
X_train[:,26] = le_var16.transform(X_train[:,26])
X_test[:,26] = le_var16.transform(X_test[:,26])

# var17
# ok

# var18
# ok

# var19
# ok

# var20
# ok

# var21
# ok

# var22
# ok

# remove colum 7 which is empty
X_train = np.delete(X_train, 6, 1)
X_test = np.delete(X_test, 6, 1)


# string to float
for i in range(1, 31):
    for j in range(0, len(X_train)):
        try:
            X_train[j, i] = float(X_train[j, i])
            # if X_train[j, i].dtype == '|S7':
                # print "dtype = "+str(X_train[j, i].dtype)+" i = "+str(i)+" j = "+str(j)
        except ValueError:
            print("train : i = "+str(i)+" j = "+str(j)+" val = "+X_train[j, i])

for i in range(1, 31):
    for j in range(0, len(X_test)):
        try:
            X_test[j, i] = float(X_test[j, i])
            # if X_train[j, i].dtype == '|S7':
                # print "dtype = "+str(X_train[j, i].dtype)+" i = "+str(i)+" j = "+str(j)
        except ValueError:
            print("test : i = "+str(i)+" j = "+str(j)+" val = "+X_test[j, i])

# print str(X_train[1].dtype)
# print str(X_train[1, 0])

# for i in range(1,27):
#     print "i = "+str(i)
#     letter_counts = Counter(X_train[:,i])
#     print letter_counts
#     print "\n"

# letter_counts = Counter(X_train[:,7])
# print letter_counts

# letter_counts = Counter(X_train[:,6])
# print letter_counts

X_train = X_train.astype(np.float32)
y_train = y_train.astype(np.float32)
X_test = X_test.astype(np.float32)
y_test = y_test.astype(np.float32)

model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0, loss='ls').fit(X_train[:, 1:], y_train)
y_pred = model.predict(X_test[:, 1:])

print mean_squared_error(y_test, y_pred)
print explained_variance_score(y_test, y_pred, multioutput='uniform_average')
print mean_squared_error(y_test, y_pred)

# print len(y_train)
# print len(X_train[:, 1:])
# print X_train.shape
