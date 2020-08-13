'''
Merge Sort:
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two
halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r)
is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
'''

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    a, b = len(arrA), len(arrB) # set a to length of arrA, set b to length of arrB
    elements = a + b # set elemnts to a + b
    merged_arr = [0] * elements # set merged_arr to 0 x elements

    for i in range(len(merged_arr)): # for i in the range of the length of merged_arr
        a, b = len(arrA), len(arrB) # set a to length of arrA, set b to length of arrB

        if a == 0 or b == 0: # if either a or b is empty
            for item in arrA: # for item in the arrA
                merged_arr[i] = item # add the item to the merged_arr
                i += 1 # add 1

            for item in arrB: # for item in the arrA
                merged_arr[i] = item # add the item to the merged_arr
                i += 1 # add 1

            return merged_arr

        x, y = arrA[0], arrB[0] # set x to the initial value of arrA, set y to the initial value of arrB
        if x < y: # if x is smaller than y
            merged_arr[i] = x # add the item to the merged_arr
            arrA.remove(x) # remove the value from the arrA

        else: # if y is smaller than y
            merged_arr[i] = y # add the item to the merged_arr
            arrB.remove(y) # remove the value from the arrB

    return merged_arr
'''
### class walkthrough ###
def merge_sort(arr):
    if len(arr) == 0:
        return None

    # Base
    # if len(arr) > 1:
    if len(arr) == 1:
        return arr

    # Recursive
    else:
        # divide 'arr' into a LHS, RHS
        merge_sort(LHS)
        merge_sort(RHS)
        arr = merge(LHS, RHS)

    return arr

    # pre-req - a, b are SORTED lists
    def merge_helper(a, b):
        sorted = []
            ai = 0
            bi = 0
            count = len(a) +len(b)

            while len(sorted) < count:
                if ai >= len(a):
                    sorted.append(b[bi])
                    bi += 1
                elif  bi >= len(b):
                    sorted.append(a[ai])
                    ai += 1
                elif a[ai] < b[bi]:
                    sorted.append(a[ai])
                    ai += 1
                elif a[ai] >= b[bi]:
                    sorted.append(b[bi])
                    bi += 1

        return sorted
'''
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr): # function to merge sorted arrays
    if len(arr) <= 1: # if leng of ar is <= 1

        return arr

    arrA = arr[:(len(arr) // 2)] # set arrA to back half the length of the arr
    arrB = arr[(len(arr) // 2):] # set arrB to front half the length of the arr

    return merge(merge_sort(arrA), merge_sort(arrB)) # use merge function to merge the two sorted arrays

def merge_in_place(arr, start, mid, end): # function to in-place merge sort
    while start < mid and mid < end + 1:  # while start < mid value, and mid value is less than end value + 1
        if arr[start] < arr[mid]: # if the arr[start] value is less than arr[mid] value
            start += 1 # move the start 1
        else:
            for i in range(start, mid): # fir each item in the range of the front half
                arr[i], arr[mid] = arr[mid], arr[i] # swap arr[i] and arr[mid]
            start += 1 # move the start 1
            mid += 1 # move the mid 1

    return arr

def merge_sort_in_place(arr, l, r): # function to merge arrays and sort in place
    if r - l <= 0: # if both are at the end, we're done!
        return arr

    mid = l + ((r - l) // 2) # set the mid point

    merge_sort_in_place(arr, l, mid) # use the merge_sort_in_place on the left half
    merge_sort_in_place(arr, mid + 1, r) # use the merge_sort_in_place on the right half
    merge_in_place(arr, l, mid + 1, r) # use the merge_in_place on the left half

    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
