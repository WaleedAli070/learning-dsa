def selectionSort(arr):
    # Selection Sorting Algorithm
    
    # A selection sort algorithm sorts through a list of items by iterating
    # through a list of elements, finding the smallest one, and swapping it 
    # for the place of unsorted item (at the front of the sorted section).
    
    # O(n²) Time Complexity (Nested For loops), 
    # O(1) Space complexity (in-place), (no extra space required)
    for i, _ in enumerate(arr):
        # Initialy, keep the value of i to be the smallest value's index
        smallestIndex = i
        # Iterate the remaining list (from i+1 to the end)
        for j in range(i + 1, len(arr)):
            print('Compairing ', arr[smallestIndex], arr[j])
            # Compare the jth Element with the smallest value's index
            # In case it's smaller (for ascending sort), 
            # update the index value for the smallest element
            if (arr[j] < arr[smallestIndex]):
                smallestIndex = j
        # In case the smallest value's index is not the same as that of i
        # swap the ith element with the smallest element found.
        if not smallestIndex == i:
            temp = arr[i]
            arr[i] = arr[smallestIndex]
            arr[smallestIndex] = temp
        # Extra logging statements for understanding purposes
        print('After ' + str(i+1) + ' Iteration(s):')
        print(arr)
    return arr

selectionSort([4, 3, 1, 5, 2, 6, 3, 1, 0, 2, 10, 12, 6, 7])