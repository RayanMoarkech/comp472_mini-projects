from rush_hour import RushHour
from file import write_search_file, write_solution_file, write_to_analysis_file

import time


def main(rush_hours: list[RushHour]):
    visited_boards: list[any] = []
    for index, rush_hour in enumerate(rush_hours):
        # Init config
        start_time = time.time()
        search_path_length = 0
        g = 0

        # Search file names
        search_file_name = 'ucs' + '-search' + '-' + str(index+1) + '.txt'
        solution_file_name = 'ucs' + '-sol' + '-' + str(index+1) + '.txt'

        # Print initial board
        write_search_file(file_name=search_file_name, mode='w', f=g, g=g, h=0,
                          rush_hour=rush_hour, moved_vehicle_info=[])

        # Get all valid states and sort by min g
        open_valid_states = rush_hour.get_all_next_valid_states({})
        search_path_length += len(open_valid_states)

        # Sort the list
        open_valid_states.sort(key=take_g)

        # Get the initial is_solved values
        is_solved = False

        # Print all possible rush hours states
        while open_valid_states and not is_solved:

            # Pop the current node game
            current_node = open_valid_states.pop(0)
            visited_boards.append(current_node)

            # Start with the first valid state - min g

            heuristic = 0
            g = len(current_node['vehicleInfo'])
            f = heuristic + g

            write_search_file(file_name=search_file_name, mode='a', f=f, g=g, h=0,
                              rush_hour=current_node['rushHour'],
                              moved_vehicle_info=current_node['vehicleInfo'])
            # # Sort the list
            open_valid_states.sort(key=take_g)

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
                        successor_g = get_values(valid_rush_hour_state=successor)[-1]
                        valid_rush_hour_state_g = get_values(valid_rush_hour_state=valid_rush_hour_state)[-1]
                        # compare and pop if successor f is higher
                        if successor_g >= valid_rush_hour_state_g:
                            successor_indexes_to_pop.add(successor_index)
                        else:
                            open_indexes_to_pop.add(open_index)

            # if a node with the same position as successor is in the CLOSED list
            # which has a lower g than successor, skip this successor
            for visited_board in visited_boards:
                for successor_index, successor in enumerate(successors):
                    # Check if both boards are the same
                    is_same = compare_boards(game1=visited_board['rushHour'], game2=successor['rushHour'])
                    if is_same:
                        # Get g values of both boards
                        successor_g = get_values(valid_rush_hour_state=successor)[-1]
                        visited_board_g = get_values(valid_rush_hour_state=visited_board)[-1]
                        # compare and pop if successor g is higher
                        if successor_g >= visited_board_g:
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
            open_valid_states.sort(key=take_g)

        # Get the runtime
        runtime = time.time() - start_time
        # Check if there is a solution
        if open_valid_states:
            final_state = current_node
        else:
            final_state = {}
            print("no solution")
        # Write solution summary to file
        write_solution_file(file_name=solution_file_name, initial_game=rush_hour, final_state=final_state,
                            runtime=runtime, search_path_length=search_path_length)

        write_to_analysis_file(puzzle_number=index, algorithm='UCS', heuristic='NA', final_state=final_state,
                               runtime=runtime, search_path_length=search_path_length)

# take g value from the valid_rush_hour_state
def take_g(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state)[-1]


# Get the g, and f values
# Takes in the valid rush hour state dictionary
def get_values(valid_rush_hour_state: dict):
    g = len(valid_rush_hour_state['vehicleInfo'])
    f = g
    return g, f


def compare_boards(game1: RushHour, game2: RushHour) -> bool:
    return game1.board == game2.board
