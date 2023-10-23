
import heapq
from search import SearchProblem
from util import PriorityQueue, Stack, Queue
class CustomStack(Stack):
    def __init__(self,lst):
        self.list = lst
    def peek(self):
        return self.list[-1]
    def contains(self, item):
        return item in self.list
    def size(self):
        return len(self.list)
    def get_item(self,idx):
        return self.list[idx]

class CustomQueue(Queue):
    def __init__(self,lst):
        self.list = lst
        

    def size(self):
        return len(self.list)



import heapq
class CustomPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        priority, item = heapq.heappop(self.heap)
        return (item, priority)

    def size(self):
        return len(self.heap)
   