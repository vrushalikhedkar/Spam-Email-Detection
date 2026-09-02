# 📩 SMS Spam Detection using Machine Learning

A Machine Learning project that classifies SMS messages as Spam or Ham (Not Spam) using CountVectorizer and Multinomial Naive Bayes.


<p align="center">
  <img src="Spam Email Detection image.png" width="1000">
</p>


### 📌 Project Overview

The goal of this project is to automatically identify whether an SMS message is spam or a normal message.

- **Spam** → unwanted/promotional messages
- **Ham** → normal/legitimate messages

#


### 📂 Dataset

This project uses the SMS Spam Collection dataset.

- ```ham``` → Normal message
- ```spam``` → Spam message

#


### 🔄 Project Steps

**1️. Load the dataset**

**2️. Check missing values**

**3️. Remove duplicate messages**

**4️. Convert labels into numbers**

**5️. Split the dataset**

**6️. Apply CountVectorizer**

**7️. Train Naive Bayes model**

**8️. Make predictions**

**9️. Check accuracy**

**10. Check confusion matrix**


#


### 🔢 Label Mapping

{'ham': 0, 'spam': 1}

- 0 = Ham

- 1 = Spam


#


### 🔤 Text Vectorization

CountVectorizer converts the SMS text into numerical word-count features. This allows the Machine Learning model to understand and process the text data.


#


### 🤖 Machine Learning Model

***Multinomial Naive Bayes*** is used to classify the SMS messages into Spam and Ham categories.

It is suitable for text classification because it works well with word-count-based features.


#


### 📊 Model Performance

**Accuracy**

98.55%

The model correctly classified approximately 98.55% of the test messages.


#


### Confusion Matrix

The confusion matrix shows the correctly and incorrectly classified Ham and Spam messages.

- 891 → Ham correctly classified
- 128 → Spam correctly classified
- 5 → Ham incorrectly classified as Spam
- 10 → Spam incorrectly classified as Ham


#


### 🧪 Message Testing

A new SMS message was tested using the trained model.

Example: text```Congratulations! You have won a free prize```

Prediction: ```Spam```


#
