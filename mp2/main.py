from file import get_games, generate_random_games, get_random_line, write_to_input_file
from heuristics import get_h1, get_h2, get_h4, get_h5, get_h6
from a_star_solver import main as a_star_solver
from gbfs import greedy_bfs as gbfs
from uniform_cost_search import main as UniformCostSearch
from file import create_analysis_file

# Global Variables
input_file = "metadata/input/sample-input.txt"

# Main method of the code
def main():
    # Create Analysis Headers
    create_analysis_file()

    # Add new random boards to input file
    # for i in range(50):
    #     write_to_input_file(get_random_line())

    # Get a list of RushHour objects from an input file
    # games = get_games(filename=input_file)

    # Get a list of RushHour objects from random
    # games = generate_random_games(count=5)

    # UCS
    # UniformCostSearch(rush_hours=games)

    # GBFS Algorithm with h1
    # gbfs(rush_hours=games, heuristic_used=1)

    # A Star Algorithm with h1
    # a_star_solver(rush_hours=games, heuristic_used=1)

    # GBFS Algorithm with h2
    # gbfs(rush_hours=games, heuristic_used=2)

    # A Star Algorithm with h2
    # a_star_solver(rush_hours=games, heuristic_used=2)

    # GBFS Algorithm with h3
    # gbfs(rush_hours=games, heuristic_used=3)

    # A Star Algorithm with h3
    # a_star_solver(rush_hours=games, heuristic_used=3)

    # GBFS Algorithm with h4
    # gbfs(rush_hours=games, heuristic_used=4)

    # A Star Algorithm with h4
    # a_star_solver(rush_hours=games, heuristic_used=4)

    # GBFS Algorithm with h5
    # gbfs(rush_hours=games, heuristic_used=5)

    # A Star Algorithm with h5
    # a_star_solver(rush_hours=games, heuristic_used=5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
