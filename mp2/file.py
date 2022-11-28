from collections import defaultdict
from rush_hour import RushHour, Vehicle, Position


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
        rush_hour_game = RushHour(board=board, vehicles=vehicles)
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
    index = 0
    # Loop through characters after the board
    for char in line[36:]:
        if 'A' <= char <= 'Z':
            fuel_limits[char] = line[index + 1]
            index += 1
        else:
            continue
    # Create a defaultdict that returns the default_fuel_limit if key does not exist
    fuel_limits = defaultdict(lambda: default_fuel_limit, fuel_limits)
    return fuel_limits
