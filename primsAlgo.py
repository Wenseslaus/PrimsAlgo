# Wenseslaus Raphael Prime Algorithm Solution

# Set the maximum value to be infinity
maximum = float('inf')

# Total number of vertices on my_graph
V = 7

# Given graph in adacency matrix
my_graph = [[0, 28, 0, 0, 0, 10, 0],
            [28, 0, 26, 0, 0, 0, 14],
            [0, 16, 0, 12, 0, 0, 0],
            [0, 0, 12, 0, 22, 0, 18],
            [0, 0, 0, 22, 0, 25, 24],
            [10, 0, 0, 0, 25, 0, 0],
            [0, 14, 0, 18, 24, 0, 0],]



def primsAlgo(my_graph):
    seen_vertices = [0, 0, 0, 0, 0, 0, 0] # an array to track the seen_vertices as we loop
    starting_edge = 0 # Set the starting point of the edge to be 0
    seen_vertices[0] = True # Now we are setting the seen_vertices to be starting from 0

    while (starting_edge < V - 1):
        p = 0
        q = 0
        maximum_val = maximum
        # Find the adjacent vertices and look for the minimum weight,
        # But if the vertex already exist in the list then continue, else
        # Choose another vertex near and make it seen
        for i in range(V):
            if seen_vertices[i]:
                for j in range(V):
                    if ((not seen_vertices[j]) and my_graph[i][j]):  
                        if maximum_val > my_graph[i][j]:
                            maximum_val = my_graph[i][j]
                            p = i # Make the weight become the new vertix
                            q = j

        # Print out the solution in order
        print("Vertex " + str(p) + "-" + str(q) + " " + "Edge " + str(my_graph[p][q]))
        seen_vertices[q] = True # Change the seen value to true
        starting_edge += 1 # Increment the starting edge by one

primsAlgo(my_graph)