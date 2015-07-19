# Best Aptitude Test
# Algorithm: Compute the correlation of each test with the GPA. The test is with
# highest correlation is the best aptitude test

from __future__ import division
import math
import basic_statistics_warmup as statslib

def get_highest_value_index(x):
	m = max(x)
	for index, value in enumerate(x):
		if x[index] == m:
			return index

def compute_dot(x, y):
	return sum(x_i * y_i for x_i, y_i in zip(x, y))

def compute_covariance(x, y):
	n = len(x)
	x_bar = sum(x) / n
	y_bar = sum(y) / n
	de_mean_x = [x_i - x_bar for x_i in x]
	de_mean_y = [y_i - y_bar for y_i in y]

	return compute_dot(de_mean_x, de_mean_y) / (n - 1)

def compute_correlation(x, y):
	stdev_x = statslib.compute_standard_deviation(len(x), x)
	stdev_y = statslib.compute_standard_deviation(len(y), y)

	if stdev_x > 0 and stdev_y > 0:
		covariance = compute_covariance(x, y)
		return covariance / stdev_x / stdev_y
	else:
		return 0

def get_best_test(input_data):
	correlations = []
	for i in range(5):
		correlation = compute_correlation(input_data[0], input_data[i+1])
		correlations.append(correlation)
	highest_index = get_highest_value_index(correlations)
	return highest_index + 1 # index 0 corresponds to test1 and so on..

def read_input_data():
	input_data = []
	# input_data[0] is GPAs, input_data[1] is test1 scores and so on...
	n = int(raw_input())
	for i in range(6):
		grades = [float(data) for data in raw_input().split()]
		input_data.append(grades)
	return input_data;

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		input_data = read_input_data()
		output = get_best_test(input_data)
		print output
