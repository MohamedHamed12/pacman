from extend_util import CustomPriorityQueue, get_path

def ucs(problem):
    frontier =CustomPriorityQueue()
    explored = set()
    parent={}
    start_state = problem.getStartState()
    frontier.push(start_state, 0)

    while frontier:
        current_state , current_cost= frontier.pop()
     

        if  problem.isGoalState(current_state):
            path, total_cost = get_path(current_state,parent)
            return path

        explored.add(current_state)
        for new_state, new_action, new_cost in problem.getSuccessors(current_state):
            if new_state  in explored:continue
            total_cost = current_cost + new_cost
            frontier.push(new_state, total_cost)
            parent[new_state] = (current_state, new_action, new_cost)
           

 
