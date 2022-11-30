from rush_hour import RushHour
from heuristics import get_h1
from file import write_search_file, write_solution_file

import functools
import time


def main(rush_hours: list[RushHour], heuristic_used: int):
    visited_boards: list[any] = []
    for index, rush_hour in enumerate(rush_hours):
        # Init config
        start_time = time.time()
        search_path_length = 0

        # Get heuristic
        if heuristic_used == 1:
            heuristic = get_h1(rush_hour=rush_hour)
            take_f = take_f_h1

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

            # Start with the first valid state - min f

            # Get heuristic
            if heuristic_used == 1:
                heuristic = get_h1(rush_hour=open_valid_states[0]['rushHour'])
            g = len(open_valid_states[0]['vehicleInfo'])
            f = heuristic + g

            write_search_file(file_name=search_file_name, mode='a', f=f, g=g, h=heuristic,
                              rush_hour=open_valid_states[0]['rushHour'],
                              moved_vehicle_info=open_valid_states[0]['vehicleInfo'])

            # Check if the game is solved
            if open_valid_states[0]['rushHour'].solved():
                is_solved = True
                print("SOLVED")
                break

            # Get all the successors
            successors = open_valid_states[0]['rushHour'].get_all_next_valid_states(history=open_valid_states[0])
            search_path_length += len(successors)

            # if a node with the same position as successor is in the OPEN list
            # which has a lower f than successor, skip this successor
            for valid_rush_hour_state in open_valid_states:
                for successor_index, successor in enumerate(successors):
                    # Check if both boards are the same
                    is_same = compare_boards(board1=valid_rush_hour_state['rushHour'].board,
                                             board2=successor['rushHour'].board)
                    if is_same:
                        # Get f values of both boards
                        successor_f = get_values(valid_rush_hour_state=successor, heuristic_used=heuristic_used)[-1]
                        valid_rush_hour_state_f = get_values(valid_rush_hour_state=valid_rush_hour_state,
                                                             heuristic_used=heuristic_used)[-1]
                        # compare and pop if successor f is higher
                        if successor_f >= valid_rush_hour_state_f:
                            successors.pop(successor_index)

            # if a node with the same position as successor is in the CLOSED list
            # which has a lower f than successor, skip this successor
            for visited_board in visited_boards:
                for successor_index, successor in enumerate(successors):
                    # Check if both boards are the same
                    is_same = compare_boards(board1=visited_board['rushHour'].board, board2=successor['rushHour'].board)
                    if is_same:
                        # Get f values of both boards
                        successor_f = get_values(valid_rush_hour_state=successor, heuristic_used=heuristic_used)[-1]
                        visited_board_f = get_values(valid_rush_hour_state=visited_board,
                                                     heuristic_used=heuristic_used)[-1]
                        # compare and pop if successor f is higher
                        if successor_f >= visited_board_f:
                            successors.pop(successor_index)

            # Concat all the new valid states to the back of the open list
            open_valid_states += successors
            # Sort the list
            open_valid_states.sort(key=take_f)

            # Pop the tested path
            popped = open_valid_states.pop(0)
            visited_boards.append(popped)

        # Write solution summary to file
        runtime = time.time() - start_time
        write_solution_file(file_name=solution_file_name, initial_game=rush_hour, final_state=open_valid_states[0],
                            runtime=runtime, search_path_length=search_path_length)


def get_min_f(valid_rush_hour_states: list[any], heuristic_used: int):
    min_f = get_values(valid_rush_hour_state=valid_rush_hour_states[0], heuristic_used=heuristic_used)[-1]
    index = 0
    for i, valid_rush_hour_state in enumerate(valid_rush_hour_states):
        current_f = get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=heuristic_used)[-1]
        if min_f > current_f:
            min_f = current_f
            index = i
    return min_f, index


# take f value from the valid_rush_hour_state
def take_f_h1(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=1)[-1]


# take f value from the valid_rush_hour_state
def take_f_h2(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=2)[-1]


# take f value from the valid_rush_hour_state
def take_f_h3(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=3)[-1]


# take f value from the valid_rush_hour_state
def take_f_h4(valid_rush_hour_state):
    return get_values(valid_rush_hour_state=valid_rush_hour_state, heuristic_used=4)[-1]


def get_values(valid_rush_hour_state, heuristic_used: int):
    if heuristic_used == 1:
        h = get_h1(rush_hour=valid_rush_hour_state['rushHour'])
    g = len(valid_rush_hour_state['vehicleInfo'])
    f = h + g
    return h, g, f


def compare_boards(board1: list[list], board2: list[list]):
    for index in range(len(board1)):
        if not functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, board1[index], board2[index]), True):
            return False
    return True
