from rush_hour import RushHour
from priority_queue import PriorityQueue

def greedy_bfs(initial_state, h):
    pritority_queue = PriorityQueue()
    closed: list[any] = []
    # Add the initial state to the queue
    pritority_queue.push(item=initial_state, node_list=[], priority=h(initial_state['rushHour']))
    node = pritority_queue._queue[0]
    closed.append(node[2])
    # node[0] = 0
    # node[1] = index
    # node[2] = {'rideHour': RushHour, 'vehicleName': str}
    # node[3] = []
    # while not node[2]['rushHour'].solved():
    while pritority_queue._queue:
        node = pritority_queue._queue[0]
        pritority_queue.pop()

        if node[2]['rushHour'].solved():
            break

        print(node[0], end=" ")
        for line in node[2]['rushHour'].board:
            for el in line:
                print(el, end="")
        for node_visited in node[3]:
            print(" ", node_visited, end="")
        print()
        # Get all the next valid states
        # TODO: pass all the old vehicle info
        valid_states = node[2]['rushHour'].get_all_next_valid_states([])
        for state in valid_states:
            if visited(closed, state) == False:
                closed.append(state)
                vehicle_name = state['vehicleName']
                fuel_limit = state['rushHour'].get_vehicle(vehicle_name).fuel_limit
                nodes_visited = node[3].copy()
                nodes_visited.insert(0, vehicle_name + str(fuel_limit))
                pritority_queue.push(item=state, node_list=nodes_visited, priority=h(state['rushHour']))
            # pritority_queue.sort()
        # for state in pritority_queue._queue:
        #     print("push: ", end=" ")
        #     print(state[0], end=" ")
        #     for line in state[2]['rushHour'].board:
        #         for el in line:
        #             print(el, end="")
        #     for node_visited in state[3]:
        #         print(" ", node_visited, end="")
        #     print()
    if node[2]['rushHour'].solved():
        print("SOLVED")
    else:
        print("NOT SOLVED")   

def visited(closed_list, rush_hour_2):
    for rush_hour in closed_list:
        if rush_hour['rushHour'].board == rush_hour_2['rushHour'].board:
            return True
    return False
