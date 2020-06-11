import heapq as hq

def shortest_path(M,start,goal):

    import heapq as hq
    
    if start == goal:
        return [start]
    
    def euclidean(node1, node2):
        x0, y0 = M.intersections[node1]
        x1, y1 = M.intersections[node2]
        return ((x0-x1) ** 2 + (y0-y1) ** 2) ** (1/2)
    
    frontier = []
    hq.heappush(frontier, (euclidean(start, goal), 0, start))
    explored = dict({start:(0, None)})
    done = set()

    def recursion():
        if not frontier:
            return -1

        f, g, current = hq.heappop(frontier)

        if explored[current][0] != g:
            recursion()

        if current == goal:
            return #reconstruct path
        done.add(current)

        for node in M.roads[current]:
            if node in done:
                continue
            
            g = g + euclidean(current, node)
            f = g + euclidean(node, goal)

            if node in explored and explored[node][0] <= g:
                continue

            hq.heappush(frontier, (f, g, node))
            print("updating key",node)
            explored.update({node: (g, current)})
            print("the length of the dictionary is", len(explored))

        return recursion()


    if recursion() is -1:
        pass
        #print("No path between the two nodes exists.")
    path = [goal]
    node = goal
    while explored[node][1] in explored:
        path = [explored[node][1]] + path
        node = explored[node][1]
        
    return(path)
            
            
            