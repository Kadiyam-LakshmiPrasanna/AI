world = {
    (1,1) : {'Safe':True},
    (1,2) : {'Breeze':True},
    (2,1) : {'Stench':True},
    (2,2) : {'Gold':True}
    }
safe_cells = {(1,1)}
position = (1,1)
def perceive(cell):
    return world.get(cell,{})
print("Starting at: ",position)

position = (1,2)
percept = perceive(position)
print("At",position,"percepts: ",percept)
if percept.get("Breeze"):
    print("Adjacent cells may contain a pit.")
    
position = (2,2)
percept = perceive(position)
print("At",position,"percepts: ",percept)
if percept.get("Gold"):
    print("Gold Found!")
    
