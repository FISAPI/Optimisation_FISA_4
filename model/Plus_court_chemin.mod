/*********************************************
 * OPL 22.1.1.0 Model
 * Author: fisapi
 * Creation Date: 27 mars 2024 at 11:19:22
 *********************************************/
int nbNodes = ...; // Nombre de sommets dans le graphe

tuple Node {
  key int x;
  key int y;
};

Node s = ...; // Indice du sommet source
Node t = ...; // Indice du sommet destination


tuple Arc {
    key Node depart;
    key Node fin;
    float cost;
}

{Node} Nodes = ...;

{Arc} Arcs = ...; // Ensemble des arcs du graphe


// Déclaration des variables de décision
dvar boolean d[Arcs]; // Variable de décision : 1 si l'arc fait partie du chemin le plus court, 0 sinon
//Contrainte de binarité 


minimize sum(a in Arcs) a.cost * d[a]; // Minimiser la somme des coûts des arcs sélectionnés

subject to {

 // Contrainte de flux
    forall (i in Nodes : i != s && i != t)
        sum(j in Arcs : (i == j.depart)) d[j] - sum(j in Arcs : (i == j.fin)) d[j] == 0;

    // Contrainte de sortie de la source
    //sum(j in Nodes : (j != s)) d[<s, j>] == 1;
    sum(a in Arcs : (a.depart == s)) d[a] == 1;
    sum(a in Arcs : (a.fin == s)) d[a] == 0;

    // Contrainte d'entrée dans la destination
    //sum(i in Nodes : (i != t)) d[<i, t>] == 1;
    sum(a in Arcs : (a.fin == t)) d[a] == 1;
    sum(a in Arcs : (a.depart == t)) d[a] == 0;

}