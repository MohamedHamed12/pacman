
from search import SearchProblem
from util import Stack, Queue
class CustomStack(Stack):
    def peek(self):
        return self.list[-1]
    def contains(self, item):
        return item in self.list
    def size(self):
        return len(self.list)
    def get_item(self,idx):
        return self.list[idx]