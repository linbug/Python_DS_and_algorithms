#Dijkstra's algorithm

costs = {'start':0, 'A':6, 'B':2, 'fin' : float('inf')}

graph = {'start': {'A':6, 'B':2},'A':{'fin':1},'B':{'A':3,'fin':5}, 'fin':{}}

parents = {'start':None, 'A':'start', 'B':'start'}

#Workflow:
#1. find the cheapest node
#2. check if there is a cheaper path to the neighbours of this node. If so, update node costs and parent.
#3. repeat until you have done this for every node in the graph
#4. calculate the final path

def dijkstra(current_node = 'start'):
    '''runs dijkstra's algorithm'''
    processed = [current_node]                                  #keep track of nodes that have already been processed
    current_node = find_lowest_cost_node(costs, processed)      #find the lowest cost unprocessed node
    while current_node:                                         #while there are unprocessed nodes left
        print('current_node='+str(current_node))
        for child in list(graph[current_node]):                 #calculate whether there is a cheaper way to reach the children of the current node
            new_cost = costs[current_node] + graph[current_node][child]
            if costs[child]>new_cost:
                costs[child] = new_cost                         #if so, update the cost of that child
                print('updating cost of ' + str(child) + ' to ' + str(new_cost))
                parents[child] = current_node                   #and update the parent
                print('updating parent of ' + str(child) + ' to ' + str(current_node))
        processed.append(current_node)
        current_node = find_lowest_cost_node(costs, processed)
    return find_final_path(parents)

def find_lowest_cost_node(costs, processed):
    '''find the lowest cost node of the unprocessed nodes'''
    lowest_cost = float('inf')
    lowest_node = None
    for node in list(costs.keys()):
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_node = node
    return lowest_node

def find_final_path(parents):
    '''return the path between start and fin'''
    current_node = parents['fin']
    path = "-->fin"
    while current_node:
        path = '-->' + path
        path = str(current_node) + path
        current_node = parents[current_node]
    return path
