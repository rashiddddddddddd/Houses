# linear search

arr = [1,2,3,4,5,6,7,8,9,10]

def LinearSearch(arr,search):
    found = False
    for i in range(0,len(arr)):
        if arr[i] == search:
           found = True
           return found
        else: 
            found = False
            return found
        

print(f"{LinearSearch(arr, 4)}")