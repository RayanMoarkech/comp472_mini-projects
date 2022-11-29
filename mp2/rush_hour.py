import string
from enum import Enum
import copy

class Move(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Rotation(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


# RushHour class
class RushHour:
    def __init__(self, board, vehicles):
        # A 2D list of the board
        self.board: list[list] = board
        # An array of vehicles
        self.vehicles: list[Vehicle] = vehicles

    # Takes in the vehicle name
    # Returns the vehicle object
    def get_vehicle(self, vehicle_name):
        for vehicle in self.vehicles:
            if vehicle.name == vehicle_name:
                return vehicle

    def is_free_at(self, x, y) -> bool:
        # print(x)
        # print(y)
        if x <= -1 or y <= -1 or x >= 6 or y >= 6:
            return False
        return self.board[y][x] == '.'

    # Takes in the move: Move enum, distance: int, vehicle_name: string
    def move_vehicle(self, move, distance, vehicle_name):
        vehicle = self.get_vehicle(vehicle_name=vehicle_name)
        rotation = vehicle.get_rotation()
        is_free = False

        # Check if there is any vehicle on the road
        if move == Move.UP and rotation == Rotation.VERTICAL:
            # Logic to move up
            back = vehicle.get_back()
            for index in range(distance):
                is_free = self.is_free_at(x=back.x, y=(back.y - index - 1))
                if not is_free:
                    # print("Cannot move up")
                    return False
        elif move == Move.DOWN and rotation == Rotation.VERTICAL:
            # Logic to move down
            front = vehicle.get_front()
            for index in range(distance):
                is_free = self.is_free_at(x=front.x, y=(front.y + index + 1))
                if not is_free:
                    # print("Cannot move down")
                    return False
        elif move == Move.LEFT and rotation == Rotation.HORIZONTAL:
            # Logic to move left
            back = vehicle.get_back()
            for index in range(distance):
                is_free = self.is_free_at(x=(back.x - index - 1), y=back.y)
                if not is_free:
                    # print("Cannot move left")
                    return False
        elif move == Move.RIGHT and rotation == Rotation.HORIZONTAL:
            # Logic to move right
            front = vehicle.get_front()
            for index in range(distance):
                is_free = self.is_free_at(x=(front.x + index + 1), y=front.y)
                if not is_free:
                    # print("Cannot move right")
                    return False

        if not is_free:
            # print("Cannot move")
            return False

        # Replace the vehicle position with . in the board
        for position in vehicle.positions:
            self.board[position.y][position.x] = "."

        # Move the vehicle
        # print("Can move")
        vehicle.move(move=move, distance=distance)

        # Register the new vehicle positions in the board
        for position in vehicle.positions:
            self.board[position.y][position.x] = vehicle_name
        
        return True


    def get_all_next_valid_states(self):
        valid_states = []
        for vehicle in self.vehicles:
            for move in Move:
                for i in range(1, 5):
                    new_rush_hour = copy.deepcopy(self)
                    valid_move = new_rush_hour.move_vehicle(move, i, vehicle.name)
                    if (valid_move):
                        valid_states.append(new_rush_hour)
        return valid_states

    # Checks if the position of the vehicle A is at the solvable position
    def valid_A(self):
        vehicle = self.get_vehicle("A")
        return vehicle.get_rotation() == Rotation.HORIZONTAL and vehicle.positions[0].y == 2
    
    def solved(self):
        return self.board[2][5] == "A"


# Vehicle class
class Vehicle:
    def __init__(self, name, positions, fuel_limit):
        # The name of the vehicle
        self.name: string = name
        # The size of the car (size of the positions)
        self.size: int = len(positions)
        # An array of positions
        self.positions: list[Position] = positions
        # Set default fuel to 100
        self.fuel_limit = fuel_limit

    def get_rotation(self) -> Rotation:
        if self.positions[0].x == self.positions[1].x:
            return Rotation.VERTICAL
        return Rotation.HORIZONTAL

    # Returns the front position
    # If the vehicle is horizontal, it returns the right-most position index
    # If the vehicle is vertical, it returns the down-most position index
    def get_front(self):
        rotation = self.get_rotation()
        if rotation == Rotation.HORIZONTAL:
            front = self.positions[0]
            for position in self.positions:
                if front.x < position.x:
                    front = position
        else:
            front = self.positions[0]
            for position in self.positions:
                if front.y < position.y:
                    front = position
        return front

    # Returns the back position
    # If the vehicle is horizontal, it returns the left-most position index
    # If the vehicle is vertical, it returns the up-most position index
    def get_back(self):
        rotation = self.get_rotation()
        if rotation == Rotation.HORIZONTAL:
            back = self.positions[0]
            for position in self.positions:
                if back.x > position.x:
                    back = position
        else:
            back = self.positions[0]
            for position in self.positions:
                if back.y > position.y:
                    back = position
        return back

    def add_position(self, position):
        self.positions.append(position)
        self.size += 1

    # Takes in the move: Move enum, distance: int
    def move(self, move, distance):
        rotation = self.get_rotation()
        if move == Move.UP and rotation == Rotation.VERTICAL:
            # Logic to move up
            for position in self.positions:
                position.y -= distance
            self.fuel_limit -= 1
        elif move == Move.DOWN and rotation == Rotation.VERTICAL:
            # Logic to move down
            for position in self.positions:
                position.y += distance
            self.fuel_limit -= 1
        elif move == Move.LEFT and rotation == Rotation.HORIZONTAL:
            # Logic to move left
            for position in self.positions:
                position.x -= distance
            self.fuel_limit -= 1
        elif move == Move.RIGHT and rotation == Rotation.HORIZONTAL:
            # Logic to move right
            for position in self.positions:
                position.x += distance
            self.fuel_limit -= 1


# Position class
class Position:
    def __init__(self, x, y):
        # x position
        self.x = x
        # y position
        self.y = y
