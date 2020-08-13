'''
Recursive:
A program is called recursive when an entity calls itself. A program is call iterative when there is a loop (or repetition).
'''
# TO-DO: Implement a recursive implementation of binary search
'''
Binary Search:
This search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison.
    1. Compare x with the middle element.
    2. If x matches with the middle element, we return the mid index.
    3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
    4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
'''
def binary_search(arr, target, start, end):
    if start > end: # if  the start value is greater than the end value
        return -1 # return -1
    mid = (start + end) // 2 # set a mid point to the start value plus the end vlaue
    if target == arr[mid]: # if the target is equal to the arr mid index value
        return mid # return the mid value

    elif target < arr[mid]: # else if the target is less than the arr mid index value
        return binary_search(arr, target, start, mid - 1)  # reduce highest by 1

    else: # else
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
