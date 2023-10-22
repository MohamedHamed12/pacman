
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






# def dfs_stack(problem):
#     """
#     Depth-first search algorithm to find a valid path in a problem.

#     Args:
#         problem: The problem to solve.

#     Returns:
#         The valid path found.
#     """
#     stack=CustomStack()
#     stack.push(problem.getStartState())
#     visited = set()  # Initialize the set of visited states
#     path = CustomStack()
#     path.push(None)

#     while stack:
#         state = stack.peek()
#         if state in visited:
#             stack.pop()
#             path.pop()  
#             continue

#         visited.add(state)  
#         if problem.isGoalState(state):
#             break

#         for new_state, new_action, cost in problem.getSuccessors(state):
#             if  new_state in visited or stack.contains(new_state) :
#                 continue
#             stack.push(new_state)  
#             path.push(new_action) 

#     ans = [path.get_item(i) for i in range(1, stack.size()) if stack.get_item(i) in visited]  # Retrieve the valid path
#     # print(len(ans))
#     return ans




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
    visited.add(start_state)
    
    while queue.size()>0:
        state, _ = queue.pop()


        if problem.isGoalState(state):
            path, total_cost = get_path(state,parent)
            return path

        for new_state, new_action, cost in problem.getSuccessors(state):
            if new_state not in visited:
                queue.push((new_state, new_action))
                parent[new_state] = (state, new_action, cost)
                visited.add(new_state)
   
