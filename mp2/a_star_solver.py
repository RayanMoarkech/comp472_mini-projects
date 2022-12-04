from rush_hour import RushHour
from heuristics import get_h1, get_h2, get_h3, get_h4, get_h5, get_h6
from file import write_search_file, write_solution_file

import time


def main(rush_hours: list[RushHour], heuristic_used: int):
    visited_boards: list[any] = []
    for index, rush_hour in enumerate(rush_hours):
        # Init config
        start_time = time.time()
        search_path_length = 0

        # Set lambda functions
        if heuristic_used == 1:
            get_h = get_h1
            take_f = take_f_h1
        elif heuristic_used == 2:
            get_h = get_h2
            take_f = take_f_h2
        elif heuristic_used == 3:
            get_h = get_h3
            take_f = take_f_h3
        elif heuristic_used == 4:
            get_h = get_h4
            take_f = take_f_h4
        elif heuristic_used == 5:
            get_h = get_h5
            take_f = take_f_h5
        elif heuristic_used == 6:
            get_h = get_h6
            take_f = take_f_h6

        # Get heuristic
        heuristic = get_h(rush_hour=rush_hour)

        # Search file names
        search_file_name = 'a-h' + str(heuristic_used) + '-search' + '-' + str(index+1) + '.txt'
        solution_file_name = 'a-h' + str(heuristic_used) + '-sol' + '-' + str(index+1) + '.txt'

        # Print initial board
        write_search_file(file_name=search_file_name, mode='w', f=heuristic, g=0, h=heuristic,
                          rush_hour=rush_hour, moved_vehicle_info=[])

        # Get all valid states and sort by min f
        open_valid_states = rush_hour.get_all_next_valid_states({})
        search_path_length += len(open_valid_states)
        # Sort the list
        open_valid_states.sort(key=take_f)

        # Get the initial is_solved values
        is_solved = False

        # Print all possible rush hours states
        while open_valid_states and not is_solved:

            # Pop the current node game
            current_node = open_valid_states.pop(0)
            visited_boards.append(current_node)

            # Start with the first valid state - min f

            # Get heuristic
            heuristic = get_h(rush_hour=current_node['rushHour'])
            g = len(current_node['vehicleInfo'])
            f = heuristic + g

            write_search_file(file_name=search_file_name, mode='a', f=f, g=g, h=heuristic,
                              rush_hour=current_node['rushHour'],
                              moved_vehicle_info=current_node['vehicleInfo'])

            # Check if the game is solved
            if current_node['rushHour'].solved():
                is_solved = True
                print("SOLVED")
                break

            # Get all the successors
            successors = current_node['rushHour'].get_all_next_valid_states(history=current_node)

            open_indexes_to_pop = set()  # To track the indexes that should be popped from the open list
            successor_indexes_to_pop = set()

            # if a node with the same position as successor is in the OPEN list
            # which has a lower f than successor, skip this successor
            for open_index, valid_rush_hour_state in enumerate(open_valid_states):
                for successor_index, successor in enumerate(successors):
                    # Check if both boards are the same
                    is_same = compare_boards(game1=valid_rush_hour_state['rushHour'],
                                             game2=successor['rushHour'])
                    if is_same:
                        # Get f values of both boards
                        successor_f = get_values(valid_rush_hour_state=successor, heuristic_used=heuristic_used)[-1]
                        valid_rush_hour_state_f = get_values(valid_rush_hour_state=valid_rush_hour_state,
                                                             heuristic_used=heuristic_used)[-1]
                        # compare and pop if successor f is higher
                        if successor_f >= valid_rush_hour_state_f:
                            successor_indexes_to_pop.add(successor_index)
                        else:
                            open_indexes_to_pop.add(open_index)

            # if a node with the same position as successor is in the CLOSED list
            # which has a lower f than successor, skip this successor
            for visited_board in visited_boards:
                for successor_index, successor in enumerate(successors):
                    # Check if both boards are the same
                    is_same = compare_boards(game1=visited_board['rushHour'], game2=successor['rushHour'])
                    if is_same:
                        # Get f values of both boards
                        successor_f = get_values(valid_rush_hour_state=successor, heuristic_used=heuristic_used)[-1]
                        visited_board_f = get_values(valid_rush_hour_state=visited_board,
                                                     heuristic_used=heuristic_used)[-1]
                        # compare and pop if successor f is higher
                        if successor_f >= visited_board_f:
                            successor_indexes_to_pop.add(successor_index)

            # Loop through the indexes
            # Pop all in successors that is not qualified
            for i, index_to_pop in enumerate(sorted(successor_indexes_to_pop)):
                successors.pop(index_to_pop-i)
            # Pop all in open list that has a higher value f compared to the successors
            for i, index_to_pop in enumerate(sorted(open_indexes_to_pop)):
                open_valid_states.pop(index_to_pop-i)

            # Add the len of the added successors to the search path
            search_path_length += len(successors)

            # Concat all the new valid states to the back of the open list
            open_valid_states += successors
            # Sort the list
            open_valid_states.sort(key=take_f)

        # Get the runtime
        runtime = time.time() - start_time
        # Check if there is a solution
        if open_valid_states:
            final_state = current_node
        else:
            final_state = {}
            print("UNSOLVABLE")
        # Write solution summary to file
        write_solution_file(file_name=solution_file_name, initial_game=rush_hour, final_state=final_state,
                            runtime=runtime, search_path_length=search_path_length)


# A lambda function used for sorting key
# take f value from the valid_rush_hour_state
def take_f_h1(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=1)[-1]


# A lambda function used for sorting key
# take f value from the valid_rush_hour_state
def take_f_h2(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=2)[-1]


# A lambda function used for sorting key
# take f value from the valid_rush_hour_state
def take_f_h3(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=3)[-1]


# A lambda function used for sorting key
# take f value from the valid_rush_hour_state
def take_f_h4(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=4)[-1]


# A lambda function used for sorting key
# take f value from the valid_rush_hour_state
def take_f_h5(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=5)[-1]


# A lambda function used for sorting key
# take f value from the valid_rush_hour_state
def take_f_h6(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=6)[-1]


# Get the h, g, and f values
# Takes in the valid rush hour state dictionary
# and the heuristic used
def get_values(valid_rush_hour_state: dict, heuristic_used: int):
    if heuristic_used == 1:
        h = get_h1(rush_hour=valid_rush_hour_state['rushHour'])
    elif heuristic_used == 2:
        h = get_h2(rush_hour=valid_rush_hour_state['rushHour'])
    elif heuristic_used == 3:
        h = get_h3(rush_hour=valid_rush_hour_state['rushHour'])
    elif heuristic_used == 4:
        h = get_h4(rush_hour=valid_rush_hour_state['rushHour'])
    elif heuristic_used == 5:
        h = get_h5(rush_hour=valid_rush_hour_state['rushHour'])
    elif heuristic_used == 6:
        h = get_h6(rush_hour=valid_rush_hour_state['rushHour'])
    g = len(valid_rush_hour_state['vehicleInfo'])
    f = h + g
    return h, g, f


def compare_boards(game1: RushHour, game2: RushHour) -> bool:
    return game1.board == game2.board
