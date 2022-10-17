import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


file_name = 'performance.txt'


data_class_org = {
  0: "reddit comments",
  1: "emotions",
  2: "sentiments"
}


# Used to get the data
# Avoid duplications
# Returns:
# target_name: emotions or sentiments based on the index
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

    return data_class_org[index], cv_train_fit, target_true_train, cv_test_transform, target_true_test


# Creates a new file called `performance.txt`
# If the file exists, it flushes all the content inside it
def flush_performance_file():
    with open(file_name, 'w') as f:
        f.write('')


# 2.4: Save info in performance file
# Appends to the file
def write_to_performance_file(model_description, target_true_test, target_predict):
    # Get the confusion matrix
    matrix = compute_confusion_matrix(target_true_test=target_true_test, target_predict=target_predict)

    # Get the classification report
    report = compute_classification_report(target_true_test=target_true_test, target_predict=target_predict)

    # Print details to file
    with open(file_name, 'a') as f:
        f.write(model_description + '\n')
        f.write('' + '\n')
        f.write('The Confusion Matrix:' + '\n')
        np.savetxt(fname=f, X=matrix, newline='\n')
        f.write('' + '\n')
        f.write('The Classification Report:' + '\n')
        f.write(report + '\n')
        f.write('' + '\n')
        f.write('----------------------------------------------------------------------------------------------' + '\n')
        f.write('' + '\n')


# Computes the confusion matrix
def compute_confusion_matrix(target_true_test, target_predict):
    return confusion_matrix(y_true=target_true_test, y_pred=target_predict)


# Computes the classification report
def compute_classification_report(target_true_test, target_predict):
    return classification_report(y_true=target_true_test, y_pred=target_predict)
