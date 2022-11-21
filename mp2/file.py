from collections import defaultdict
from rush_hour import RushHour


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
        board, vehicles = create_board(line=line)
        # Get the fuel limits dictionary
        fuel_limits = get_fuel_limits(line=line, default_fuel_limit=100)
        # Add the created game to the list of games
        rush_hour_game = RushHour(board=board, vehicles=vehicles, fuel_limits=fuel_limits)
        games.append(rush_hour_game)
    return games


# Create a board based on the line
# Returns a 2D list representation of the board and a set of vehicles that exists in the board
def create_board(line):
    board = [[], [], [], [], [], []]
    vehicles = set()
    index = 0
    # Create the board
    for char in line:
        if 'A' <= char <= 'Z' or char == '.':
            y = int(index/6)
            board[y].append(char)
            vehicles.add(char)
            index += 1
        elif index >= 36:
            break
        else:
            raise Exception("Incorrect format file")
    return board, vehicles


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
