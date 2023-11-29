
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



# example usage
G = Graph()

a = G.insert_vertex('a')
b = G.insert_vertex('b')
c = G.insert_vertex('c')
d = G.insert_vertex('d')

G.insert_edge(a, b)
G.insert_edge(b, c)
G.insert_edge(c, a)
G.insert_edge(c, d)

# search G starting from a
vertex = find_high_degree(G, a)  # should return vertex c

