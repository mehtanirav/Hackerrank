# Laptop battery life

from scipy import stats
from matplotlib import pyplot as plt

def read_training_data(filename):
	charge_time = []
	use_time = []
	with open(filename, 'r') as f:
		for line in f:
			data = line.split(',')
			charge_time.append(float(data[0]))
			use_time.append(float(data[1]))
	return charge_time, use_time

def plot_training_data(x,y):
    plt.scatter(charge_time, use_time)
    plt.xlabel("Charge Time")
    plt.ylabel("Battery Lasts")
    plt.show()

def filter_training_data(x,y):
	filter_x = []
	filter_y = []
	
	for x_i, y_i in zip(x, y):
		if x_i < 4:
			filter_x.append(x_i)
			filter_y.append(y_i)

	return filter_x, filter_y

if __name__ == "__main__":
	charge_time, use_time = read_training_data('trainingdata.txt')
	
	#plot_training_data(charge_time, use_time)

	# From the scatter plot, we see that there is a linear relation between charge_time and
	# use_time, till charge_time is < 4. After that use_time is constant at 8
	filtered_charge_time, filtered_use_time = filter_training_data(charge_time, use_time)

	slope, intercept, r_value, p_value, std_error = stats.linregress(filtered_charge_time, filtered_use_time)

	# Use the generate slope and intercept to predict the use_time given the charge_time
	input_charge_time = float(raw_input())

	if input_charge_time < 4:
		predicted_use_time = slope*input_charge_time + intercept
	else:
		predicted_use_time = 8

	print "%.2f" % predicted_use_time



