world = [
    ['S','-','-','-'],
    ['-','P','-','-'],
    ['-','-','W','-'],
    ['-','-','-','G']
    ]
print("Wumpus World")
print()

for row in world:
    print(row)
print("\nAgent starts at(0,0)")
x=0
y=0
#move right
y=y+1
print("Move Right->",(x,y))

#move right
y=y+1
print("Move Right->",(x,y))

#move down
x=x+1
print("Move Down->",(x,y))

#move down
x=x+1
print("Move Down->",(x,y))

if world[x][y] == "W":
    print("Wumpus found! Game over")
elif world[x][y] == "P":
    print("Pit found! Game over")
elif world[x][y] == "G":
    print("Gold found! you win")
else:
    print("Safe cell")
        
