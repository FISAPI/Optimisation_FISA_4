import math


class Noeud:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristique(a, b, heuristique_choice=1):
    (x1, y1) = a
    (x2, y2) = b
    # Dans notre cas, on peut aussi utiliser la distance de Manhattan
    # return abs(x1 - x2) + abs(y1 - y2)
    # Ou a distance en ligne droite
    # return max(abs(x1 - x2), abs(y1 - y2))
    if heuristique_choice == 1 :
        return 0
    elif heuristique_choice == 2:
        return max(abs(x1 - x2), abs(y1 - y2))
    else:
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def a_star(graphe, depart, arrivee, heuristique_choice=1):
    noeud_depart = Noeud(depart)
    noeud_arrivee = Noeud(arrivee)
    noeud_depart.h = heuristique(noeud_depart.position, noeud_arrivee.position, heuristique_choice)
    noeud_depart.f = noeud_depart.h

    open_set = [noeud_depart]
    closed_set = set()

    while open_set:
        noeud_courant = min(open_set, key=lambda o: o.f)
        open_set.remove(noeud_courant)

        if noeud_courant.position == noeud_arrivee.position:
            chemin = []
            total_cost = noeud_courant.g  # Le coût total du chemin est le coût g du noeud d'arrivée
            while noeud_courant:
                chemin.append(noeud_courant.position)
                noeud_courant = noeud_courant.parent
            return chemin[::-1], total_cost  # Retourner le chemin et le coût total

        closed_set.add(noeud_courant.position)

        voisins = graphe.get_voisins(noeud_courant.position)
        for (voisin_position, cout) in voisins:
            if voisin_position in closed_set:
                continue
            
            noeud_voisin = Noeud(voisin_position, noeud_courant)

            tentative_g_score = noeud_courant.g + cout
            if tentative_g_score < noeud_voisin.g or noeud_voisin not in open_set:
                noeud_voisin.g = tentative_g_score
                noeud_voisin.h = heuristique(noeud_voisin.position, noeud_arrivee.position, heuristique_choice)
                noeud_voisin.f = noeud_voisin.g + noeud_voisin.h
                noeud_voisin.parent = noeud_courant

                if noeud_voisin not in open_set:
                    open_set.append(noeud_voisin)

    print("Aucun chemin trouvé")
    return None, None

# TODO: FAIRE L'ENREGISTREMENT DES CHEMINS DANS UN FICHIER