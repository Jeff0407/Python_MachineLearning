"""
File: boston_housing_competition.py
Name: Yu-Ju Fang
--------------------------------
This file demonstrates how to analyze boston
housing dataset.
"""

import pandas as pd
from sklearn import preprocessing, linear_model, model_selection, metrics, ensemble, svm
import matplotlib.pyplot as plt

TRAIN_FILE = 'boston_housing/train.csv'
TEST_FILE = 'boston_housing/test.csv'


def out_file(predictions, test_data, test_ID, filename):
	"""
	@param predictions: list, predictions of the housing price
	@param test_data:  test data from 'boston_housing/test.csv'
	@param test_ID: test ID for each case
	@param filename: string, output filename
	"""
	with open(filename, 'w') as out:
		out.write('ID,medv\n')
		for i in range(len(predictions)):
			out.write(str(test_ID[i])+','+str(predictions[i])+'\n')  # Write the ID number and prediction of each housing price for each test case


def main():
	"""
	First, we split the train data to train data and validation data and to train the model and check the performance
	of this model with . Then, we use the model we find to predict the housing price of the test data and then use the
	outfile function to output the result as a csv file.
	"""

	# Load data
	data = pd.read_csv(TRAIN_FILE)
	test_data = pd.read_csv(TEST_FILE)

	# Data preprocessing for train data
	Y = data['medv']  # Record correct answer of the train data
	X = data.drop(['medv'], axis=1)
	X.pop('ID')

	X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.3)  # Split train data to training data and validation data

	# Standardize the data
	standardizer = preprocessing.StandardScaler()
	x_train = standardizer.fit_transform(X_train)  # Standardize the train data
	x_test = standardizer.transform(X_test)   # Standardize the validation data

	# Polynomial Features
	poly_phi_extractor = preprocessing.PolynomialFeatures(degree=1)  # Use polynomial features
	x_train = poly_phi_extractor.fit_transform(x_train)  # Use polynomial features for train data
	x_test = poly_phi_extractor.transform(x_test)   # Use polynomial features for validation data

	# Import Linear Regression
	h = linear_model.LinearRegression()
	classfier = h.fit(x_train, y_train)

	# Predict result
	predictions = classfier.predict(x_test)
	print(metrics.mean_squared_error(predictions, y_test)**0.5)

	# -----------------------------------Predict housing price form test data-------------------------------------------

	# Data preprocessing for test data
	test_ID = test_data['ID']  # Record test ID of each case
	test_data.pop('ID')

	# Standardize the test data
	test_data = standardizer.transform(test_data)  # Standardize the test data
	test_data = poly_phi_extractor.transform(test_data)  # Use polynomial for the test data

	# Predict result
	predictions = classfier.predict(test_data)
	out_file(predictions, test_data, test_ID, 'boston_no_ID.csv')


if __name__ == '__main__':
	main()
