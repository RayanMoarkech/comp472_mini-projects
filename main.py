# Library imports
import json
import nltk
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
# from gensim.downloader import load
import gensim.downloader as api
from nltk.tokenize import word_tokenize

# File imports
from mnb_classifier import base_mnb, top_mnb
from dt_classifier import base_dt, top_dt
from compute_performance import flush_performance_file


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
def process_tokens(data_json):
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


# 2.2: Split the dataset into 80% for training and 20% for testing
# Takes in the dataset
# Prints the list of words with the occurrences
def split_dataset(data_json):
    data_train, data_test = train_test_split(data_json, test_size=0.2, random_state=0)
    return data_train, data_test


# 3.1: Load the data
# To load the word2vec-google-news-300 pretrained embedding model
def load_word2vector_data():
    corpus = api.load('word2vec-google-news-300')
    return corpus


# 3.2 Extract words from the Reddit posts using tokenizer from nlkt
def tokenize_reddit_posts(data_train, data_test):
    # train_values is a list of all Reddit post content from training set
    train_values = [data_array[0] for data_array in data_train]

    # test_values is a list of all Reddit post content from training set
    test_values = [data_array[0] for data_array in data_test]

    # Using nltk tokenizer to tokenize words in post
    train_tokens = [word_tokenize(i) for i in train_values]
    test_tokens = [word_tokenize(i) for i in test_values]

    # Flatten tokens to only have words, instead of list of words
    print()
    print("Number of tokens in the training set: ")
    print(len([words for sentence in train_tokens for words in sentence]))

    return train_tokens, test_tokens


# 3.3 Computing embedding of Reddit posts
def average_embeddings(tokens, corpus):
    average_embeddings = []
    for post in tokens:
        post_embedding = []
        for word in post:
            try:
                word_embedding = corpus[word]
                post_embedding.append(word_embedding)
            except (KeyError):
                pass
        if len(post_embedding) > 0:
            post_embedding_avg = np.average(post_embedding, axis=0)
            average_embeddings.append(post_embedding_avg)
    return average_embeddings


def flatten(tokens):
    flat_list = sum(tokens, [])
    print(flat_list)


# 3.4 Computing hit rates of training and test sets
def embedding_hit_rate(corpus, train_tokens, test_tokens):
    # flatten tokens to only have words, instead of list of words
    train_words = [words for post in train_tokens for words in post]
    test_words = [words for post in test_tokens for words in post]

    train_hit = 0
    for word in train_words:
        try:
            corpus[word]
            train_hit += 1
        except (KeyError):
            pass

    train_hit_rate = (train_hit / len(train_words)) * 100
    print(train_hit_rate, "%")

    test_hit = 0
    for word in test_words:
        try:
            corpus[word]
            test_hit += 1
        except (KeyError):
            pass

    test_hit_rate = (train_hit / len(train_words)) * 100
    print(test_hit_rate, "%")

    return train_hit_rate, train_hit_rate


# Main method of the code
def main():
    # 1.2: Get the dataset
    data_json = load_data(file_name='goemotions.json')

    # 1.3: Graph emotions histogram
    graph_histogram(data_json=data_json, index=1)

    # 1.3: Graph emotions histogram
    graph_histogram(data_json=data_json, index=2)

    # 2.1: Process the dataset
    process_tokens(data_json=data_json)

    # 2.2: Split the dataset for testing and training
    data_train, data_test = split_dataset(data_json=data_json)

    # Flush the performance.txt file to generate a new one
    # uncomment to regenerate!
    # flush_performance_file()

    # 2.3.1: Base-MNB
    base_mnb(data_train=data_train, data_test=data_test)

    # 2.3.2: Base-DT
    base_dt(data_train=data_train, data_test=data_test)

    # 2.3.4: Top-MNB
    top_mnb(data_train=data_train, data_test=data_test)

    # 2.3.5: Top-DT
    top_dt(data_train=data_train, data_test=data_test)

    # 3.1: Load
    corpus = load_word2vector_data()

    # 3.2 Extract words from the Reddit posts using tokenizer from nlkt
    # nltk.download('all')
    train_tokens, test_tokens = tokenize_reddit_posts(data_train, data_test)

    # 3.3 Computing embedding of Reddit posts
    average_embeddings(train_tokens, corpus)

    # 3.4 Computing hit rates of training and test sets
    embedding_hit_rate(corpus, train_tokens, test_tokens)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
