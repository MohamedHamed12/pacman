# search.py
# ---------

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from extend_util import get_path
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    start_state = problem.getStartState()
    frontier = util.Stack()  # Store (state, action) pairs
    frontier.push((start_state, None))  
    visited = set()  # Initialize the set of visited states
    parent = {}  # Store parent states for reconstructing the path
    
    while not frontier.isEmpty():
        state, _ = frontier.pop()
        visited.add(state)
        if problem.isGoalState(state):
            path, total_cost = get_path(state,parent)
            return path

        for new_state, new_action, cost in problem.getSuccessors(state):
            if new_state not in visited:
                frontier.push((new_state, new_action))
                parent[new_state] = (state, new_action, cost)



def breadthFirstSearch(problem: SearchProblem):
    start_state = problem.getStartState()
    queue = util.Queue()  # Store (state, action) pairs
    queue.push((start_state, None))  # Store (state, action) pairs
    visited = set()  # Initialize the set of visited states
    parent = {}  # Store parent states for reconstructing the path
    visited.add(start_state)

    while not queue.isEmpty():
        state, _ = queue.pop()


        if problem.isGoalState(state):
            path, total_cost = get_path(state,parent)
            return path

        for new_state, new_action, cost in problem.getSuccessors(state):
            if new_state not in visited:
                queue.push((new_state, new_action))
                parent[new_state] = (state, new_action, cost)
                visited.add(new_state)


def uniformCostSearch(problem: SearchProblem):
    frontier =util.PriorityQueueWithFunction(lambda x: x[1])
    explored = set()
    parent={}
    start_state = problem.getStartState()
    frontier.push((start_state, 0))

    while not frontier.isEmpty():
        current_state , current_cost= frontier.pop()
     

        if  problem.isGoalState(current_state):
            path, total_cost = get_path(current_state,parent)
            return path

        explored.add(current_state)
        for new_state, new_action, new_cost in problem.getSuccessors(current_state):
            if new_state  in explored:continue
            total_cost = current_cost + new_cost
            frontier.push((new_state, total_cost))
            parent[new_state] = (current_state, new_action, new_cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    frontier = util.PriorityQueueWithFunction(lambda x: x[1])
    explored = set()
    parent = {}

    start = problem.getStartState()
    
    frontier.push((start, 0))

    while not frontier.isEmpty():
        current_state, current_cost = frontier.pop()

        if problem.isGoalState(current_state):
            path, total_cost = get_path(current_state, parent)
            return path

        explored.add(current_state)

        for new_state, new_action, new_cost in problem.getSuccessors(current_state):
            if new_state in explored:
                continue
            total_cost = current_cost + new_cost
            heuristic_cost = heuristic(new_state, problem)
            frontier.push((new_state, total_cost+heuristic_cost))
            explored.add(new_state)
            parent[new_state] = (current_state, new_action, new_cost)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

