
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
class CustomPriorityQueue(PriorityQueue):
 

    def pop(self):
        priority, self.count, item =heapq.heappop(self.heap )
        return (item, priority)

    def size(self):
        return len(self.heap)
    
    
def get_path(cur_state,parent):
    total_cost = 0
    path = []
    while cur_state in parent:
        assert cur_state  in parent, f"Error: {cur_state} is in parent"
        cur_state, action , cost = parent[cur_state]
        path.append(action)  
        total_cost += cost
    print(total_cost)
    return path[::-1],total_cost