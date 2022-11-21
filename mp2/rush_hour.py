# RushHour class

class RushHour:
    def __init__(self, board, vehicles, fuel_limits):
        # A 2D list of the board
        self.board = board
        # A set of vehicles
        self.vehicles = vehicles
        # A dictionary with the fuel limits
        self.fuel_limits = fuel_limits
