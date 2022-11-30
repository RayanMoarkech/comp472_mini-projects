from rush_hour import RushHour
from priority_queue import PriorityQueue


# def greedy_bfs(rush_hour, h):
#     pritority_queue = PriorityQueue()
#     # Add the initial state to the queue
#     pritority_queue.push(item=rush_hour, priority=h(rush_hour['rushHour']))
#     # for i in range(4):
#     while not rush_hour['rushHour'].solved():
#         # Get the next state
#         rush_hour = pritority_queue.pop()
#         node = ""
#         print("pop: ", end=" ")
#         print(h(rush_hour['rushHour']), end=" ")
#         for line in rush_hour['rushHour'].board:
#             for el in line:
#                 print(el, end="")
#         vehicle_name = rush_hour['vehicleName']
#         # print(" ", vehicle_name, end="")
#         if vehicle_name != '':
#             fuel_limit = rush_hour['rushHour'].get_vehicle(vehicle_name).fuel_limit
#             node = vehicle_name + str(fuel_limit)
#             print(" ", node, end="")
#         print()
#         # Get all the next valid states
#         valid_states = rush_hour['rushHour'].get_all_next_valid_states()
#         # Add the valid states to the queue
#         for state in valid_states:
#             pritority_queue.push(state, h(state['rushHour']))
#         # for state in pritority_queue._queue:
#         #     print(h(state[2]['rushHour']), end=" ")
#         #     for line in state[2]['rushHour'].board:
#         #         for el in line:
#         #             print(el, end="")
#         #     vehicle_name = state[2]['vehicleName']
#         #     print(" ", vehicle_name, end="")
#         #     fuel_limit = state[2]['rushHour'].get_vehicle(vehicle_name).fuel_limit
#         #     print(fuel_limit, end="")
#         #     print()

def greedy_bfs(initial_state, h):
    pritority_queue = PriorityQueue()
    # Add the initial state to the queue
    pritority_queue.push(item=initial_state, node_list=[], priority=h(initial_state['rushHour']))
    node = pritority_queue._queue[0]
    # node[0] = 0
    # node[1] = index
    # node[2] = {'rideHour': RushHour, 'vehicleName': str}
    # node[3] = []
    while not node[2]['rushHour'].solved():
        node = pritority_queue._queue[0]
        pritority_queue.pop()
        print(node[0], end=" ")
        for line in node[2]['rushHour'].board:
            for el in line:
                print(el, end="")
        for node_visited in node[3]:
            print(" ", node_visited, end="")
        print()
        # Get all the next valid states
        valid_states = node[2]['rushHour'].get_all_next_valid_states()
        for state in valid_states:
            vehicle_name = state['vehicleName']
            fuel_limit = state['rushHour'].get_vehicle(vehicle_name).fuel_limit
            nodes_visited = node[3].copy()
            nodes_visited.insert(0, vehicle_name + str(fuel_limit))
            pritority_queue.push(item=state, node_list=nodes_visited, priority=h(state['rushHour']))


