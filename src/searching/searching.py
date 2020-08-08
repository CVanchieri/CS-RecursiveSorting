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
# or iteratively
#def agnostic_binary_search(arr, target):
    # your code here

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

result = binary_search(arr1,1,1,len(arr1)-1) # find the result by iusing binary_search function on the length of the array without the last elemnt.
print(result)
