from collections import Counter
text = "I like AI.I like python.Ai is helpful"
words = text.lower().replace(".","").split()
uni= Counter(words)
bi = Counter(zip(words,words[1:]))
tri = Counter(zip(words,words[1:],words[2:]))

print(uni)
print(bi)
print(tri)
