import gensim.downloader as api
from nltk.tokenize import word_tokenize
import numpy as np

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
def average_embeddings(train_tokens, test_tokens, corpus):
    train_average_embeddings = []
    for post in train_tokens:
        post_embedding = []
        for word in post:
            try:
                word_embedding = corpus[word]
                post_embedding.append(word_embedding)
            except (KeyError):
                pass
        if len(post_embedding) > 0:
            post_embedding_avg = np.average(post_embedding, axis=0)
            train_average_embeddings.append(post_embedding_avg)
        else:
            train_average_embeddings.append([0] * 300)
    
    test_average_embeddings = []
    for post in test_tokens:
        post_embedding = []
        for word in post:
            try:
                word_embedding = corpus[word]
                post_embedding.append(word_embedding)
            except (KeyError):
                pass
        if len(post_embedding) > 0:
            post_embedding_avg = np.average(post_embedding, axis=0)
            test_average_embeddings.append(post_embedding_avg)
        else:
            test_average_embeddings.append([0] * 300)

    return train_average_embeddings, test_average_embeddings

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