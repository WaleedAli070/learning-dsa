def mergeSort(arr):
    # Merge Sorting Algorithm
    
    # A merge sort algorithm is a sorting algorithm that sorts a collection
    # by breaking it into half (recursively, until the half comprises exactly 1 element). 
    # It then sorts those two halves, and then merges them together, 
    # in order to form one, completely sorted collection.
    
    # O(nlog(n)) Worst case Time Complexity. Combination of linear (n) and logrithmic (log(n)).
    # often referred to as "linearithmic" time.
    # O(n) Space Complexity, (out-of-place). requires extra space, as the array size grows (major drawback).
    
    arrayLength = len(arr)
    # In case array length is already reduced to a single element, return
    if arrayLength == 1:
        return
    
    # Compute a midpoint to split the array into 2 halves (left and right)
    midPoint = arrayLength // 2
    leftHalf = arr[0:midPoint]
    rightHalf = arr[midPoint:]
    
    # Recursively call the same function on both the splitted halves to further split them
    mergeSort(leftHalf)
    mergeSort(rightHalf)
    
    print('Left half', leftHalf)
    print('Right half', rightHalf)
    
    # Once, the splitting is done, start merging the two halves, 
    # after sorting those, in a separate function
    merge(leftHalf, rightHalf, arr)
    
    # return the merged, sorted array
    return arr

def merge(leftArray, rightArray, arr):
    # initialize index at 0, later to be incremented
    index = 0
    print('Raw Arr', arr)
    # Given the two arrays, iterate until either of those is exhausted
    while (len(leftArray) > 0 and len(rightArray) > 0):
        # compare first element of both the halves and add the smaller number
        # to the separate array, while removing that element from the respective array (popping-out)
        if (leftArray[0] > rightArray[0]):
            arr[index] = rightArray.pop(0)
        else:
            arr[index] = leftArray.pop(0)
        index += 1
    # check and add remaining elements of either half to the separate array
    while (len(leftArray) > 0):
        arr[index] = leftArray.pop(0)
        index += 1 
        
    while (len(rightArray) > 0):
        arr[index] = rightArray.pop(0)
        index += 1 
    
    print('Sorted Array', arr)
        
mergeSort([4, 3, 3, 1, 5, -2, 1, 6, -3, 1, 0, 2, 10, 12, 6, 7])