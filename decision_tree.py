import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import preprocessing
from sklearn import metrics
from mpl_toolkits import mplot3d
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report    
from sklearn import tree
from sklearn.metrics import confusion_matrix 


df = preprocessing.preprocessing().get_df()
msk = np.random.rand(len(df)) < 0.8
training = df[msk]
testing = df[~msk]

feature_cols = ['Category','Installs','Reviews','Size','Price','Content Rating']
x_train = training[feature_cols]
y_train = training['Rating']
y_train = y_train.astype("int")
x_test = testing[feature_cols]
y_test = testing['Rating'] #target
y_test = y_test.astype("int")

clf = DecisionTreeClassifier()
clf = clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
