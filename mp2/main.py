from file import get_games
from rush_hour import Move
from heuristics import get_h1, get_h2
from gbfs import greedy_bfs
from a_star_solver import main as a_star_solver
from gbfs import greedy_bfs as gbfs

import copy


# Global Variables
input_file = "metadata/input/sample-input.txt"


# Main method of the code
def main():
    # Get a list of RushHour objects from an input file
    games = get_games(filename=input_file)

    # Board manipulation
    sample_mod(initial_game=games[1])

    # A Star Algorithm with h1
    #a_star_solver(rush_hours=games, heuristic_used=1)
    #gbfs(rush_hours=games, heuristic_used=1)
    #sample_mod(initial_game=games[0])

    # A Star Algorithm with h1
    #a_star_solver(rush_hours=games, heuristic_used=1)
    gbfs(rush_hours=games, heuristic_used=1)

    # A Star Algorithm with h2
    # a_star_solver(rush_hours=games, heuristic_used=2)

    # A Star Algorithm with h3
    # a_star_solver(rush_hours=games, heuristic_used=3)


# A sample function with some board manipulations with RushHour methods
def sample_mod(initial_game):
    # Deep copy the array to be modified and used
    game = copy.deepcopy(initial_game)

    # for line in game.board:
    #     for el in line:
    #         print(el, end=" ")
    #     print()

    # print()

    # # Move M down 2 spots
    # game.move_vehicle(Move.DOWN, 2, "M")
    # for line in game.board:
    #     for el in line:
    #         print(el, end=" ")
    #     print()

    # print()

    # Move A right once
    # game.move_vehicle(Move.RIGHT, 1, "A")
    # for line in game.board:
    #     for el in line:
    #         print(el, end=" ")
    #     print()

    #valid_states = game.get_all_next_valid_states({})

    # for state in valid_states:
    #     for line in state.board:
    #         for el in line:
    #             print(el, end=" ")
    #         print()
    #     print()

    # for state in valid_states:
    #     print("h1", get_h1(state['game']))
    #     print("h2", get_h2(state))

    #greedy_bfs({'rushHour': game, 'vehicleName': ''}, get_h1)
    #     print("h1", get_h1(state))
    #     print("h2", get_h2(state))
    # for state in valid_states:
    #     for line in state['rushHour'].board:
    #         for el in line:
    #             print(el, end=" ")
    #         print()
    #     print()

    #greedy_bfs(game, get_h1)

    # Get vehicle position
    # print(game.get_vehicle("A").positions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
