from collections import defaultdict
from rush_hour import RushHour, Vehicle, Position

import os


# Get all the RushHour games from a file
# RushHour game = boards and fuel limits
# Returns a list of RushHour objects
def get_games(filename):
    lines = get_file_lines(filename=filename)
    return generate_games(lines=lines)


# Get the Lines from a file
# Returns a list of strings (lines)
def get_file_lines(filename):
    file1 = open(file=filename, mode='r')
    return file1.readlines()


# Generate boards from the lines of a file
# Returns a list of RushHour objects
def generate_games(lines):
    games = []
    for line in lines:
        line = line.strip()
        # Skip if line is empty
        if not line:
            continue
        # Skip if line starts with #
        if line[0] == '#':
            continue
        # Create the board from a valid line
        board, vehicles_dict = create_board(line=line)
        # Get the fuel limits dictionary
        fuel_limits = get_fuel_limits(line=line, default_fuel_limit=100)
        # Create vehicles objects
        vehicles = create_vehicles(vehicles_dict=vehicles_dict, fuel_limits=fuel_limits)
        # Add the created game to the list of games
        rush_hour_game = RushHour(board=board, vehicles=vehicles, config_line=line)
        games.append(rush_hour_game)
    return games


# Create a board based on the line
# Returns a 2D list representation of the board and a dictionary with vehicle name as key and position list as value
def create_board(line):
    board = [[], [], [], [], [], []]
    vehicles_dict = {}  # Will store the vehicle name as key and position list as value
    index = 0
    # Create the board
    for char in line:
        if 'A' <= char <= 'Z' or char == '.':
            y = int(index / 6)
            x = index % 6
            # add the char in the board
            board[y].append(char)
            # add the char position to the vehicle dictionary
            if not char == '.':
                if char in vehicles_dict:
                    vehicles_dict[char].append(Position(x, y))
                else:
                    vehicles_dict[char] = [Position(x, y)]
            index += 1
        elif index >= 36:
            break
        else:
            raise Exception("Incorrect format file")
    return board, vehicles_dict


# Returns a list of vehicle objects
def create_vehicles(vehicles_dict, fuel_limits):
    vehicles = []
    for vehicle_name in vehicles_dict:
        vehicles.append(Vehicle(name=vehicle_name,
                                positions=vehicles_dict[vehicle_name],
                                fuel_limit=fuel_limits[vehicle_name]))
    return vehicles


# Get all the fuel limits
# Returns a dictionary
def get_fuel_limits(line, default_fuel_limit):
    fuel_limits = {}
    fuel_remaining_line = line[36:]
    # Loop through characters after the board
    for index, char in enumerate(fuel_remaining_line):
        if 'A' <= char <= 'Z':
            fuel_limits[char] = int(fuel_remaining_line[index + 1])
        else:
            continue
    # Create a defaultdict that returns the default_fuel_limit if key does not exist
    fuel_limits = defaultdict(lambda: default_fuel_limit, fuel_limits)
    return fuel_limits


# Write to Search file
# Takes in the file_name, the write mode (initial should be 'w' then all appends should be 'a'),
# the f(n) value, the g(n) value, the h(n) value, the rush_hour object,
# and a list of the moved vehicle info ['A99', 'M99']
def write_search_file(file_name: str, mode: str, f: int, g: int, h: int, rush_hour: RushHour,
                      moved_vehicle_info: list[str]):
    if not os.path.exists('output'):
        os.makedirs('output')
    file = open(os.path.join('output', file_name), mode)
    file.write('%s %s %s ' % (f, g, h))
    for y in range(len(rush_hour.board)):
        for x in range(len(rush_hour.board[y])):
            file.write(rush_hour.board[y][x])
    for moved_vehicle_info in moved_vehicle_info:
        file.write(' %s' % moved_vehicle_info)
    file.write('\n')
    file.close()


# Write the Solution file
# Takes in the file_name, the initial RushHour object, the final state dict (the one returned from valid states),
# the runtime value, and the search path length states value
def write_solution_file(file_name: str, initial_game: RushHour, final_state: dict, runtime: float,
                        search_path_length: int):
    if not os.path.exists('output'):
        os.makedirs('output')
    file = open(os.path.join('output', file_name), 'w')

    # Initial config
    file.write('--------------------------------------------------------------------------------\n')
    file.write('Initial board configuration:  %s\n' % initial_game.config_line)
    file.write('\n')

    # Initial board
    file.write('! %s\n' % initial_game.config_line[36:])
    for y in range(len(initial_game.board)):
        for x in range(len(initial_game.board[y])):
            file.write(initial_game.board[y][x])
        file.write('\n')
    file.write('\n')

    # Initial vehicle fuel availability
    file.write('Car fuel available: ')
    for vehicle in initial_game.vehicles:
        file.write('%s:%s ' % (vehicle.name, vehicle.fuel_limit))
    file.write('\n')
    file.write('\n')

    # Error if no solution
    if not final_state:
        file.write('Sorry, could not solve the puzzle as specified.\n')
        file.write('Error: no solution found\n')
        file.write('\n')

    # Results summary
    file.write('Runtime: %s seconds\n' % runtime)
    if final_state:
        file.write('Search path length: %s states\n' % search_path_length)
        file.write('Solution path length: %s moves\n' % len(final_state['vehicleInfo']))

        # Solution path summary
        file.write('Solution path: ')
        for history in final_state['history']:
            file.write('%s %s %s; ' % (history['vehicleName'], history['vehicleMove'], history['vehicleDistance']))
        file.write('%s %s %s; ' % (final_state['vehicleName'], final_state['vehicleMove'], final_state['vehicleDistance']))
        file.write('\n')
        file.write('\n')

        # Solution path
        for history in final_state['history']:
            file.write('%3s\t%6s\t%2s\t%8s\t%s\t' %
                       (history['vehicleName'], history['vehicleMove'], history['vehicleDistance'], history['vehicleFuel'],
                        history['rushHour'].get_one_liner_board()))
            for vehicle_info in history['vehicleInfo']:
                file.write('%s ' % vehicle_info)
            file.write('\n')
        file.write('%3s\t%6s\t%2s\t%8s\t%s\t' % (final_state['vehicleName'], final_state['vehicleMove'],
                                                 final_state['vehicleDistance'], final_state['vehicleFuel'],
                                                 final_state['rushHour'].get_one_liner_board()))
        for vehicle_info in final_state['vehicleInfo']:
            file.write('%s ' % vehicle_info)
        file.write('\n')
        file.write('\n')

        # Used car paths
        file.write('! ')
        for vehicle_info in final_state['vehicleInfo']:
            file.write('%s ' % vehicle_info)
        file.write('\n')

        # Final board
        for y in range(len(final_state['rushHour'].board)):
            for x in range(len(final_state['rushHour'].board[y])):
                file.write(final_state['rushHour'].board[y][x])
            file.write('\n')
        file.write('\n')

    file.write('--------------------------------------------------------------------------------\n')

    file.close()
