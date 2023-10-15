TheData = [20,3,4,8,12,99,1,16,22]
# sort in ascending order using insertion sort 

def sortTheData(TheData):
    lb = 0
    ub = len(TheData)
    if ub <= 1:
      return
    for i in range(1,ub):
        key = TheData[i]
        place = i - 1
        while place >= lb and key < TheData[place]:
            TheData[place + 1] = TheData[place]
            place -= 1
        TheData[place + 1] = key
        print(TheData)


sortTheData(TheData)
print(TheData)
