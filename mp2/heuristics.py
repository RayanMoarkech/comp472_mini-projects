from rush_hour import RushHour


# Gets the heuristic h2 of a rush hour game
# Takes in RushHour object
# Returns the heuristic value
def get_h2(rush_hour: RushHour):
    ambulance = rush_hour.get_vehicle("A")
    front = ambulance.get_front()
    heuristic = 0
    for x in range(front.x + 1, 6):
        if not rush_hour.board[front.y][x] == '.':
            heuristic += 1
    return heuristic
