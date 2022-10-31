import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error
from pandas_profiling import ProfileReport
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
#from mlxtend.plotting import plot_confusion_matrix
from sklearn import tree
import math
import warnings
import matplotlib.pyplot as plt


import seaborn as sns
import numpy as np
import os


import pickle
import requests
import json



'''
This model predicts the diabetics for a given individual data
'''




# Diabetes_012,HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,HeartDiseaseorAttack,PhysActivity,Fruits,Veggies,HvyAlcoholConsump,AnyHealthcare,NoDocbcCost,GenHlth,MentHlth,PhysHlth,DiffWalk,Sex,Age,Education,Income
# [0,1,1,1,40,1,0,0,0,0,1,0,1,0,5,18,15,1,0,9,4,3]
# [0,0,0,0,25,1,0,0,1,0,0,0,0,1,3,0,0,0,0,7,6,1]
# [0,1,1,1,28,0,0,0,0,1,0,0,1,1,5,30,30,1,0,9,4,8]
# [0,1,0,1,27,0,0,0,1,1,1,0,1,0,2,0,0,0,0,11,3,6]
# [0,1,1,1,24,0,0,0,1,1,1,0,1,0,2,3,0,0,0,11,5,4]
# [0,1,1,1,25,1,0,0,1,1,1,0,1,0,2,0,2,0,1,10,6,8]

# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))


print(model.predict([[1,1,1,40,1,0,0,0,0,1,0,1,0,5,18,15,1,0,9,4,3]]))
print(model.predict([[0,0,0,25,1,0,0,1,0,0,0,0,1,3,0,0,0,0,7,6,1]]))
print(model.predict([[1,1,1,28,0,0,0,0,1,0,0,1,1,5,30,30,1,0,9,4,8]]))
print(model.predict([[1,0,1,27,0,0,0,1,1,1,0,1,0,2,0,0,0,0,11,3,6]]))
print(model.predict([[1,1,1,24,0,0,0,1,1,1,0,1,0,2,3,0,0,0,11,5,4]]))
print(model.predict([[1,1,1,25,1,0,0,1,1,1,0,1,0,2,0,2,0,1,10,6,8]]))