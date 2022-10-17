import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# Used to get the data
# Avoid duplications
# Returns:
# cv_train_fit: the CountVectorizer.fit_transform of the comments in the train data set
# target_true_train: array containing the target true value at index (emotions=1,sentiments=2) in the train data set
# cv_test_transform: the CountVectorizer.transform of the comments in the test data set
# target_true_test: array containing the target true value at index (emotions=1,sentiments=2) in the test data set
def get_true_cv_target_data(data_train, data_test, index):
    # Create a numpy array with the comments
    comments_train_array = [data_array[0] for data_array in data_train]
    comments_train_np = np.array(comments_train_array)

    # Get the training data comments
    cv = CountVectorizer()
    cv_train_fit = cv.fit_transform(comments_train_np)

    # Get the target train true values
    target_true_train = [data_array[index] for data_array in data_train]

    # Get the test set
    comments_test_array = [data_array[0] for data_array in data_test]
    comments_test_np = np.array(comments_test_array)
    cv_test_transform = cv.transform(comments_test_np)

    # Get the target test true values
    target_true_test = [data_array[index] for data_array in data_test]

    return cv_train_fit, target_true_train, cv_test_transform, target_true_test


# Creates a new file called `performance.txt`
# If the file exists, it flushes all the content inside it
def flush_performance_file():
    with open('performance.txt', 'w') as f:
        f.write('')


# 2.4: Save info in performance file
# Appends to the file
def write_to_performance_file(model_description, model_confusion_matrix, model_precision):
    with open('performance.txt', 'a') as f:
        f.writelines('')

# Computes the confusion matrix
def compute_confusion_matrix():
    print()


# Computes the classification report
def compute_classification_report():
    print()
