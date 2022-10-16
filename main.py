# This is a sample Python script.
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


# 1.2: Loads the data from a file
# Takes in a file_name string
# Returns a json dictionary
def load_data(file_name):
    # Open the json file and load it
    file = open(file_name, )
    data_json = json.load(file)

    # Print
    print()
    print('-------------------------------------------------')
    print('Load Data')
    print('-------------------------------------------------')
    print(f"The dataset {file_name} is loaded")

    return data_json


# 1.3: Graph a histogram with matplot
# Takes in a data_json with the index to retrieve
def graph_histogram(data_json, index):
    values = [data_array[index] for data_array in data_json]
    plt.figure(figsize=(15, 15))
    plt.hist(values)
    plt.xticks(rotation='vertical')
    plt.show()


# 2.1: Process the dataset with CountVectorizer
# Takes in the dataset
# Prints the list of words with the occurrences
def processTokens(data_json):
    # Create a numpy array with the comments
    comments_array = [data_array[0] for data_array in data_json]
    comments_np = np.array(comments_array)

    # Create training data
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(comments_np)

    # Get the count and words array
    count_array = cv_fit.toarray().sum(axis=0)
    word_array = cv.get_feature_names_out()

    # Print the count of each word
    print()
    print('-------------------------------------------------')
    print('Tokens occurrences')
    print('-------------------------------------------------')
    print(dict(zip(word_array, count_array)))
    # for index, token in enumerate(word_array):
    #     print(token, ': ', count_array[index])


# Main method of the code
def main():
    # 1.2: Get the dataset
    data_json = load_data(file_name='goemotions.json')

    # 1.3: Graph emotions histogram
    graph_histogram(data_json, 1)

    # 1.3: Graph emotions histogram
    graph_histogram(data_json, 2)

    # 2.1: Process the dataset
    processTokens(data_json)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
