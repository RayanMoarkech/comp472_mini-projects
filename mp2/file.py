

# Get all the boards from a file
# Returns a list of boards
def get_boards(filename):
    lines = get_file_lines(filename=filename)
    return generate_boards(lines=lines)


# Get the Lines from a file
# Returns a list of strings (lines)
def get_file_lines(filename):
    file1 = open(file=filename, mode='r')
    return file1.readlines()


# Generate boards from the lines of a file
# Returns a list of boards
def generate_boards(lines):
    boards = []
    for line in lines:
        line = line.strip()
        # Skip if line is empty
        if not line:
            continue
        # Skip if line starts with #
        if line[0] == '#':
            continue
        # Create the board from a valid line
        board = create_board(line)
        # Add the created board to the list of boards
        boards.append(board)
    return boards


def create_board(line):
    board = []
    print(line)
    return board
