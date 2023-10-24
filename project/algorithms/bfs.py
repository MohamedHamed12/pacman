from extend_util import CustomQueue, get_path

def bfs_queue(problem ) -> list:
    """
    breadth-first search algorithm to find a valid path in a problem.

    Args:
        problem: The problem to solve.

    Returns:
        The valid path found.
    """
    start_state = problem.getStartState()
    queue = CustomQueue([(start_state, None)])  # Store (state, action) pairs
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