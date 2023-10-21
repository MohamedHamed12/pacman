
from search import SearchProblem
from extend_util import CustomStack


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






def dfs_stack(problem):
    """
    Depth-first search algorithm to find a valid path in a problem.

    Args:
        problem: The problem to solve.

    Returns:
        The valid path found.
    """
    stack=CustomStack()
    stack.push(problem.getStartState())
    # stack = [problem.getStartState()]  # Initialize the stack with the start state
    visited = set()  # Initialize the set of visited states
    # path = [None]  # Initialize the path with None for the start state
    path = CustomStack()
    path.push(None)

    while stack:
        state = stack.peek()
        if state in visited:
            stack.pop()
            path.pop()  
            continue

        visited.add(state)  
        if problem.isGoalState(state):
            break

        for new_state, new_action, cost in problem.getSuccessors(state):
            if  new_state in visited or stack.contains(new_state) :
                continue
            stack.push(new_state)  
            path.push(new_action) 

    ans = [path.get_item(i) for i in range(1, stack.size()) if stack.get_item(i) in visited]  # Retrieve the valid path
    return ans