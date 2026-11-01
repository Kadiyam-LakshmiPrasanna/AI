facts = {"power_light_off","computer_not_starting"}
rules = {
         "check_power_supply":{"power_light_off","computer_not_starting"},
         "inspect_power_cable":{"check_power_supply"}}
def backward_chain(goal):
    if goal in facts:
        return True
    if goal not in rules:
        return False
    for condition in rules[goal]:
        if not backward_chain(condition):
            return False
    return True
goal = "inspect_power_cable"
print("Goal: ",goal)
if backward_chain(goal):
    print("Goal Proved")
else:
    print("Goal cant be proved")
        
