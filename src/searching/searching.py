# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if start > end: # if  the start index > end index, return -1
        return -1
    mid = (start + end) // 2 # set a mid point
    if target == arr[mid]: # if the target is in the array, return mid target
        return mid

    elif target < arr[mid]: # if the target is less than the arr[mid] value
        return binary_search(arr, target, start, mid - 1)  # reduce highest by 1

    else:
        return binary_search(arr, target, mid + 1, end)  # increase highesty by 1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iterativelyq
def agnostic_binary_search(arr, target):
    # your code here
    pass
