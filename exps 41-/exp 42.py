initial_state = {
    "on(A,Table)",
    "on(B,Table)",
    "clear(A)",
    "clear(B)"
    }
goal = {"on(A,B)"}
actions = {
    "Move(A,B)" : {
        "preconditions" : {"on(A,Table)","clear(A)","clear(B)"},
        "add" : {"on(A,B)"},
        "delete" : {"on(A,Table)","clear(B)"}
        }
    }
state = initial_state.copy()
plan = []
for action,details in actions.items():
    if details["preconditions"].issubset(state):
        state -= details["delete"]
        state |= details["add"]
        plan.append(action)
print("Plan: ",plan)
print("Final State: ",state)
print("Goal Reached: ",goal.issubset(state))
