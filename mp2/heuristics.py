from rush_hour import RushHour, Rotation


# Gets the heuristic h1 of a rush hour game
# Takes in RushHour object
# Returns the heuristic value
def get_h1(rush_hour: RushHour) -> int:
    ambulance = rush_hour.get_vehicle("A")
    front = ambulance.get_front()
    heuristic = 0
    blocking_vehicle = ""
    for x in range(front.x + 1, 6):
        if rush_hour.board[front.y][x] != "." and rush_hour.board[front.y][x] != blocking_vehicle:
            blocking_vehicle = rush_hour.board[front.y][x]
            heuristic += 1
    return heuristic


# Gets the heuristic h2 of a rush hour game
# Takes in RushHour object
# Returns the heuristic value
def get_h2(rush_hour: RushHour) -> int:
    ambulance = rush_hour.get_vehicle("A")
    front = ambulance.get_front()
    heuristic = 0
    for x in range(front.x + 1, 6):
        if not rush_hour.board[front.y][x] == '.':
            heuristic += 1
    return heuristic


# Gets the heuristic h2 of a rush hour game
# Takes in RushHour object
# Returns the heuristic value
def get_h3(rush_hour: RushHour) -> int:
    multiplier = 5
    h = get_h1(rush_hour=rush_hour)
    h *= multiplier
    return h


# Gets the heuristic h4 of a rush hour game
# Takes in RushHour object
# Returns the heuristic value
# Distance between ambulance and exit
def get_h4(rush_hour: RushHour) -> int:
    ambulance = rush_hour.get_vehicle("A")
    front = ambulance.get_front()
    heuristic = 5 - front.x
    return heuristic

# cars blocking ambulance also blocked by cars
# heuristic increases if blocking car is blocked on one side and both sides
def get_h5(rush_hour: RushHour):
    ambulance = rush_hour.get_vehicle("A")
    front = ambulance.get_front()
    heuristic = 0
    blocking_vehicle = ""
    for x in range(front.x + 1, 6):
        if rush_hour.board[front.y][x] != "." and rush_hour.board[front.y][x] != blocking_vehicle:
            blocking_vehicle = rush_hour.board[front.y][x]
            heuristic += 1
            vehicle = rush_hour.get_vehicle(blocking_vehicle)
            if vehicle.get_rotation() == Rotation.HORIZONTAL:
                x_front = vehicle.get_front().x + 1
                x_behind = vehicle.get_back().x - 1
                _y = vehicle.get_front().y
                if  x_front >= 6 or rush_hour.board[_y][x_front] != ".":
                    heuristic +=1
                if x_behind < 0 or rush_hour.board[_y][x_behind] != ".":
                    heuristic +=1
            elif vehicle.get_rotation() == Rotation.VERTICAL:
                y_front = vehicle.get_front().y + 1
                y_behind = vehicle.get_back().y -1
                _x = vehicle.get_front().x
                if  y_front >= 6 or rush_hour.board[y_front][_x] != ".":
                    heuristic +=1
                if y_behind < 0 or rush_hour.board[y_behind][_x] != ".":
                    heuristic +=1
    return heuristic

# cars blocking ambulance also blocked by cars
# only increases heuristic if car is blocked on both sides
def get_h6(rush_hour: RushHour):
    ambulance = rush_hour.get_vehicle("A")
    front = ambulance.get_front()
    heuristic = 0
    blocking_vehicle = ""
    for x in range(front.x + 1, 6):
        if rush_hour.board[front.y][x] != "." and rush_hour.board[front.y][x] != blocking_vehicle:
            blocking_vehicle = rush_hour.board[front.y][x]
            heuristic += 1
            vehicle = rush_hour.get_vehicle(blocking_vehicle)

            if vehicle.get_rotation() == Rotation.HORIZONTAL:
                x_front = vehicle.get_front().x + 1
                x_behind = vehicle.get_back().x - 1
                _y = vehicle.get_front().y
                if  x_front < 6 and rush_hour.board[_y][x_front] != "." and x_behind >= 0 and rush_hour.board[_y][x_behind] != ".":
                    heuristic +=1
            elif vehicle.get_rotation() == Rotation.VERTICAL:
                y_front = vehicle.get_front().y + 1
                y_behind = vehicle.get_back().y -1
                _x = vehicle.get_front().x
                if  y_front < 6 and  rush_hour.board[y_front][_x] != "." and y_behind >= 0 and rush_hour.board[y_behind][_x] != ".":
                    heuristic +=1
    return heuristic