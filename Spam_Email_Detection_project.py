import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
dataset = pd.read_csv('SMSSpamCollection.csv')
dataset
dataset.shape
dataset['label'].value_counts()
dataset.isnull().sum()
dataset.duplicated().sum()
dataset = dataset.drop_duplicates()
dataset
X = dataset['message']
y = dataset['label'].map({'ham': 0, 'spam': 1}).values
X
y
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)
X_train.shape
X_test.shape
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
X_train.shape
X_test.shape
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred
print(y_pred[:10])   ## phle 10 msg
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
cr
message = ["Congratulations! You have won a free prize"]
message_vector = vectorizer.transform(message)
prediction = model.predict(message_vector)
prediction
if prediction[0] == 1:
    print('Spam')
else:
    print('Ham')


