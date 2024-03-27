import math


class Graph:
    def __init__(self):
        self.aretes = {}
        self.sommet = {}
        self.n = 0
        self.m = 0
        self.reseau = [[0 for _ in range(self.m)] for _ in range(self.n)]

    def read_file(self, filename):
        with open(filename, 'r') as file:
            line = file.readline().strip().split(' ')
            self.n, self.m = int(line[0]), int(line[1])
            self.reseau = [[0 for _ in range(self.m)] for _ in range(self.n)]
            for i in range(self.n):
                line = file.readline().strip().split(' ')
                for j in range(self.m):
                    if line[j] == '1':
                        self.add_reseau_point(i, j, 1)
                    elif line[j] == '2':
                        self.add_reseau_point(i, j, 2)
                    elif line[j] == '3':
                        self.add_reseau_point(i, j, 3)
                    elif line[j] == "0":
                        self.add_reseau_point(i, j, 0)

    def add_reseau_point(self, i, j, nb):
        try:
            self.reseau[i][j] = nb
        except Exception as e:
            print(e)

    def display_reseau(self):
        for i in range(self.n):
            print(self.reseau[i])
            print("\n")


    # def add_reseau(self, reseau):
    #     self.reseau = reseau

    # def add_arete(self, arete_id):
    #     if arete_id not in self.aretes:
    #         self.aretes[arete_id] = {}
    #
    # def add_edge(self, v1, v2, weight):
    #     if v1 in self.aretes and v2 in self.aretes:
    #         self.aretes[v1][v2] = weight
    #         self.aretes[v2][v1] = weight
    #
    # def remove_arete(self, arete_id):
    #     if arete_id in self.aretes:
    #         del self.aretes[arete_id]
    #         for v in self.aretes.values():
    #             if arete_id in v:
    #                 del v[arete_id]
    #
    # def remove_edge(self, v1, v2):
    #     if v1 in self.aretes and v2 in self.aretes:
    #         if v1 in self.aretes[v2] and v2 in self.aretes[v1]:
    #             del self.aretes[v1][v2]
    #             del self.aretes[v2][v1]
    #
    # def get_aretes(self):
    #     return list(self.aretes.keys())
    #
    # def get_neighbors(self, arete_id):
    #     if arete_id in self.aretes:
    #         return list(self.aretes[arete_id].keys())
    #     else:
    #         return []
    #
    # def get_edge_weight(self, v1, v2):
    #     if v1 in self.aretes and v2 in self.aretes:
    #         if v1 in self.aretes[v2] and v2 in self.aretes[v1]:
    #             return self.aretes[v1][v2]
    #         else:
    #             return None
    #     else:
    #         return None
