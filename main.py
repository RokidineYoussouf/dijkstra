from parserA import *
from vertex import *
from dijkstra import Dijkstra
from connex import *
from a_Star import A_Star

#On crée un graph composée de sommet et d'arc
def creer_graph(sommets, arcs):
    return (sommets, arcs)

#On récupère les sommets du fichier
def initialiser_sommet(fichier):
    info_sommets= parse_csv(fichier)
    sommets = []
    for info in info_sommets:
        sommets.append(Vertex(info))
    return sommets

#On récupère les arcs du fichier et on leur donne à leur sommet 
def initiliser_arcs_sommet(sommets, fichier_arc):
    arcs = parse_adjacency_matrix(fichier_arc)
    i = 0
    for arc in arcs:
        sommets[i].set_arcs(arc)
        i = i+1
    return (sommets, arcs)


sommets = initialiser_sommet("input/coordinates.csv")
g = initiliser_arcs_sommet(sommets, "input/adjacency_matrix.txt")

#g = (sommets, arcs)
d = Dijkstra(g)

if estConnexe(g, 1)==True:
    print("Le graphe est connexe")
else:
    print("Le graphe n'est pas connexe")


a_star = A_Star(g, 3,1)

chemin_a_star= a_star.chemin()

chemin = d.plus_court_chemin(3, 1)
tab = [None, None]
print("---------------------CHEMIN DISJKTRA---------------------------")
for sommet in chemin[0]:
    print(sommet.get_info())
print("cout :",chemin[1])

print("---------------------CHEMIN A STAR---------------------------")
for sommet in chemin_a_star[0]:
    print(sommet.get_info())
print("cout : ",chemin_a_star[1])
