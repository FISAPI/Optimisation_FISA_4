/*********************************************
 * OPL 22.1.1.0 Model
 * Author: fisapi
 * Creation Date: 23 avril 2024 at 10:22:19
 *********************************************/
// le nombre des villes
int n=...;
//les variables de décision
dvar float+ u[2..n];
dvar boolean x[1..n][1..n];
// le cout de transport
float cout[1..n][1..n]=...;
// la fonction bjectif
minimize sum(i in 1..n, j in 1..n)
x[i][j]cout[i][j];
//Les contraintes
subject to {
 entrer:
 forall (j in 1..n)
 sum(i in 1..n) x[i][j]==1;
 sortir:
 forall (i in 1..n)
 sum (j in 1..n) x[i][j]==1;
 //sous_tour:
 sous_tour:
 forall (i in 2..n,j in 2..n)
 u[i]-u[j]+(n-1)x[i][j]<=n-2;

 }