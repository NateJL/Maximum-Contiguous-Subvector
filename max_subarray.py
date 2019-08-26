# -*- coding: utf-8 -*-
"""
CSC 440 Programming Assignment #1
Due: November 1st, 2018
This program contains 5 different searching algorithms to find the maximum contiguous subvector
given an array of arbitrary length.
The search algorithms included are:
        -Linear algorithm               [X]
        -Cubic  algorithm               [X]
        -Quadratic algorithm (x2)       [X][X]
        -Divide & Conquer algorithm     [X]
        
@author: Nathan Larson
"""
import random



#=============================================================================================
# This algorithm takes a linear approach to the maximum contiguous subvector problem
# with a time complexity of O(n).
# @param array to search
# @return maximum contiguous subvector sum 
def linear_algorithm(array):
    current_max = array[0]          # initialize both the current_max and 
    max_so_far = array[0]           # max_so_far values to zero
    
    for i in range(1, len(array)):  # loop through the entire array element by element
        
                                                            # set the current max value to larger of:
        current_max = max(array[i], current_max + array[i]) # -current array element
                                                            # -current max subvector + array element
        
        # set the overall max value to either the current max value if it is larger than max so far,
        # or stay the same value if it remains the largest so far.
        
                                                  # set the current max subvector so far to larger of:
        max_so_far = max(max_so_far, current_max) #     - current max subvector (stay the same)
	                                              #     - new current max subvector
    
    return max_so_far               # Return the max subvector remaining after the full loop



#=============================================================================================
# This Cubic algorithm calculates the maximum contiguous subvector of an array by generating
# all pairs with start index i and end index j and calculating each sum in between.
# @param array to search
# @return maximum contiguous subvector sum
def cubic_algorithm(array):
    current_max = array[0]          # initialize the current max sum first element
    
    for i in range(0, len(array)):      # outer loop to handle the start index
        for j in range(i, len(array)):  # inner loop to handle the end index
            temp_sum = 0
            for k in range(i, j+1):     # inner-inner loop to run through the 
                temp_sum += array[k]
            if(temp_sum > current_max):
                current_max = temp_sum
        
    
    return current_max



#=============================================================================================
# This Quadratic algorithm calculates the maximum contiguous subvector of an array by looping
# through the array and calculating each sum starting from all indices.
# @param array to search
# @return maximum contiguous subvector sum
def quadratic_algorithm1(array):
    current_max = array[0]
    
    for i in range(0, len(array)):          # outer loop to handle the start index
        temp_sum = 0
        for j in range(i, len(array)):      # inner loop to handle the end index
            temp_sum += array[j]
            if(temp_sum > current_max):
                current_max = temp_sum
    
    return current_max



#=============================================================================================
# The seconds quadratic algorithm first calculates the cumulative sums of the input array
# then uses those values to calculate the max contiguous subvector.
# @param array to search
# @return maximum contiguous subvector sum
def quadratic_algorithm2(array):
    current_max = 0
    array_sum = [0] * (len(array)+1)    
    array_sum[0] = 0     
                
    for i in range(1, len(array_sum)):                  # initial loop to sum array[0...i]
        array_sum[i] = (array_sum[i-1] + array[i-1])
        
    for i in range(1, len(array_sum)):                      # main loop to compute subvector sum
        for j in range(i, len(array_sum)):
            current_sum = array_sum[j] - array_sum[i-1]
            if(current_sum > current_max):
                current_max = current_sum
                
    return current_max



#==========================================================================================================
# This Divide & Conquer algorithm uses recursion to search the array for the max contiguous subvector
# @param array to search
# @return maximum contiguous subvector sum
def div_and_con_algorithm(array):
    max_sum = maxSubVectorSum(array, 0, len(array)-1)
    return max_sum

# This function is used as the main recursive call function for the divide & conquer algorithm
# @param array: array of int to find max contiguous subvector
#          low: index of end of lower max sum
#         high: index of beginning of upper max sum
def maxSubVectorSum(array, low, high):
    
    if(low == high):                # Base case to end recursive calls
        return array[low]
    
    mid = (low + high) // 2         # calculate the mid-point
    
                                                                # Return max of:
    return max(maxSubVectorSum(array, low, mid),                # Max sum in lower half
               maxSubVectorSum(array, mid+1, high),             # Max sum in upper half
               maxSubVectorSumWithMid(array, low, mid, high))   # Max sum crosses midpoint

# This function is used to compute the maximum possible sum in the given array
# that contains the array element at the specified index
def maxSubVectorSumWithMid(array, low, mid, high):
    
    temp_sum = 0                # initialize temporary sum variable
    lower_sum = 0               # lower sum to zero
    upper_sum = 0               # upper sum to zero
    
    for i in range(mid, low-1, -1):             # loop through all elements in the lower subvector
        temp_sum = temp_sum + array[i]          # Sum elements in the lower subvector
        if(temp_sum > lower_sum):               # if the new sum is larger than the current max sum
            lower_sum = temp_sum                # then assign the new max sum to lower_sum
            
    temp_sum = 0
    for i in range(mid+1, high+1):              # loop through all elements in the upper subvector
        temp_sum = temp_sum + array[i]          # Sum elements in the upper subvector
        if(temp_sum > upper_sum):               # if the new sum is larger than the current max sum
            upper_sum = temp_sum                # then assign the new max sum to upper_sum
            
    # Return the sum from lower and upper sides of mid-point
    return lower_sum + upper_sum



#=========================
def myMax2(num1, num2):
    if(num1 > num2):
        return num1
    else:
        return num2
    
def myMax3(num1, num2, num3):
    temp_max = num1
    if(num2 > temp_max):
        temp_max = num2
    if(num3 > temp_max):
        temp_max = num3
        if(num2 > num3):
            temp_max = num2
    return temp_max
#=========================



#=============================================================================================
# Function to run 100 tests consecutively, comparing results and breaking if any of the results are not the same
def runTestLoop():
    print("Running tests.")
    num_of_tests = 100
    for i in range(0, num_of_tests):
        array = [random.randint(-32, 32) for _ in range(10)]
        linear_max = linear_algorithm(array)
        conquer_max = div_and_con_algorithm(array)
        cubic_max = cubic_algorithm(array)
        quad1_max = quadratic_algorithm1(array)
        quad2_max = quadratic_algorithm2(array)
        
        if(linear_max == conquer_max == cubic_max == quad1_max == quad2_max):
            print("Test(", i, "/", num_of_tests, "): Passed")
        else:
            print("Test(", i, "/", num_of_tests, "): Failed")
            print("Linear:\t", linear_max)
            print("D & C:\t", conquer_max)
            print("Cubic:\t", cubic_max)
            print("Quad1:\t", quad1_max)
            print("Quad2:\t", quad2_max)
            
            break
        
def oneTest():
    array = [random.randint(-32, 32) for _ in range(10)]
    print("Linear:\t", linear_algorithm(array))
    print("D & C:\t", div_and_con_algorithm(array))
    print("Cubic:\t", cubic_algorithm(array))
    print("Quad1:\t", quadratic_algorithm1(array))
    print("Quad2:\t", quadratic_algorithm2(array))

if(__name__=="__main__"):
    print("Maximum Subvector Sum")
    runTestLoop()
    #oneTest();
    

