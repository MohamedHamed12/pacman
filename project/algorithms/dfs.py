
from search import SearchProblem
from extend_util import CustomStack, get_path
import util

def dfs_recursive(problem: SearchProblem):
    """
    Perform depth-first search recursively to find a path in the given problem.

    Args:
        problem (SearchProblem): The problem to be solved.

    Returns:
        List: The path from the start state to the goal state.
    """
    visited  = set()  # Set to keep track of visited states
    path = []  # List to store the path from start to goal state

    def dfs_helper(state)-> bool:
        """
        Recursive helper function for depth-first search.

        Args:
            state: The current state to explore.

        Returns:
            bool: True if goal state is found, False otherwise.
        """

        for new_state , action, cost in problem.getSuccessors(state):
            if new_state  in visited :continue
            visited.add(new_state)
            path.append(action)

            if problem.isGoalState(new_state): return True    
            if dfs_helper(new_state):  return True

            path.pop()

        return False

    dfs_helper(problem.getStartState())
    return path




def dfs_stack(problem ) -> list:
    """
    breadth-first search algorithm to find a valid path in a problem.

    Args:
        problem: The problem to solve.

    Returns:
        The valid path found.
    """
    start_state = problem.getStartState()
    queue = CustomStack([(start_state, None)])  # Store (state, action) pairs
    visited = set()  # Initialize the set of visited states
    parent = {}  # Store parent states for reconstructing the path
    
    while queue.size()>0:
        state, _ = queue.pop()


        visited.add(state)
        if problem.isGoalState(state):
            path, total_cost = get_path(state,parent)
            return path

        for new_state, new_action, cost in problem.getSuccessors(state):
            if new_state not in visited:
                queue.push((new_state, new_action))
                parent[new_state] = (state, new_action, cost)