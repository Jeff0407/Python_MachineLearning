"""
File: titanic_github.py
Name: Jeff
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle. Hyperparameters are hidden by the library!
This abstraction makes it easy to use but less flexible.
"""

import pandas as pd
from sklearn import ensemble
from sklearn.preprocessing import LabelEncoder

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'
nan_cache = {}


def data_preprocess(filename, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be read into pandas
	:param mode: str, indicating the mode we are using (either Train or Test)
	:param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
	:return: Tuple(data, labels), if the mode is 'Train' data, if the mode is 'Test'
	"""
	data = pd.read_csv(filename)
	labels = None

	data.loc[data.Sex == 'male', 'Sex'] = 1
	data.loc[data.Sex == 'female', 'Sex'] = 0

	# Changing 'S' to 0, 'C' to 1, 'Q' to 2
	data.loc[data.Embarked == 'S', 'Embarked'] = 0
	data.loc[data.Embarked == 'C', 'Embarked'] = 1
	data.loc[data.Embarked == 'Q', 'Embarked'] = 2

	if mode == 'Train':

		# Drop Name, Cabin, PassengerId, Ticket
		data.pop('Name')
		data.pop('Cabin')
		data.pop('PassengerId')
		data.pop('Ticket')

		# Record the mean of Age and Fare
		age_mean = round(data.Age.mean(), 3)
		fare_mean = round(data.Fare.mean(), 3)

		data = data.dropna()

		# Record true Labels
		labels = data['Survived']
		data.pop('Survived')

		# Create New Feature FareBin_Code_5
		data['FareBin_5'] = pd.qcut(data['Fare'], 5)
		label = LabelEncoder()
		data['FareBin_Code_5'] = label.fit_transform(data['FareBin_5'])
		df_5 = pd.crosstab(data['FareBin_Code_5'], data['Pclass'])
		data.pop('Fare')
		data.pop('FareBin_5')

		nan_cache['Age'] = age_mean
		nan_cache['Fare'] = fare_mean

		return (data, labels)

	elif mode == 'Test':
		# Create New Feature FareBin_Code_5
		data['FareBin_5'] = pd.qcut(data['Fare'], 5)
		label = LabelEncoder()
		data['FareBin_Code_5'] = label.fit_transform(data['FareBin_5'])
		df_5 = pd.crosstab(data['FareBin_Code_5'], data['Pclass'])
		data.pop('Fare')
		data.pop('FareBin_5')

		# Fill in the Nan data in age with the mean of Age in the training data
		data.Age = data['Age'].fillna(nan_cache['Age'])

		# Drop Name, Cabin, PassengerId, Ticket
		data.pop('Name')
		data.pop('Ticket')
		data.pop('Cabin')
		data.pop('PassengerId')

		return data


def one_hot_encoding(data, feature):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: DataFrame, remove the feature column and add its one-hot encoding features
	"""
	if feature == 'Sex':
		# One hot encoding for a new category Male
		data['Sex_1'] = 0
		data.loc[data.Sex == 1, 'Sex_1'] = 1
		# One hot encoding for a new category Female
		data['Sex_0'] = 0
		data.loc[data.Sex == 0, 'Sex_0'] = 1

		# No need Sex anymore!
		data.pop('Sex')

	elif feature == 'Pclass':
		# One hot encoding for a new category FirstClass
		data['Pclass_0'] = 0
		data.loc[data.Pclass == 1, 'Pclass_0'] = 1
		# One hot encoding for a new category SecondClass
		data['Pclass_1'] = 0
		data.loc[data.Pclass == 2, 'Pclass_1'] = 1
		# One hot encoding for a new category ThirdClass
		data['Pclass_2'] = 0
		data.loc[data.Pclass == 3, 'Pclass_2'] = 1
		# No need Pclass anymore!
		data.pop('Pclass')

	elif feature == 'Embarked':
		data['Embarked_0'] = 0
		data.loc[data.Embarked == 0, 'Embarked_0'] = 1
		data['Embarked_1'] = 0
		data.loc[data.Embarked == 1, 'Embarked_1'] = 1
		data['Embarked_2'] = 0
		data.loc[data.Embarked == 2, 'Embarked_2'] = 1
		# No need Embarked anymore!
		data.pop('Embarked')

	return data


def out_file(predictions, filename):
	"""
	This function can outfile the result into csv format and be submitted to Kaggle
	@param predictions: the result we predict from test data with our model
	@param filename: str, the filename you create
	"""
	with open(filename, 'w') as out:
		out.write('PassengerId,Survived\n')
		for i in range(len(predictions)):
			out.write(str(892+i)+','+str(predictions[i])+'\n')


def main():
	"""
	Call data_preprocess(), one_hot_encoding(), and
	standardization() on training data.
	"""
	train_data, y_train = data_preprocess(TRAIN_FILE, mode='Train')
	test_data = data_preprocess(TEST_FILE, mode='Test')

	train_data = one_hot_encoding(train_data, 'Sex')
	train_data = one_hot_encoding(train_data, 'Pclass')
	train_data = one_hot_encoding(train_data, 'Embarked')
	test_data = one_hot_encoding(test_data, 'Sex')
	test_data = one_hot_encoding(test_data, 'Pclass')
	test_data = one_hot_encoding(test_data, 'Embarked')

	x_train = train_data
	x_test = test_data

	# Use Random Forest as our model
	forest = ensemble.RandomForestClassifier(max_depth=9, min_samples_leaf=11)
	forest.fit(x_train, y_train)
	predictions = forest.predict(x_test)
	print(forest.score(x_train, y_train))
	out_file(predictions, 'titanic_github_submission.csv')


if __name__ == '__main__':
	main()
