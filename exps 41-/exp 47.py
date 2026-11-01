from collections import Counter
text = "I like AI.I like python.AI is useful."
words = text.lower().replace(".","").split()
uni = Counter(words)
bi = Counter(zip(words,words[1:]))
tri = Counter(zip(words,words[1:],words[2:]))
print("Unigram: ",uni)
print("Bigram: ",bi)
print("Trigram: ",tri)
words = "like"
next_words = {b[1]:c for b,c in bi.items() if b[0] == words}
print("\nNext word after 'like': ",max(next_words,key=next_words.get))
print("P(AI|PYTHON)= ",bi[("python","ai")]/uni["python"] if bi[("python","ai")] else 0)
v = len(uni)
p = (bi[("python","ai")]+1)/(uni["python"]+v)
print("Smoothed P(AI|python)= ",round(p,3))
