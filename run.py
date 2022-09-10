import joblib
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv("heart.csv")
data = data.sample(frac = 1)
### DROPPING ROWS THAT CAN SKEW THE DATA IN NAIVE BAYES CLASSIFIER
X = data.drop(['trestbps','chol','thalach','oldpeak'],axis = 'columns').values
#DROPPING THE LABELS TO GET THE DATA OUT
y = data['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4225, random_state=0)

loaded_model = joblib.load('finalized_model.sav')
