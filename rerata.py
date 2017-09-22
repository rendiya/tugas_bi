import math
from collections import Counter

def mean(x):
    return sum(x)/len(x)

def median(x):
    # Input: list of numbers; Output: the "middle" number of an ordered list of #s
    
    sorted_x = sorted(x)
    length_n = len(x)
    
    middle = length_n // 2 # Integer division
    
    # Even numbered amount in list:
    if length_n % 2 == 0:
        median_even = (sorted_x[middle - 1] + sorted_x[middle]) / 2
        return(median_even) # Remember index 0 as 1st element.
    else:
        return(sorted_x[middle]) # Return middle number


def mode(x):
    return (Counter(x).most_common(1))

def variance(x):
    n = len(x)
    x_bar = mean(x)
    return(round(sum((x_i - x_bar)**2 for x_i in x) / (n - 1), 2))

def standard_deviation(x):
    return(math.sqrt(variance(x)))

def range(x):
    x = sorted(x)
    return(x[-1]-x[0])

def quartile_1(l):
    return sorted(l)[int(len(l) * .25)]
    
def quartile_3(l):
    return sorted(l)[int(len(l) * .75)]