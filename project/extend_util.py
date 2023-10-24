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