#Hackerrank - Basic Statistics warmup

from __future__ import division
from collections import Counter
import sys
import math

def read_input():
    n = int(raw_input())
    data = [int(num) for num in raw_input().split()]
    return n, data

def average(x,y):
    return (x + y)/2

def compute_mean(n, data):
    mean = sum(data)/n
    return mean

def compute_median(n, data):
    sorted_data = sorted(data)
    if n%2 != 0:
        median = sorted_data[n // 2]
    else:
        median = average(sorted_data[n // 2], sorted_data[n // 2 - 1])
    return median

def compute_mode(n, data):
    counts = Counter(data)
    max_count = max(counts.values())
    mode = sys.maxint
    for num, count in counts.iteritems():
        if count == max_count and num < mode:
            mode = num
    return mode

def compute_standard_deviation(n, data):
    mean = compute_mean(n, data)
    deviations = [num - mean for num in data]
    sum_of_squares = sum(num*num for num in deviations)
    variance = sum_of_squares/n
    standard_deviation = math.sqrt(variance)
    return standard_deviation

def compute_confidence_interval(n, data):
    mean = compute_mean(n, data)
    standard_error = compute_standard_deviation(n, data)/math.sqrt(n)
    width = 1.96 * standard_error
    lower = mean - width
    upper = mean + width
    return lower, upper
    
if __name__=="__main__":
    n,data = read_input()

    mean = compute_mean(n, data)
    print "%.1f" % mean

    median = compute_median(n, data)
    print "%.1f" % median
    
    mode = compute_mode(n, data)
    print mode

    standard_deviation = compute_standard_deviation(n, data)
    print "%.1f" % standard_deviation

    lower, upper = compute_confidence_interval(n, data)
    print "%.1f %.1f" % (lower, upper)
