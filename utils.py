import math
from Graph import Graph


def create_graph_from_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        line = file.readline().strip().split(' ')
        n, m = int(line[0]), int(line[1])
        for i in range(n):
            line = file.readline().strip().split(' ')
            for j in range(m):
                if line[j] == '1':
                    graph.add_arete((i, j))
                elif line[j] == '2':
                    graph.add_arete((i, j))
                    start = (i, j)
                elif line[j] == '3':
                    graph.add_arete((i, j))
                    end = (i, j)
        for i in range(n):
            for j in range(m):
                if (i, j) in graph.aretes:
                    if i > 0 and (i-1, j) in graph.aretes:
                        graph.add_edge((i, j), (i-1, j), 1)
                    if i < n-1 and (i+1, j) in graph.aretes:
                        graph.add_edge((i, j), (i+1, j), 1)
                    if j > 0 and (i, j-1) in graph.aretes:
                        graph.add_edge((i, j), (i, j-1), 1)
                    if j < m-1 and (i, j+1) in graph.aretes:
                        graph.add_edge((i, j), (i, j+1), 1)
                    if i > 0 and j > 0 and (i-1, j-1) in graph.aretes:
                        graph.add_edge((i, j), (i-1, j-1), math.sqrt(2))
                    if i > 0 and j < m-1 and (i-1, j+1) in graph.aretes:
                        graph.add_edge((i, j), (i-1, j+1), math.sqrt(2))
                    if i < n-1 and j > 0 and (i+1, j-1) in graph.aretes:
                        graph.add_edge((i, j), (i+1, j-1), math.sqrt(2))
                    if i < n-1 and j < m-1 and (i+1, j+1) in graph.aretes:
                        graph.add_edge((i, j), (i+1, j+1), math.sqrt(2))
    return graph, start, end


if __name__ == '__main__':
    graph = Graph()
    graph.read_file(filename='exos/reseau_5_10_1.txt')
    graph.display_reseau()
