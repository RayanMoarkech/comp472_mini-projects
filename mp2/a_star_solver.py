from rush_hour import RushHour
from heuristics import get_h1
from file import write_search_file


def main(rush_hour: RushHour, heuristic_used: int):
    # Get heuristic
    if heuristic_used == 1:
        heuristic = get_h1(rush_hour=rush_hour)

    # Search file name
    file_name = 'a-h' + str(heuristic_used) + '-search' + '-1.txt'

    # Print initial board
    write_search_file(file_name=file_name, mode='w', f=1, g=0, h=1, rush_hour=rush_hour)

    # Get all valid states
    valid_rush_hour_states = rush_hour.get_all_next_valid_states()

    # Print all possible rush hours states
    for valid_rush_hour in valid_rush_hour_states:
        write_search_file(file_name=file_name, mode='a', f=1, g=0, h=1, rush_hour=valid_rush_hour['rushHour'],
                          moved_vehicle_name=valid_rush_hour['vehicleName'])

