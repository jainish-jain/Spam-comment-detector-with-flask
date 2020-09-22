# Spam Comment Detector

This repository is based on the flask framework web application, with the help of Machine Learning, the application is capable to detect that the comment is spam or not.  

## File Structure

📦Spam-comment-detector-with-flask
 ┣ 📂static
 ┃ ┗ 📂js
 ┃    ┣ 📜app.js
 ┃    ┣ 📜form.js
 ┃    ┗ 📜particles.js
 ┣ 📂templates
 ┃ ┗ 📜form.html
 ┣ 📜SPAM.csv
 ┣ 📜app.py
 ┗ 📜requirements.txt

## Flask

A microframework based on Werkzeug. It's extensively documented
and follows best practice patterns.

## Model

#### CountVectorizer

Convert a collection of text documents to a matrix of token counts.This implementation produces a sparse representation of the counts using
scipy.sparse.coo_matrix.

If you do not provide an a-priori dictionary and you do not use an analyzer
that does some kind of feature selection then the number of features will
be equal to the vocabulary size found by analyzing the data.

#### Train Test Split

Split arrays or matrices into random train and test subsets. Quick utility that wraps input validation and ``next(ShuffleSplit().split(X, y))`` and application to input data into a single call for splitting (and optionally subsampling) data in a oneliner.

#### Naive Bayes classifier for multinomial models

The multinomial Naive Bayes classifier is suitable for classification with
discrete features (e.g., word counts for text classification). The
multinomial distribution normally requires integer feature counts. However,
in practice, fractional counts such as tf-idf may also work.

### Requirements.txt

- Click==7.0

- Flask==1.1.2

- pandas==1.1.0

- sklearn==0.0

- joblib==0.16.0

- gunicorn==20.0.4

- itsdangerous==1.1.0

- Jinja2==2.10.3

- MarkupSafe==1.1.1

- Werkzeug==0.16.0

### GUI

<img title="" src="file:///guiimages/mainscreen.png" alt="">

<img title="" src="file:///guiimages/spamscreen.png" alt="">

<img title="" src="file:///guiimages/hamscreen.png" alt="">
