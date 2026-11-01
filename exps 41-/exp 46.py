import random
import matplotlib.pyplot as plt
Q = [0.0] * 5
alpha,gamma,epsilon = 0.1,0.9,0.2
rewards = []
for episode in range(100):
    state,total = 0,0
    while state < 4:
        action = random.choice([0,1]) if random.random() < epsilon else (0 if Q[state] >= Q[state + 1] else 1)
        next_state = state + 1
        reward = 10 if next_state == 4 else -1
        Q[state] += alpha * (reward + gamma * Q[next_state] - Q[state])
        total += reward
        state = next_state
    rewards.append(total)
print("learned Q values: ",[round(x,2) for x in Q])
print("Final Cumulative reward: ",rewards[-1])
plt.plot(rewards)
plt.xlabel("Episode")
plt.ylabel("Cumulative reward")
plt.ylabel("Reward across Episodes")
plt.show()


            
