import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer


# 2.3.1: Base-MNB
def base_mnb(data_train, data_test):
    print()
    print('-------------------------------------------------')
    print('Base MNB')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    base_mnb_model(data_train=data_train, data_test=data_test, index=1)

    # Test on sentiments
    print()
    print('Sentiments:')
    base_mnb_model(data_train=data_train, data_test=data_test, index=2)


# Base-MNB model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def base_mnb_model(data_train, data_test, index):
    # Create a numpy array with the comments
    comments_array = [data_array[0] for data_array in data_train]
    comments_np = np.array(comments_array)

    # Create training data
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(comments_np)
    target_vector = [data_array[index] for data_array in data_train]

    # Train the model
    classifier = MultinomialNB()
    model = classifier.fit(X=cv_fit, y=target_vector)
    print("Class priors log = ", model.class_log_prior_)

    # Predict
    test = cv.transform(np.array([data_test[1][0]]))
    predict = model.predict(test)
    print('Predicted class =', predict, '; Target class =', data_test[1][index])
