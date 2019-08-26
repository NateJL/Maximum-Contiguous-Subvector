#!/usr/bin/env python3

"""
Created on Mon Oct 22 18:05:57 2018

@author: Nathan Larson
"""

import timeit
import max_subarray
import sys
import random
	
if __name__ == '__main__':
	# creates an array of rational numbers the size of sys.argv[2]
	# array = [random.uniform(-100,100) for _ in range(int(sys.argv[2]))]
	
	# a simple test array, ignores second command line argument
	# array = [0,-1,4,-8,5,6,0,-1]
	
	# an array of all zeros takes less time to create
	array = [0] * int(sys.argv[2])
    
    # an array of random values for testing
	# array = [random.randint(-32, 32) for _ in range(int(sys.argv[2]))]


	print('That took',
		timeit.timeit(lambda:
			print('The maximum subarray sum is:',
				getattr(max_subarray, sys.argv[1])(array)),
		number = 1),
		'seconds')