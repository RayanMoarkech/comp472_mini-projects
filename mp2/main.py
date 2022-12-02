from file import get_games
from heuristics import get_h1, get_h2, get_h4, get_h5, get_h6
from a_star_solver import main as a_star_solver
from gbfs import greedy_bfs as gbfs


# Global Variables
input_file = "metadata/input/sample-input.txt"


# Main method of the code
def main():
    # Get a list of RushHour objects from an input file
    games = get_games(filename=input_file)

    # Board manipulation
    #sample_mod(initial_game=games[1])

    # print(get_h5(rush_hour=games[0]), get_h6(rush_hour=games[0]))
    # print(get_h5(rush_hour=games[1]), get_h6(rush_hour=games[1]))
    # print(get_h5(rush_hour=games[2]), get_h6(rush_hour=games[2]))
    # print(get_h5(rush_hour=games[3]), get_h6(rush_hour=games[3]))
    # print(get_h5(rush_hour=games[4]), get_h6(rush_hour=games[4]))
    # print(get_h5(rush_hour=games[5]), get_h6(rush_hour=games[5]))

    # GBFS Algorithm with h1
    # gbfs(rush_hours=games, heuristic_used=1)

    # A Star Algorithm with h1
    a_star_solver(rush_hours=games, heuristic_used=1)

    # GBFS Algorithm with h2
    # gbfs(rush_hours=games, heuristic_used=2)

    # A Star Algorithm with h2
    a_star_solver(rush_hours=games, heuristic_used=2)

    # GBFS Algorithm with h3
    # gbfs(rush_hours=games, heuristic_used=3)

    # A Star Algorithm with h3
    a_star_solver(rush_hours=games, heuristic_used=3)

    # GBFS Algorithm with h4
    # gbfs(rush_hours=games, heuristic_used=4)

    # A Star Algorithm with h4
    # a_star_solver(rush_hours=games, heuristic_used=4)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
