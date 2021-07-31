import numpy as np
import pandas as pd

from sklearn import svm
from sklearn.model_selection import train_test_split


df = pd.read_csv('~/microarray-ml/db/Liver_GSE14520_U133A.csv')
df.drop(['samples'], 1, inplace=True)

y = np.array(df['type'])

# 22278 columns after dropping samples
# runs=1: 273 .9+, 1865 .8+

features = []

# runs SVM on each gene to determine accuracy

for i in range(1, 22278):
    X = np.array(df[df.columns[i]])
    X.reshape(-1, 1)
    
    accuracy = 0.0
    runs = 1

    for ii in range(runs):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
        X_train = X_train.reshape(-1, 1)
        y_train = y_train.reshape(-1, 1)
        X_test  = X_test.reshape(-1, 1)

        clf = svm.SVC(kernel='rbf')
        clf.fit(X_train, y_train.ravel())

        accuracy += clf.score(X_test, y_test)
       
    features.append([accuracy / runs, df.columns[i], i])

# export genes to genes.txt in order of accuracy
features = sorted(features, reverse=True)
f = open('~/microarray-ml/genes.txt', 'w')
f.write("Gene, Column, Accuracy\n")
for feature in features:
    f.write("{}, {}, {}\n".format(feature[1], str(feature[2]), feature[0]))
f.close()