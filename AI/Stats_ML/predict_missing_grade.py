# Predict Missing Grade
import json
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from random import randint

# Algorithm:
	#1. Create separate linear models for each of the following highly possible combinations
	#2. for each test case, figure out which combination, does it belong to and then use  that model to predict the Grade

class Model:
	def __init__(self, feature_vector, target_value_vector):
		self.feature_vector = feature_vector
		self.target_value_vector = target_value_vector

	def add_feature_target_value(self, feature, target_value):
		self.feature_vector.append(feature)
		self.target_value_vector.append(target_value)

	def get_feature_vector(self):
		return self.feature_vector

	def get_target_value_vector(self):
		return self.target_value_vector

	def generate_regression_model(self):
		degree = 3
		regression_model = make_pipeline(PolynomialFeatures(degree), Ridge())
		regression_model.fit(self.feature_vector, self.target_value_vector)
		self.regression_model = regression_model

	def predict(self, test_feature):
		predicted_value_vector = self.regression_model.predict(test_feature)
		return predicted_value_vector[0]

def get_model(training_data, hash_key):
	if not hash_key in training_data:
		training_data[hash_key] = Model([],[])

	return training_data[hash_key]

def generate_feature(subject_scores):
	del subject_scores['serial']
	feature = []

	for key in sorted(subject_scores.keys()):
		feature.append(subject_scores[key])

	return feature

def generate_feature_target_value(subject_scores):
	target_value = subject_scores['Mathematics']
	del subject_scores['Mathematics']

	feature = generate_feature(subject_scores)
	return feature, target_value


def generate_hash(key_list):
	if 'serial' in key_list:
		key_list.remove('serial')
	
	if 'Mathematics' in key_list:
		key_list.remove('Mathematics')
	
	key_list.sort()
	hash_key = '-'.join(key_list)
	return hash_key

def add_training_data(subject_scores, training_data):
	hash_key = generate_hash(subject_scores.keys())
	training_model = get_model(training_data, hash_key)

	feature, target_value = generate_feature_target_value(subject_scores)
	training_model.add_feature_target_value(feature, target_value)

def read_training_data():
	training_data = {}
	with open('training.json', "r") as f:
		n = int(f.readline())

		for line in f.readlines():
			subject_scores = json.loads(line)
			add_training_data(subject_scores, training_data)

	return training_data

def generate_regression_models(model_training):
	for hash_key in model_training.keys():
		model = model_training[hash_key]
		model.generate_regression_model()

def read_and_predict_test_data(model_training):
	n = int(raw_input())
	for _ in range(0,n):
		feature_vector = []

		subject_scores = json.loads(raw_input())
		hash_key = generate_hash(subject_scores.keys())
		feature = generate_feature(subject_scores)
		feature_vector.append(feature)

		if hash_key in model_training:
			model = model_training[hash_key]
			mathematics_grade = model.predict(feature_vector)
		else:
			mathematics_grade = randint(1,8)

		print int(round(mathematics_grade))

if __name__ == "__main__":
	model_training = read_training_data()
	generate_regression_models(model_training)

	read_and_predict_test_data(model_training)