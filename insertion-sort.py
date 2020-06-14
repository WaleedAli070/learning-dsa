def insertionSort(arr):
    # Insertion Sorting Algorithm
    
    # An insertion sort algorithm maintains a sublist of the collection
    # as the sorted-list and iterates through the rest of unsorted list,
    # inserting each element, one by one, at its correct order in the sorted-list.
    
    # O(n²) Worst case Time Complexity (Nested For loops), O(n) Best case Time Complexity
    # O(n) Space Complexity, (in-place).
    
    # Iterate to the length of the list
    # We will have two sub-lists, sorted and unsorted
    # at each outer iteration, our sorted list will grow and 
    # unsorted list will shrink by 1 element
    for i, ithElement in enumerate(arr):
        # Initialize j to be i, 
        j = i
        # start from the end of sorted list (ith index)
        # and compare the elements of sorted-sublist until we  
        # reach the location where the element is to be inserted,  
        # while decrementing j by 1 at each internal iteration
        while (j > 0 and arr[j - 1] > ithElement):
            print('Compairing ', arr[j], arr[j - 1])
            # keep shifting unordered elements to the right
            arr[j] = arr[j - 1]
            j -= 1
        # insert the current element to the location it needs to be
        arr[j] = ithElement
        # Extra logging statements for understanding purposes
        print('After ' + str(i+1) + ' Iteration(s):')
        print(arr)
    return arr

insertionSort([4, 3, 1, 5, -2, 6, -3, 1, 0, 2, 10, 12, 6, 7])