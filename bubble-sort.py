def bubbleSort(arr):
    # Bubble Sorting Algorithm
    
    # A bubble sort algorithm iterates through the list or array that it is given, 
    # and compares each pair of adjacent elements in the list by size. 
    # If the elements are in the incorrect order, it swaps them, 
    # It continues to swap out of order elements until the entire list is sorted.
    
    # O(n²) Time Complexity (Nested For loops), 
    # O(1) Space complexity (in-place), (no extra space required)
    
    # Iterate to the end of the list
    for i, _ in enumerate(arr):
        # Flag to check if any swapping is done in the current iteration
        swapped = False
        # Iterating from start of the list to the length - value of i (minor optimization)
        # reason being, in each outer iteration, maximum number is already "bubbled-up"
        # to the end of the list, so we don't need to compare with that.
        for j in range(0, len(arr) - i - 1):
            print('Compairing ', arr[j], arr[j+1])
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                # in case any swapping is done in the current iteration, we will set the flag to True
                swapped = True
        # at the end of inner iteration, we will check if our flag is still False,
        # in case it is, that means no swapping is done and the list is already sorted.
        # therefore break out of the iterations
        if not swapped:
            break
        # Extra logging statements for understanding purposes
        print('After ' + str(i+1) + ' Iteration(s):')
        print(arr)
    return arr

bubbleSort([4, 3, 1, 5, -2, 6, -3, 1, 0, 2, 10, 12, 6, 7])