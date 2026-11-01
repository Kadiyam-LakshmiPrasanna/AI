from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
texts = [
    "win a free prize now",
    "claim your free gift",
    "Meeting is scheduled tomorrow",
    "Please submit the assignment",
    "Congratulations you won money",
    "The project meeting is at 10AM"
    ]
labels = ["spam","spam","not spam","not spam","spam","not spam"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X,labels)
test_texts = [
            "win a free gift",
            "please attend the project meeting"
    ]
X_test = vectorizer.transform(test_texts)
predictions = model.predict(X_test)
for text,result in zip(test_texts,predictions):
    print(text,"->",result)
