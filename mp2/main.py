from file import get_games


# Global Variables
input_file = "metadata/input/sample-input.txt"


# Main method of the code
def main():
    print("Hello")

    # Get a list of RushHour objects from an input file
    games = get_games(filename=input_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
