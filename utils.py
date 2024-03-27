import math
import Graph


def create_graph_from_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        line = file.readline().strip().split(' ')
        n, m = int(line[0]), int(line[1])
        for i in range(n):
            line = file.readline().strip().split(' ')
            for j in range(m):
                if line[j] == '1':
                    graph.add_vertex((i, j))
                elif line[j] == '2':
                    graph.add_vertex((i, j))
                    start = (i, j)
                elif line[j] == '3':
                    graph.add_vertex((i, j))
                    end = (i, j)
        for i in range(n):
            for j in range(m):
                if (i, j) in graph.vertices:
                    if i > 0 and (i-1, j) in graph.vertices:
                        graph.add_edge((i, j), (i-1, j), 1)
                    if i < n-1 and (i+1, j) in graph.vertices:
                        graph.add_edge((i, j), (i+1, j), 1)
                    if j > 0 and (i, j-1) in graph.vertices:
                        graph.add_edge((i, j), (i, j-1), 1)
                    if j < m-1 and (i, j+1) in graph.vertices:
                        graph.add_edge((i, j), (i, j+1), 1)
                    if i > 0 and j > 0 and (i-1, j-1) in graph.vertices:
                        graph.add_edge((i, j), (i-1, j-1), math.sqrt(2))
                    if i > 0 and j < m-1 and (i-1, j+1) in graph.vertices:
                        graph.add_edge((i, j), (i-1, j+1), math.sqrt(2))
                    if i < n-1 and j > 0 and (i+1, j-1) in graph.vertices:
                        graph.add_edge((i, j), (i+1, j-1), math.sqrt(2))
                    if i < n-1 and j < m-1 and (i+1, j+1) in graph.vertices:
                        graph.add_edge((i, j), (i+1, j+1), math.sqrt(2))
    return graph, start, end