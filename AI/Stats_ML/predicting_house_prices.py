# Predicting house prices
from sklearn import linear_model

def read_training_data():
	first_line = raw_input().split()
	total_features = int(first_line[0])
	n = int(first_line[1])

	price = []
	features = []
	feature_vec = []

	for _ in range(0,n):
		line = raw_input().split()
		feature_vec = [float(num) for num in line]
		del feature_vec[-1]

		features.append(feature_vec)
		price.append(float(line[-1]))

	return price, features

def read_test_data():
	n = int(raw_input())
	features = []
	for _ in range(0,n):
		feature = [float(num) for num in raw_input().split()]
		features.append(feature)

	return n, features

if __name__ == "__main__":

	price_per_unit, training_features = read_training_data()

	n, test_features = read_test_data()

	regression_object = linear_model.LinearRegression()
	regression_object.fit(training_features, price_per_unit)

	predicted_prices = regression_object.predict(test_features)
	for price in predicted_prices:
		print "%.2f" % price



