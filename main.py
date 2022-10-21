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
import time

# File imports
from mnb_classifier import base_mnb, top_mnb
from dt_classifier import base_dt, top_dt
from mlp_classifier import base_mlp, base_mlp_embeddings, top_mlp, top_mlp_embeddings
from embeddings import load_word2vector_data, tokenize_reddit_posts, embedding_hit_rate, load_fasttext_data, load_glove_data
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

    #2.3.3: Base-MLP
    base_mlp(data_train=data_train, data_test=data_test)

    # 2.3.2: Base-DT
    base_dt(data_train=data_train, data_test=data_test)

    # 2.3.4: Top-MNB
    top_mnb(data_train=data_train, data_test=data_test)

    # 2.3.5: Top-DT
    top_dt(data_train=data_train, data_test=data_test)
    
    # 2.3.6 Top-MLP
    top_mlp(data_train=data_train, data_test=data_test)

    # 3.1: Load
    corpus = load_word2vector_data()

    # 3.2 Extract words from the Reddit posts using tokenizer from nlkt
    # nltk.download('all')
    train_tokens, test_tokens = tokenize_reddit_posts(data_train, data_test)

    # 3.3 Computing embedding of Reddit posts
    train_average_embeddings, test_average_embeddings = average_embeddings(train_tokens, test_tokens, corpus)

    # 3.4 Computing hit rates of training and test sets
    #embedding_hit_rate(corpus, train_tokens, test_tokens)

    # 3.5 Train Base-MLP
    base_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, corpus)

    # 3.6: Top-MLP for embeddings
    top_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, corpus)

    #3.8 Different pre-trained Engish models
    fasttext_corpus = load_fasttext_data()
    base_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, fasttext_corpus, "FastText")
    top_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, fasttext_corpus, "FastText")

    glove_corpus = load_glove_data()
    base_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, glove_corpus, "Glove")
    top_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, glove_corpus, "Glove")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
