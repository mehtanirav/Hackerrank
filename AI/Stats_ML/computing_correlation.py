# Computing the correlation

from __future__ import division
import basic_statistics_warmup as statslib

def read_input():
	n = int(raw_input())
	maths = []
	phy = []
	chem = []
	
	for _ in range(0,n):
		scores = raw_input().split()
		maths.append(int(scores[0]))
		phy.append(int(scores[1]))
		chem.append(int(scores[2]))

	return n, maths, phy, chem

def compute_dot_product(x, y):
	return sum(x_i * y_i for x_i, y_i in zip(x, y))

def compute_pearson_coefficient(x, x_mu, x_sigma, y, y_mu, y_sigma):
	dot_product = compute_dot_product(x,y)
	pearson_coefficient = (dot_product - n * x_mu * y_mu) / ((n-1) * (x_sigma * y_sigma))
	return pearson_coefficient

if __name__ == "__main__":

	n, maths, physics, chemistry = read_input()
	
	maths_mean = statslib.compute_mean(n, maths)
	maths_sd = statslib.compute_standard_deviation(n, maths)

	physics_mean = statslib.compute_mean(n, physics)
	physics_sd = statslib.compute_standard_deviation(n, physics)

	chemistry_mean = statslib.compute_mean(n, chemistry)
	chemistry_sd = statslib.compute_standard_deviation(n, chemistry)

	pearson_coefficient_maths_physics = compute_pearson_coefficient(maths, maths_mean, maths_sd, physics, physics_mean, physics_sd)
	print "%.2f" % pearson_coefficient_maths_physics

	pearson_coefficient_physics_chem = compute_pearson_coefficient(physics, physics_mean, physics_sd, chemistry, chemistry_mean, chemistry_sd)
	print "%.2f" % pearson_coefficient_physics_chem

	pearson_coefficient_chem_maths = compute_pearson_coefficient(chemistry, chemistry_mean, chemistry_sd, maths, maths_mean, maths_sd)
	print "%.2f" % pearson_coefficient_chem_maths


