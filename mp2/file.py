from collections import defaultdict
from rush_hour import RushHour, Vehicle, Position

import os
import random


# Get all the RushHour games from a file
# RushHour game = boards and fuel limits
# Returns a list of RushHour objects
def get_games(filename: str) -> list[RushHour]:
    lines = get_file_lines(filename=filename)
    return generate_games(lines=lines)


# Generates a random rush hour games
# Returns a list RushHour objects
def generate_random_games(count: int) -> list[RushHour]:
    lines = []
    for index in range(count):
        line = get_random_line()
        lines.append(line)
    return generate_games(lines=lines)


# Returns a random line of the rush hour board and fuel
# 1 line string
def get_random_line() -> str:
    vehicle_list = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    board_line = 36 * ['.']

    ambulance_front = 11 + random.randint(1, 5)
    board_line[ambulance_front] = 'A'
    board_line[ambulance_front + 1] = 'A'

    fuel_line = ''

    # Add dots everywhere
    for index, char in enumerate(board_line):
        # Break if all vehicle used
        if not vehicle_list:
            break
        # Skip already created
        if char != '.':
            continue
        # 1/11 chance to skip
        if random.randint(1, 11) == 1:
            continue
        # Get a vehicle
        vehicle_to_use = random.choice(vehicle_list)
        vehicle_list.remove(vehicle_to_use)
        # Get random size
        size = random.randint(2, 3)
        # Create horizontal vehicle: 1/2 chance
        if random.randint(1, 2) == 1 or index > 29:
            fits = True
            # Check if the vehicle fits
            multipliyer = int(index / 6)
            if not multipliyer * 6 <= index + size < (multipliyer + 1) * 6:
                # vehicle_list.append(vehicle_to_use)  # Insert back the vehicle
                fits = False
            # Check if place is taken
            if fits:
                for x in range(size):
                    if board_line[index + x] != '.':
                        fits = False
                        break
            # Insert vehicle
            if fits:
                for x in range(size):
                    board_line[index + x] = vehicle_to_use
                continue
        # Create vertical vehicle: 1/2 chance or if not fitting in horizontal
        # Check if vehicle fits
        multipliyer = int(index / 6)
        if not multipliyer + size < 6:
            vehicle_list.append(vehicle_to_use)  # Insert back the vehicle
            continue
        # Check if place is taken
        taken = False
        for x in range(size):
            if board_line[index + (x * 6)] != '.':
                taken = True
                break
        if taken:
            continue
        # Insert vehicle
        for x in range(size):
            board_line[index + (x * 6)] = vehicle_to_use

        # Create fuel restriction: 1/4 chance
        if random.randint(1, 4) == 1:
            fuel = random.randint(0, 99)
            fuel_line += vehicle_to_use + str(fuel) + ' '

    return ''.join(board_line) + ' ' + fuel_line


# Prints the board 2D list to console
# Takes in a 2D list board
def print_board(board: list[list]):
    for y in range(len(board)):
        for x in range(len(board[y])):
            print(board[y][x], end=' ')
        print()
    print()


# Get the Lines from a file
# Returns a list of strings (lines)
def get_file_lines(filename):
    file1 = open(file=filename, mode='r')
    return file1.readlines()


# Generate boards from the lines of a file
# Returns a list of RushHour objects
def generate_games(lines) -> list[RushHour]:
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


# Adds a line string to the input file
def write_to_input_file(line: str):
    input_path = os.path.join('metadata', 'input')
    if not os.path.exists(input_path):
        os.makedirs(input_path)
    file = open(os.path.join(input_path, 'input.txt'), 'a')
    file.write('%s\n' % line)
    file.close()


# Write to Search file
# Takes in the file_name, the write mode (initial should be 'w' then all appends should be 'a'),
# the f(n) value, the g(n) value, the h(n) value, the rush_hour object,
# and a list of the moved vehicle info ['A99', 'M99']
def write_search_file(file_name: str, mode: str, f: int, g: int, h: int, rush_hour: RushHour,
                      moved_vehicle_info: list[str]):
    output_path = os.path.join('metadata', 'output')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    file = open(os.path.join(output_path, file_name), mode)
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
    output_path = os.path.join('metadata', 'output')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    file = open(os.path.join(output_path, file_name), 'w')

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
