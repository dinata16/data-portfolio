# Text Classification on BBC News Archive Using Neural Networks

In this article, we explore how to build a text classification model for the BBC News Archive dataset using a neural network. Text classification is a fundamental task in natural language processing (NLP) with applications in sentiment analysis, spam detection, and more. Here, we demonstrate how to preprocess the data, build the model, and evaluate its performance.

## Dataset Overview

The dataset contains two columns:
- `text`: The content of BBC news articles.
- `category`: The category or label for each article, such as business, politics, sport, etc.

The objective is to classify each article into its respective category based on its text content.

## Steps to Build the Model

### 1. Import Libraries
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
```
We import necessary libraries for data processing, visualization, and building the neural network model.

### 2. Load and Inspect Data
```python
df = pd.read_csv('bbc-text.csv')
print(df.head())
```
The dataset is loaded into a Pandas DataFrame. Inspecting the first few rows provides insight into the structure of the data.

### 3. Visualize Data Distribution
```python
df['category'].value_counts().plot(kind='bar')
plt.title('Distribution of News Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
```
A bar chart shows the distribution of news articles across categories. This helps in understanding the balance of the dataset.

### 4. Preprocess Data
#### Text Preprocessing
```python
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_data(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    text = ' '.join([w for w in word_tokens if w not in stop_words])
    return text

df['text'] = df['text'].apply(preprocess_data)
```
The preprocessing function converts text to lowercase, removes special characters and numbers, and eliminates stop words.

#### Tokenization and Padding
```python
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
X = pad_sequences(sequences, maxlen=200)
y = pd.get_dummies(df['category']).values
```
We tokenize the text data into sequences of integers and pad them to ensure uniform length. The labels are one-hot encoded for compatibility with the neural network.

### 5. Split Data
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
The data is split into training and testing sets using an 80-20 split.

### 6. Build the Neural Network
```python
model = Sequential([
    Embedding(input_dim=10000, output_dim=128, input_length=200),
    LSTM(128, return_sequences=True),
    LSTM(64),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
```
The model consists of embedding layers, LSTM layers, and dense layers for classification. We use the Adam optimizer and categorical cross-entropy loss.

### 7. Train the Model
```python
history = model.fit(X_train, y_train, validation_split=0.2, epochs=10, batch_size=32)
```
The model is trained for 10 epochs with a batch size of 32. A validation split ensures we can monitor the model's performance during training.

### 8. Evaluate the Model
```python
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_accuracy:.2f}')
```
The test dataset is used to evaluate the model's accuracy after training.

### 9. Generate Classification Report
```python
from sklearn.metrics import classification_report

y_pred = np.argmax(model.predict(X_test), axis=1)
y_true = np.argmax(y_test, axis=1)
print(classification_report(y_true, y_pred, target_names=df['category'].unique()))
```
A classification report provides precision, recall, and F1-score for each category.

### 10. Analyze Model Performance
The graph below shows the model's accuracy during training and testing over the epochs:

![Model Accuracy](https://github.com/user-attachments/assets/c1da5d42-ec8a-4c64-82bb-230388111263)

From the graph, it is evident that the model achieves high accuracy on both training and testing data after 5 epochs, indicating minimal overfitting. 

Additionally, the classification report below provides detailed performance metrics:

**Classification Report:**
```
               precision    recall  f1-score   support

     business       0.91      0.90      0.91       102
entertainment       0.88      0.94      0.91        77
     politics       0.97      0.87      0.92        84
        sport       0.99      0.93      0.96       102
         tech       0.85      0.96      0.90        80

     accuracy                           0.92       445
    macro avg       0.92      0.92      0.92       445
 weighted avg       0.92      0.92      0.92       445
```
The model performs exceptionally well across all categories, achieving an overall accuracy of 92%. The high precision, recall, and F1-scores indicate the model's reliability in classifying news articles.

## Conclusion
This project demonstrates how to build a text classification model using the BBC News Archive dataset. By preprocessing the data, designing a neural network, and evaluating its performance, we successfully classified news articles into their respective categories. This pipeline can be extended to other text classification tasks with similar datasets.

You can access the code and dataset [here](https://www.kaggle.com/datasets/hgultekin/bbcnewsarchive).

---

*Happy coding!*
