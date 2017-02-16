#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#print len(features_train[0])
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc_min_samples_split_2 = accuracy_score(pred, labels_test)

clf2 = DecisionTreeClassifier(min_samples_split=50)
clf2 = clf2.fit(features_train, labels_train)
pred2 = clf2.predict(features_test)

acc_min_samples_split_50 = accuracy_score(pred2, labels_test)


print "->1 -> ", acc_min_samples_split_2
print "->2 -> ", acc_min_samples_split_50



#########################################################
### your code goes here ###


#########################################################


