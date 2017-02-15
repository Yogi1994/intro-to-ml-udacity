#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# size of enron dataset
print "size of enron dataset " , len(enron_data)

# numebr of features
print "numebr of features " , len(enron_data['GLISAN JR BEN F'])

number_of_poi = 0
for person in enron_data:
	if enron_data[person]['poi'] == 1 :
		number_of_poi += 1

# number of person of interest
print "number of person of interest", number_of_poi