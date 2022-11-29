from rush_hour import RushHour
from priority_queue import PriorityQueue


def greedy_bfs(rush_hour: RushHour, h):
    pritority_queue = PriorityQueue()
    # Add the initial state to the queue
    pritority_queue.push(rush_hour, h(rush_hour))
    for i in range(3):
    # while not rush_hour.solved():
        # Get the next state
        rush_hour = pritority_queue.pop()
        # Get all the next valid states
        valid_states = rush_hour.get_all_next_valid_states()
        # Add the valid states to the queue
        for state in valid_states:
            pritority_queue.push(state, h(state))
    for el in pritority_queue._queue:
        print("Heuristic: ", el[0])
        print("Priority: ", el[1])
        for line in el[2].board:
            for el in line:
                print(el, end=" ")
            print()
        print()