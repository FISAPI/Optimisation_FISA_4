/*********************************************
 * OPL 22.1.1.0 Model
 * Author: aureh
 * Creation Date: 27 mars 2024 at 11:19:22
 *********************************************/
int nbNodes = ...; // Nombre de sommets dans le graphe
range Nodes = 1..nbNodes;
int s = ...; // Indice du sommet source
int t = ...; // Indice du sommet destination

tuple Arc {
    key int depart;
    key int fin;
    float cost;
}

{Arc} Arcs = ...; // Ensemble des arcs du graphe


// Déclaration des variables de décision
dvar boolean x[Nodes][Nodes]; // Variable de décision : 1 si l'arc fait partie du chemin le plus court, 0 sinon
//Contrainte de binarité 

// Déclaration des variables de distance
dvar float+ d[Nodes]; // Distance du sommet i à la source s

minimize sum(a in Arcs) a.cost * x[a.depart][a.fin]; // Minimiser la somme des coûts des arcs sélectionnés

subject to {

 // Contrainte de flux
    forall (i in Nodes : i != s && i != t)
        sum(j in Nodes : (i != j)) x[i][j] - sum(j in Nodes : (i != j)) x[j][i] == 0;

    // Contrainte de sortie de la source
    sum(j in Nodes : (j != s)) x[s][j] == 1;

    // Contrainte d'entrée dans la destination
    sum(i in Nodes : (i != t)) x[i][t] == 1;

}


 