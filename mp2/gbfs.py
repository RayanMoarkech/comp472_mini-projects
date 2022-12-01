from rush_hour import RushHour
from priority_queue import PriorityQueue
from heuristics import get_h1, get_h2, get_h3, get_h4
from file import write_search_file, write_solution_file
import time

# def greedy_bfs(initial_state, h):
#     pritority_queue = PriorityQueue()
#     closed: list[any] = []
#     # Add the initial state to the queue
#     pritority_queue.push(item=initial_state, node_list=[], priority=h(initial_state['rushHour']))
#     node = pritority_queue._queue[0]
#     closed.append(node[2])
#     # node[0] = 0
#     # node[1] = index
#     # node[2] = {'rideHour': RushHour, 'vehicleName': str}
#     # node[3] = []
#     # while not node[2]['rushHour'].solved():
#     while pritority_queue._queue:
#         node = pritority_queue._queue[0]
#         pritority_queue.pop()

#         if node[2]['rushHour'].solved():
#             break

#         print(node[0], end=" ")
#         for line in node[2]['rushHour'].board:
#             for el in line:
#                 print(el, end="")
#         for node_visited in node[3]:
#             print(" ", node_visited, end="")
#         print()
#         # Get all the next valid states
#         # TODO: pass all the old vehicle info
#         valid_states = node[2]['rushHour'].get_all_next_valid_states([])
#         for state in valid_states:
#             if visited(closed, state) == False:
#                 closed.append(state)
#                 vehicle_name = state['vehicleName']
#                 fuel_limit = state['rushHour'].get_vehicle(vehicle_name).fuel_limit
#                 nodes_visited = node[3].copy()
#                 nodes_visited.insert(0, vehicle_name + str(fuel_limit))
#                 pritority_queue.push(item=state, node_list=nodes_visited, priority=h(state['rushHour']))
#     if node[2]['rushHour'].solved():
#         print("SOLVED")
#     else:
#         print("NOT SOLVED")   

def greedy_bfs(rush_hours: list[RushHour], heuristic_used: int):

    # assign heuristic function
    heuristics = [get_h1, get_h2, get_h3, get_h4]
    h = heuristics[heuristic_used - 1]

    for index, rush_hour in enumerate(rush_hours):

        # file names
        search_file_name = 'gbfs-h' + str(heuristic_used) + '-search' + '-' + str(index+1) + '.txt'
        solution_file_name = 'gbfs-h' + str(heuristic_used) + '-sol' + '-' + str(index+1) + '.txt'

        # get heuristic value of initial state
        initial_heuristic = h(rush_hour)
        
        # Init config
        start_time = time.time()
        search_path_length = 0

        # create open and closed list
        open = PriorityQueue()
        closed: list[any] = []

        # Change initial state game to dict, to match format of next valid states
        intitial_state_dict = {
            'rushHour': rush_hour,
            'vehicleName': "",
            'vehicleInfo': "",
            'vehicleMove': "",
            'vehicleDistance': "",
            'vehicleFuel': [],
            'history': []
        }

        # Add the initial state to the open list
        open.push(item=intitial_state_dict, node_list=[], priority=h(rush_hour))

        # add intial state to closed list
        node = open._queue[0]
        closed.append(intitial_state_dict)
        # node[0] = heuristic
        # node[1] = index
        # node[2] = rush hour dict
        # node[3] = []
        while open._queue:
            node = open._queue[0]

            if node[2]['rushHour'].solved():
                break

            print(node[0], end=" ")
            for line in rush_hour.board:
                for el in line:
                    print(el, end="")
            for node_visited in node[3]:
                print(" ", node_visited, end="")
            print()

            heuristic = node[0]
            write_search_file(file_name=search_file_name, mode='a', f=0, g=1, h=heuristic,
                              rush_hour=node[2]['rushHour'],
                              moved_vehicle_info=node[2]['vehicleInfo'])

            # Get all the next valid states
            # TODO: pass all the old vehicle info
            valid_states = node[2]['rushHour'].get_all_next_valid_states(history=node[2])
            open.pop()
            search_path_length += len(valid_states)
            for state in valid_states:
                if visited(closed, state) == False:
                    closed.append(state)
                    vehicle_name = state['vehicleName']
                    fuel_limit = state['rushHour'].get_vehicle(vehicle_name).fuel_limit
                    nodes_visited = node[3].copy()
                    nodes_visited.insert(0, vehicle_name + str(fuel_limit))
                    open.push(item=state, node_list=nodes_visited, priority=h(state['rushHour']))
        if node[2]['rushHour'].solved():
            print("SOLVED")
        else:
            print("CANNOT SOLVE")
        runtime = time.time() - start_time

        if open._queue:
            final_state = open._queue[0][2]
        else:
            final_state = {}
        # Write solution summary to file
        write_solution_file(file_name=solution_file_name, initial_game=rush_hour, final_state=final_state,
                            runtime=runtime, search_path_length=search_path_length)   

def visited(closed_list, rush_hour_compare):
    for rush_hour in closed_list:
        if rush_hour['rushHour'].board == rush_hour_compare['rushHour'].board:
            return True
    return False
