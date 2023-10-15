#2 teams 

test = int(input())
for i in range(test):
    players = int(input())
    team1 = [int(power) for power in input().split(' ')]
    team2 = [int(power) for power in input().split(' ')]
    i = 0
    while len(team1) != 0 and len(team2) != 0:
        if team1[i] > team2[i]:
            team2.pop(0)
            i = i + 1
        elif team2[i] > team1[i]:
            team1.pop(0)
            i = i + 1
