#Dijkstra's algorithm

costs = {'start':0, 'A':6, 'B':2, 'fin' : None}

graph = {'start': {'A':6, 'B':2},'A':{'fin':1},'B':{'A':3,'fin':5}, 'fin':{}}

parents = {'A':'start', 'B':'start'}

#Workflow:
#1. find the cheapest node
#2. check f there is a cheaper path to the neighbours of this node
#3. repeat until you have done this for every node in the graph
#4. calculate the final path

# current_node = 'start'
# queue = ['A','B']
#if there's still something left in the queue, look for any child nodes; add these to the queue if they've not been added before
#for children of current node, if cost < (costs[current_node] + costs[child], update costs to graph['current_node']['child'], update parents
#repeat until there's nothing left in the queue
#calculate the distance starting from the end point and moving backwards along the parents dictionary

def dijkstra(current_node = 'start'):
    queue = list(graph[current_node])
    seen = [current_node]+list(graph[current_node])
    while queue:
        current_node = queue.pop(0)
        print('current_node='+str(current_node))
        for i in list(graph[current_node]): #add children to the queue if they haven't previously been added
            if i not in seen:
                queue.append(i)
                seen.append(i)
                print('adding '+ str(list(graph[current_node])) + ' to the queue')
                print(seen)
        for child in list(graph[current_node]): #calculate whether there is a cheaper way to reach the children of the current node
            if costs[child] == None or costs[child]<(costs[current_node]+costs[child]):
                costs[child] = graph[current_node][child] + costs[current_node]
                print('updating cost of ' + str(child) + ' to ' + str(graph[current_node][child] + costs[current_node]))
                parents[child] = current_node
                print('updating parent of ' + str(child) + ' to ' + str(current_node))