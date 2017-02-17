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
	# print person
	if enron_data[person]['poi'] == 1 :
		number_of_poi += 1

# number of person of interest
print "number of person of interest", number_of_poi

poi_names_file = open('../final_project/poi_names.txt','r')
poi_names = []
for line in poi_names_file:
	if(line[0] == '('):
		poi_names.append(line)
print "toal number of poi", len(poi_names)

print "total value of stock belongs to  James Prentice", enron_data['PRENTICE JAMES']['total_stock_value']
print "How many email messages do we have from Wesley Colwell to persons of interest?", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "What's the value of stock options exercised by Jeffrey K Skilling?", enron_data['SKILLING JEFFREY K']['exercised_stock_options']


print "lay" , enron_data['LAY KENNETH L']['total_payments']
print "SKILLING JEFFREY K" , enron_data['SKILLING JEFFREY K']['total_payments']
print "andrew fastow" , enron_data['FASTOW ANDREW S']['total_payments']


number_of_person_with_salary = 0
numebr_of_known_emails = 0
number_of_people_with_total_payments_as_NaN = 0;
for person in enron_data:
	# print person
	if enron_data[person]['salary'] != 'NaN':
		number_of_person_with_salary += 1
	if enron_data[person]['email_address'] != 'NaN':
		numebr_of_known_emails += 1
	if enron_data[person]['total_payments'] == 'NaN':
		number_of_people_with_total_payments_as_NaN += 1


print "How many folks in this dataset have a quantified salary? What about a known email address?",number_of_person_with_salary, numebr_of_known_emails

print 'number_of_people_with_total_payments_as_NaN', number_of_people_with_total_payments_as_NaN
print ' percentage of _of_people_with_total_payments_as_NaN', ((1.0*number_of_people_with_total_payments_as_NaN)/len(enron_data))*100

fullname_poi = []
for line in poi_names:
	x = line.split(" ")
	#print x; 
	lastname_length = len(x[1])
	lastname = x[1][:lastname_length-1].upper()
	firstname_length = len(x[2])
	#print firstname_length
	firstname = x[2][:firstname_length-3].upper()
	fullname = str(lastname+ ' ' + firstname)
	fullname_poi.append(fullname)
	#print fullname
poi_with_payment_nan = 0
print ""
for person in enron_data:
	#print person

	for line in poi_names:
		x = line.split(" ")
		#print x; 
		lastname_length = len(x[1])
		lastname = x[1][:lastname_length-1].upper()
		firstname_length = len(x[2])
		#print firstname_length
		firstname = x[2][:firstname_length-1].upper()
		fullname = str(lastname+ ' ' + firstname)
		person = str(person)
		# if person == 'LAY KENNETH L':
		# 	print person , fullname, person.find(fullname)
		if person.find(fullname) != -1 :
			print fullname, "eron_name", person, enron_data[person]['total_payments']
			if enron_data[person]['total_payments'] == 'NaN':
				poi_with_payment_nan += 1

print poi_with_payment_nan