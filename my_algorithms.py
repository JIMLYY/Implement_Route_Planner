from math import sqrt
from queue import Queue





def shortest_path(routes, start, goal):
    # we use a queue to conduct BFS on the map
    queue = Queue()
    
    # relation is a dictionary to remember the relationship between points 
    relation = {start: None}
    
    # length is a hash table to keep track of the points that we have visited 
    length = {start: 0}
    
    # put the first point into queue to initiate BFS
    queue.put(start)
    
    #BFS
    while not queue.empty():
        curr_point = queue.get()

        if curr_point == goal:
            getPath(relation, start, goal)
            
   
        for link_point in routes.roads[curr_point]:
            link_length = length[curr_point] + distance(routes.intersections[curr_point], routes.intersections[link_point])
            
            # make sure we won't get into infinite BFS and update the shortest path
            if link_point not in length or link_length < length[link_point]:
                length[link_point] = link_length
                queue.put(link_point)
                
                # remember the relationship between points 
                relation[link_point] = curr_point

    return getPath(relation, start, goal)

# helper function 1
def getPath(relation, start, goal):
    curr = goal
    shortest_Path = [curr]
    while curr != start:
        curr = relation[curr]
        shortest_Path.insert(0,curr)
    return shortest_Path

# helper function 2
def distance(point_1, point_2):
    x1,y1 = point_1[0], point_1[1]
    x2,y2 = point_2[0], point_2[1]
    square_dis = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return sqrt(square_dis)


