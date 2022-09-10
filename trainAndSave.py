from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from collections import Counter
import joblib
### EXTRACTING DATA
data = pd.read_csv("heart.csv")
data = data.sample(frac = 1)
### DROPPING ROWS THAT CAN SKEW THE DATA IN NAIVE BAYES CLASSIFIER
X = data.drop(['trestbps','chol','thalach','oldpeak'],axis = 'columns').values
#DROPPING THE LABELS TO GET THE DATA OUT
y = data['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4225, random_state=0)
#TRAINING AND TESTING THE CLASSIFIER
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
# Model Accuracy, how often is the classifier correct?
acc_score = accuracy_score(y_test, y_pred)
conf_mat = confusion_matrix(
        y_test, y_pred)

print(acc_score)
print(conf_mat)

# save the model to disk
filename = 'finalized_model.sav'
joblib.dump(gnb, filename)
