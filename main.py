# This is a sample Python script.
import json

# Loads the data from a file
# Takes in a file_name string
# Returns a json dictionary
def load_data(file_name):
    file = open(file_name,)
    data_json = json.load(file)

    print(f"The dataset {file_name} is loaded")
    return data_json

# Main method of the code
def main():
    # Get the dataset
    data_json = load_data(file_name='goemotions.json')

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
