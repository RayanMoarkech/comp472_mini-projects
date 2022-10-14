# This is a sample Python script.
import json
import matplotlib.pyplot as plt
import numpy as np

# Loads the data from a file
# Takes in a file_name string
# Returns a json dictionary
def load_data(file_name):
    file = open(file_name,)
    data_json = json.load(file)

    print(f"The dataset {file_name} is loaded")
    return data_json

# Graph a histogram with matplot
# Takes in a data_json with the index to retrieve
def graph_histogram(data_json, index):
    values = [set[index] for set in data_json]
    plt.figure(figsize=(15, 15))
    plt.hist(values)
    plt.xticks(rotation='vertical')
    plt.show()


# Main method of the code
def main():
    # Get the dataset
    data_json = load_data(file_name='goemotions.json')

    # Graph emotions histogram
    graph_histogram(data_json, 1)

    # Graph emotions histogram
    graph_histogram(data_json, 2)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
