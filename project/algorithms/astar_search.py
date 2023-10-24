from extend_util import  get_path
from util import PriorityQueueWithFunction
def astar_search(problem, heuristic_func):
    frontier = PriorityQueueWithFunction(lambda x: x[1])
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
            heuristic_cost = heuristic_func(new_state, problem)
            frontier.push((new_state, total_cost+heuristic_cost))
            explored.add(new_state)
            parent[new_state] = (current_state, new_action, new_cost)
    return None