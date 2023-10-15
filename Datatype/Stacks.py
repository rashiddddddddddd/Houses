
arr = ["" for i in range(11)]
basepointer = 0
toppointer = -1
stackful = len(arr) - 1

def push(arr,index):
    global basepointer,toppointer,stackful
    if toppointer == stackful:
        return "full array"
    else:
        toppointer = toppointer + 1
        arr[toppointer] = index
    return arr

def pop(arr):
    global basepointer,toppointer,stackful
    if toppointer == - 1:
        return "stack is empty"
    else:
        arr[toppointer] = ""
        toppointer = toppointer - 1
 
    return arr

j = 0
while j < 11:
    arr = push(arr,10)
    print(arr)
    j += 1



print(arr)
print("-------")
arr = pop(arr)
print(arr)

