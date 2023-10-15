


def BubbleSort(arr):
    swap = False
    lenarr = len(arr)
    while swap == False or lenarr == 0:
        swap = False
        for j in range(0, lenarr-1):
            if arr[j] <= arr[j+1]:
                swap = True
                arr[j], arr[j +1] = arr[j+1] , arr[j]
            print(arr)


arr = [23,124,42,12,1]
print("unsorted list:",arr)
BubbleSort(arr)
print("sorted list:",arr)


        