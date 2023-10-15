def BinarySearch(arr, search):
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == search:
            return mid
        elif search < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1 
 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(BinarySearch(arr, 5))