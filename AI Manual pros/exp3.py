import random
def f(x):
    return x*x
x=5
T=100
cooling = 0.9
while T>1:
    new_x = x+random.uniform(-1,1)
    if f(new_x) < f(x):
        x = new_x
    else:
        chance = random.random()
        if chance < 0.1:
            x = new_x
    T = T*cooling

print("Best x: ",x)
print("Minimum value: ",f(x))
