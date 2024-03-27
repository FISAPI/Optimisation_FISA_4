import math

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = {}

    def add_edge(self, v1, v2, weight):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][v2] = weight
            self.vertices[v2][v1] = weight

    def remove_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            del self.vertices[vertex_id]
            for v in self.vertices.values():
                if vertex_id in v:
                    del v[vertex_id]

    def remove_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v1 in self.vertices[v2] and v2 in self.vertices[v1]:
                del self.vertices[v1][v2]
                del self.vertices[v2][v1]

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return list(self.vertices[vertex_id].keys())
        else:
            return []

    def get_edge_weight(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v1 in self.vertices[v2] and v2 in self.vertices[v1]:
                return self.vertices[v1][v2]
            else:
                return None
        else:
            return None


