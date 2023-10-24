from extend_util import CustomPriorityQueue

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
            print("Total cost: ",total_cost)
            return path

        explored.add(current_state)
        for new_state, new_action, new_cost in problem.getSuccessors(current_state):
            if new_state  in explored:continue
            total_cost = current_cost + new_cost
            frontier.push(new_state, total_cost)
            parent[new_state] = (current_state, new_action, new_cost)
           

 
def get_path(cur_state,parent):
    total_cost = 0
    path = []
    while cur_state in parent:
        cur_state, action , cost = parent[cur_state]
        path.append(action)  
        total_cost += cost
    return path[::-1],total_cost