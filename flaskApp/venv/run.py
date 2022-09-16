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

def main():

    loaded_model = joblib.load('finalized_model.sav')
    age = 50
    sex = 0
    cp = 0
    trestbps = 0
    chol = 0

    pred = loaded_model.predict(age,sex,cp,trestbps,chol,0,1,168,0,1,2,2,3)

    print(pred)

main()