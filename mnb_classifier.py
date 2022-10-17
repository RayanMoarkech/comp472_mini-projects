from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV

from compute_performance import *


# 2.3.1: Base-MNB
def base_mnb(data_train, data_test):
    print()
    print('-------------------------------------------------')
    print('Base MNB')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=1)
    base_mnb_model(
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )

    # Test on sentiments
    print()
    print('Sentiments:')
    cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=2)
    base_mnb_model(
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )


# Base-MNB model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def base_mnb_model(cv_train_fit, target_true_train, cv_test_transform, target_true_test):
    # Define the model classifier
    classifier = MultinomialNB()

    # Train the model
    model = classifier.fit(X=cv_train_fit, y=target_true_train)
    print("Class priors log = ", model.class_log_prior_)

    # Predict
    target_predict = model.predict(cv_test_transform)


# 2.3.4: Top-MNB
def top_mnb(data_train, data_test):
    print()
    print('-------------------------------------------------')
    print('Top MNB')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=1)
    top_mnb_model(
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )

    # Test on sentiments
    print()
    print('Sentiments:')
    cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=2)
    top_mnb_model(
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )


# Top-MNB model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def top_mnb_model(cv_train_fit, target_true_train, cv_test_transform, target_true_test):
    # Define the model classifier
    parameters = {
        'alpha': (0.5, 0, 2)
    }
    classifier = MultinomialNB()
    grid_search = GridSearchCV(classifier, parameters)

    # Train the model
    model = grid_search.fit(X=cv_train_fit, y=target_true_train)
    # print("Class priors log = ", model.class_log_prior_)

    # Predict
    target_predict = model.predict(cv_test_transform)

    # Get the test target true values


