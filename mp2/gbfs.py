from rush_hour import RushHour

# def get_all_next_valid_states(rush_hour: RushHour):
#     valid_states = []
#     for vehicle in rush_hour.vehicles:
#         for move in [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]:
#             for i in range(1, 6):
#                 if rush_hour.is_valid_move(vehicle.name, move, i):
#                     new_rush_hour = copy.deepcopy(rush_hour)
#                     new_rush_hour.move_vehicle(move, i, vehicle.name)
#                     valid_states.append(new_rush_hour)
#     return valid_states