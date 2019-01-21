# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

#import dataset--------
df = pd.read_csv('balanceddata.csv')
y= df['2. Category']
X_data = [str(x) for x in df['Description']]

#data preprocessing
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_le=le.fit_transform(y)

from sklearn.feature_extraction.text import CountVectorizer
ct=CountVectorizer()
X_data_ct = ct.fit_transform(X_data)

#data split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data_ct,y_le)


classifiers = {'1': MultinomialNB(),
               '2': LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial'),
               '3': svm.LinearSVC(),
               '4': RandomForestClassifier(n_jobs=-1),
               '5': DecisionTreeClassifier(random_state=0),
               '6': MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=1000,activation='logistic')
               }

for clf in classifiers.values():

    print("Started training model!")
    clf.fit(X_train, y_train)
    print("Started test model!")
    y_pred = clf.predict(X_test)
    print("Results")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))


#model save
from sklearn.externals import joblib
joblib.dump(ct, 'ct_log.joblib')
joblib.dump(le, 'le_log.joblib')
joblib.dump(mlp, 'mlpdata_log.joblib')