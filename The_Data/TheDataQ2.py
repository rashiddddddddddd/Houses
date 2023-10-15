TheData = [20,3,4,8,12,99,1,16,22]


def search(TheData, SearchValue):
    Found = False
    lenarr = len(TheData)
    for i in range(lenarr):
        if SearchValue == TheData[i]:
            Found = True
        elif SearchValue != TheData[i]:
            Found = False
    return Found

TheData = [20,3,4,8,12,99,1,16,22]

search(TheData,13)
