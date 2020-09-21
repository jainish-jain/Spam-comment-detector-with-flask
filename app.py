from flask import Flask, render_template, request, jsonify
import pandas as pd 
#import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
import joblib



df= pd.read_csv("SPAM.csv")
df_data = df[["Message","Category"]]
# Features and Labels
df_x = df_data['Message']
df_y = df_data.Category
# Extract Feature With CountVectorizer
corpus = df_x
cv = CountVectorizer()
X = cv.fit_transform(corpus) # Fit the Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
#Naive Bayes Classifier
clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/predict', methods=['POST'])
def process():
    name = request.form['name']
    data = [name]
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)
    result = "Not a Spam"
    if my_prediction == 'spam':
        result="Spam"
        return jsonify({'error':result})
    return jsonify({'name':result})
	
	# email = request.form['email']
	# name = request.form['name']

	# if name and email:
	# 	newName = name[::-1]

	# 	return jsonify({'name' : newName})

	# return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)