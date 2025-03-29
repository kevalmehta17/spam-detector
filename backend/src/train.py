from preprocess import load_and_clean_data
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.naive_bayes import MultinomialNB 
from sklearn.model_selection import train_test_split 
from joblib import dump 

# Load the dataset
df = load_and_clean_data('../data/spam.csv')

# Split the dataset into features and lables:-

x_train, x_test, y_train, y_test = train_test_split(df['message'],df['label'],test_size=0.2, random_state=42) #80% training and 20% testing 


vectorizer  = TfidfVectorizer() #TF-IDF:- usefull for the text-classification
x_train_tfidf = vectorizer.fit_transform(x_train)
x_test_tfidf = vectorizer.transform(x_test) #transform the test data using the same vectorizer

# Train the model
model = MultinomialNB() #create Native bayes classifier object
model.fit(x_train_tfidf, y_train) #Train the model using the training data

# Save model & vectorizer

dump(model,"../models/spam_classifier.joblib") 
dump(vectorizer,"../models/vectorizer.joblib") 
# dump() is from the joblib library, which is used for saving and loading Python objects efficiently.

print("Model and vectorizer saved successfully.")