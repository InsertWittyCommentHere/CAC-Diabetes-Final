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


plt.switch_backend('Agg') 
print(os.listdir('.'))

dataset = pd.read_csv("data/diabetes_012_health_indicators_BRFSS2015.csv")

df = dataset

df.dropna(inplace = True)

# Checking duplicates
duplicate = df[df.duplicated()]

# Removing duplicate rows from the dataset
df.drop_duplicates(inplace = True)

duplicate = df[df.duplicated()]

# GRP 1 - "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack"
# GRP 2 - "Smoker", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", GRP 1
# GRP 3 - "GenHlth", "PhysHlth", "MentHlth", "DiffWalk", GRP 2
# GRP 4 - "Age", "Sex", "Education", "Income", GRP 3
# GRP 5 - "CholCheck", "AnyHealthcare", "NoDocbcCost", GRP 4   (Entire Dataset)

group1 = dataset[["Diabetes_012", "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack"]].copy()
group2 = dataset[["Diabetes_012", "Smoker", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack"]].copy()
group3 = dataset[["Diabetes_012", "GenHlth", "PhysHlth", "MentHlth", "DiffWalk", "Smoker", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack"]].copy()
group4 = dataset[["Diabetes_012", "GenHlth", "PhysHlth", "MentHlth", "DiffWalk", "Smoker", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack", "Age", "Sex", "Education", "Income"]].copy()
group5 = dataset


#df = df[["Diabetes_012", "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack"]]

### OverSampling ###
# in our dataset the label is diabetes column

# This will return the label distribution count 
df['Diabetes_012'].value_counts()

# over sampling of the dataset to get a balanced dataset
class_0 = df[df['Diabetes_012'] == 0]
class_1 = df[df['Diabetes_012'] == 1]
class_2 = df[df['Diabetes_012'] == 2]

# over sampling of the minority classes 1 and 2
class_1_over = class_1.sample(len(class_0), replace=True)
class_2_over = class_2.sample(len(class_0), replace=True)

# Creating a new dataframe with over sampled class 1 df and class 0 df
df_new = pd.concat([class_1_over, class_0, class_2_over], axis=0)

### Splitting dataset to train and test

X = df_new.drop('Diabetes_012', axis = 1) # features
y = df_new[['Diabetes_012']] # labels

# splitting the features and labels into train and test with test size = 20% and train size = 80%
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=10)

### Fit Random Forest classifier

# Initializing the model w/ n_estimators = 100
model_2 = RandomForestClassifier(n_estimators = 100, criterion = 'entropy',
                            min_samples_split=2, random_state=0)

# fitting the model on the train data
model_2.fit(X_train, y_train)

# predicting values on test data
predictions = model_2.predict(X_test)

# calculating the accuracy of the model
accuracies = {}
accuracy_1 = accuracy_score(y_test, predictions)
accuracies['Random Forest Classifier'] = accuracy_1

# calculating the classification report 
classificationreport = classification_report(y_test, predictions) 

# calculating the mse 
mse = mean_squared_error(y_test, predictions)

# calculating the rmse 
rmse = math.sqrt(mse)
print('\nAccuracy score of Random Forest Classifier: ' + str(round(accuracy_1*100, 2)))
print("\n"+"*"*50)
print('\nClassification_report : ')
print(classificationreport)
print("\n"+"*"*50)
print('\nMean squared error : '+ str(mse))
print("\n"+"*"*50)
print('\nRoot mean squared error : '+ str(rmse))


# Saving model using pickle
pickle.dump(model_2, open('model.pkl','wb'))


# Loading model to compare the results
#model = pickle.load( open('model.pkl','rb'))
#print(model.predict([[1.8]]))