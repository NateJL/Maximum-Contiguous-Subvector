# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:05:57 2018

@author: Nathan Larson
"""

#
# BubbleSort function
#
def bubbleSort(array):
    comparisons = 0     # comparison counter
    exchanges = 0       # exchanges counter
    print(array)
    for i in range(len(array)-1, 0, -1):                        # start outer loop with the last element in array 
        
        for j in range(len(array)-1, len(array)-i-1, -1):       # inner loop from last element down to len(array)-i
            comparisons += 1                                    # increment number of comparisons
            
            if array[j-1] > array[j]:                           # if element [j-1] is larger than element [j]
                exchanges += 1                                  # increment number of exchanges
                array[j], array[j-1] = array[j-1], array[j]     # switch element [j-1] and element [j]
                
        print(array, " | Pass: ", len(array)-i, "\t| Comparisons: ", comparisons, "\t| Exchanges: ", exchanges)
    return array


#
# QuickSort function
#
def quickSort(array):
    smaller = []
    equal = []
    larger = []
    
    if(len(array)<=1):
        return array
    
    pivot = array[0]
    for i in range(len(array)):
        if array[i] < pivot:
            smaller.append(array[i])
        elif array[i] == pivot:
            equal.append(array[i])
        else:
            larger.append(array[i])
    
    return quickSort(smaller)+equal+quickSort(larger)



if(__name__=="__main__"):
    print("Sorting Algorithms.")
    print(bubbleSort([6,1,7,11,4,10,2,5,9,3,8]))
    #print(quickSort([6,1,7,11,4,10,2,5,9,3,8]))