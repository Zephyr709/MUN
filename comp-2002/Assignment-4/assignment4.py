# Jager Cooper, 201765344
from graph import Graph

def find_high_degree(graph, vertex):
    """
    Traverses the graph starting from vertex to look for high degree nodes.

    graph is an object of the Graph class.
    vertex is a vertex in the graph, and an object of the Vertex class.

    See algorithm find_high_degree() in the assignment instructions.

    Returns the vertex with the highest degree that was found during the
    traversal.
    """

    ## Question 1
    ## TO DO
    
    max = vertex
    visited = []
    n = getNeighbours(graph, vertex, visited)
    
    while len(n) > 0:
        v = n[0]
        
        #Find highest degree neighbour
        for neighbour in n:
            if graph.degree(neighbour) > graph.degree(v):
                v = neighbour

        # Move to and set v to visited
        visited.append(v)
        
        if graph.degree(v) > graph.degree(max):
            max = v
        
        n = getNeighbours(graph, vertex, visited)
        
    return max
            
            
    
    
    

def getNeighbours(graph, vertex, visitedList):
    neighbours = []
    
    for edge in graph.incident_edges(vertex):
        
        neighbour = edge.opposite(vertex)
        
        if neighbour not in visitedList:
            neighbours.append(neighbour)
    
    return neighbours
            
       
            


# example usage
G = Graph()

a = G.insert_vertex('a')
b = G.insert_vertex('b')
c = G.insert_vertex('c')
d = G.insert_vertex('d')
a1 = G.insert_vertex('a1')
b1 = G.insert_vertex('b1')
c1 = G.insert_vertex('c1')
d1 = G.insert_vertex('d1')


G.insert_edge(a, b)
G.insert_edge(b, c)
G.insert_edge(c, a)
G.insert_edge(c, d)
G.insert_edge(a1, b)
G.insert_edge(b, c1)
G.insert_edge(c1, a1)
G.insert_edge(c1, d1)
G.insert_edge(a, c1)
G.insert_edge(c, c1)


# search G starting from a
vertex = find_high_degree(G, c1)  # should return vertex c
print(vertex)
