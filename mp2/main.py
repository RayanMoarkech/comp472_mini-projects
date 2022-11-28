from file import get_games
from rush_hour import Move
import copy


# Global Variables
input_file = "metadata/input/sample-input.txt"


# Main method of the code
def main():
    print("Hello")

    # Get a list of RushHour objects from an input file
    games = get_games(filename=input_file)

    # Board manipulation
    sample_mod(initial_game=games[0])


# A sample function with some board manipulations with RushHour methods
def sample_mod(initial_game):
    # Deep copy the array to be modified and used
    game = copy.deepcopy(initial_game)

    for line in game.board:
        for el in line:
            print(el, end=" ")
        print()

    print()

    # Move M down 2 spots
    game.move_vehicle(Move.DOWN, 2, "M")
    for line in game.board:
        for el in line:
            print(el, end=" ")
        print()

    print()

    # Move A right once
    game.move_vehicle(Move.RIGHT, 1, "A")
    for line in game.board:
        for el in line:
            print(el, end=" ")
        print()

    print()

    # Get vehicle position
    print(game.get_vehicle("A").positions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
