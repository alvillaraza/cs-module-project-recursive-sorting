# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    '''
    takes in two sorted arrays, combines them into one sorted array and returns it
    '''

    #what are the inputs?  
        #they need to be sorted arrays
    #what are the outputs
        #outputs a combined sorted array
    #what does it do?
        #maintains the sorting quality of the arrays
    totalLen = len(arrA) + len(arrB)
    merged_arr = [None] * totalLen
    pointerA = pointerB = 0
    #what happens if either array is 0 long?
    #what happens if arrA only has larger values than arrB?
    #what happens if arrA and arrB have the same exact values?
    #what happens if one array is empty or one array is longer than the other array

    for index in range(0, totalLen):
        #place the appropriate element from arrA or arrB
        #appropriate element is the smallest element out of the 2 arrays
        if pointerA >= len(arrA):
            merged_arr[index] = arrB[pointerB]
            pointerB += 1
        elif pointerB >= len(arrB):
            merged_arr[index] = arrB[pointerB]
            pointerA += 1
        elif arrA[pointerA] < arrB[pointerB]:
            merged_arr[index] = arrA[pointerA]
            pointerA += 1
        else:  #arrB[pointerB] > element in arrA
            merged_arr[index] = arrB[pointerB]
            pointerB += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # split the array
    #if there is only 1 element in the array, you can't split it
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    return merge(merge_sort(left), merge_sort(right))
    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here


