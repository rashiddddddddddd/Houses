# for index <- lb + 1 to ub
#   key <- array[index]
#   place <- index - 1 
#   while place >= lb and arr[place] > key
#       arr[place+1] <- arr[place]
#       place <- place - 1
#   arr[place+1] <- key



def Insertionsort(arr):
    for index in range (lb + 1,ub):
        key = arr[index]
        place = index - 1
        while place > lb and arr[place] > key:
            arr[place + 1] = arr[place]
            place = place - 1
        arr[place + 1] = key
        print(arr)

arr = [1,5,7,2,1,5,14,23,10,25]
lb = 0
ub = len(arr)

Insertionsort(arr)
print(arr)