def quickSort(arr, left = None, right = None, count = 0):
    # Quick Sorting Algorithm
    
    # The quicksort algorithm uses a Divide&Conquer strategy, that sorts a collection 
    # by choosing a pivot point, and partitioning the collection around the pivot,
    # so that elements smaller than the pivot are before it, and elements larger than
    # the pivot are after it. It continues to choose a pivot point and break down the 
    # collection into single-element lists, before combing them back together to form one sorted list.
    
    # O(nlog(n)) Worst case Time Complexity. Combination of linear (n) and logrithmic (log(n)).
    # often referred to as "linearithmic" time.
    # O(log(n)) Space Complexity, (in-place). requires minimal extra space, as the array size grows
    # which is often ignored and the Alogrithm is considered "in-place".
    
    arrayLength = len(arr)
    
    # For simplicity, by default left and right variables are initialized with None, 
    # so that function can be called with a single argument (array itself). In that case, 
    # variables are then assigned their initial values (0 and last element, respectively) 
    if left == None:
        left = 0
    if right == None:
        right = arrayLength - 1
        
    if arrayLength > 1:
        # calling the partition method which will handle splitting of array into 2 halves
        # around the pivot, arranging smaller elements before and larger elements after it,
        # and then returning the boundary index for that subset of the array.
        index = partition(arr, left, right)

        print('Boundary Index', index)
        count += 1
        # until, the boundary index is less than the value of left and greater than the value of right,
        # (esentially meaning, the sub-array length is greater than 1), keep calling the function
        # recursively to perform splits of the array.
        if (left < index - 1):
            quickSort(arr, left, index - 1, count)
        if (index < right):
            quickSort(arr, index, right, count)
    
    print('Array: ', arr)
    return arr

def partition(arr, left, right):
    # Compute the pivot element of the array (keeping the pivot to be the middle element)
    pivot = arr[(left + right) // 2]
    print('Pivot:', pivot)
    
    # Iterate until the left pointer is less than the right pointer,
    # meaning, the two pointers don't cross each other.
    while (left <= right):
        # As we need to keep smaller elements before the pivot and larger elements after,
        # we will essentially find a larger element, currently residing before the pivot
        # and smaller element residing after the pivot to swap both the elements.
        # until that case is found, we will keep icrementing "left" and decrementing "right"
        while (arr[left] < pivot):
            left += 1
        while (arr[right] > pivot):
            right -= 1
        # as soon as both the loops are done, and left is still less than or equal to right,
        # meaning both the pointers have not crossed each other yet, we will swap the elements
        # present at both the pointers' location
        if (left <= right):
            # calling a separate function (for clean code purposes, nothing special here) 
            # to perform swap operation
            swap(arr, left, right)
            # as soon as swapping is done, again increment left pointer and decrement right
            left += 1
            right -= 1
    # return the value of left pointer, to be used as the boundary index
    # for performing the further split of the array (if required).
    return left

def swap(arr, leftIndex, rightIndex):
    print('Swapping: ', arr[leftIndex], arr[rightIndex])
    # Simple Swapping operations. btw, this also ensures that sorting is
    # mostly happening in-place, utilizing a minimal space for temp variable, most of the time.
    temp = arr[leftIndex]
    arr[leftIndex] = arr[rightIndex]
    arr[rightIndex] = temp

quickSort([4, 3, 3, 1, 5, -2, -1, 6, -3, 1, 0, 2, 10, 12, 6, 7])