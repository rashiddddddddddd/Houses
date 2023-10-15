


arr = [20,3,4,8,12,99,1,16,22]
def BinarySearch(arr,high,low,search):
    mid = int((high + low) / 2)
    Found = False
    while (Found == False) or (low == high):
        if search >= arr[mid]:
            low = mid + 1
        elif search <= arr[mid]:
            high = mid + 1
        elif search == arr[mid]:
            Found = True
        else:
            Found = False
    print(Found)

def BubbleSort(arr):
    swap = False
    ub = len(arr)
    for n in range(ub-1,0,-1):
        for i in range(n):
            swap = False
            if arr[i] >= arr[i+1]:
                swap = True
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
    print(arr)

arr = [20,3,4,8,12,99,1,16,22]

BubbleSort(arr)
print(BinarySearch(arr,len(arr),0,4))
