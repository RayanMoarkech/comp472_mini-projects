import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    # def push(self, item, priority):
    #     heapq.heappush(self._queue, (priority, self._index, item))
    #     self._index += 1

    def push(self, item, node_list, priority):
        heapq.heappush(self._queue, (priority, self._index, item, node_list))
        self._index += 1

    def empty(self):
        return len(self._queue) == 0

    def pop(self):
        return heapq.heappop(self._queue)[-1]