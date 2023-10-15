# bubble sort

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
  
  
#insertion sort

def InsertionSort(arr):
  lb = 0
  ub = len(arr)
  if ub <=1:
    return
  for i in range(1, ub):
    key = arr[i]
    place = i-1
    while place >= lb and key < arr[place]:
      arr[place+1] = arr[place]
      place -= 1
    arr[place+1] = key 
    print(arr)
  
arr = [83,1,7,13,19,27,73,19,43,21,4]

print("before:",arr)
InsertionSort(arr)

print("----------")

arr = [83,1,7,13,19,27,73,19,43,21,4]

print("before:", arr)
BubbleSort(arr)
