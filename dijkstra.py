import sys
class Dijkstra:
    def __init__(self, graphe):
        self.graphe = graphe
    
    #Méthode qui initialise les sommets
    def initialisation(self,id_sommet_depart):
        count = 0 #initialisation du compteur qui permettra de parcourir notre graphe
        for sommet in self.graphe[0]: #Ici on parcours les sommets de notre graphe
            if count == id_sommet_depart:# on compare le sommet de départ à la valeur actuel du compteur
                sommet.set_distance(0) #on arrete de parcourir les chemins  du graphe
            else:
                sommet.set_distance(sys.maxsize)#ici on peut continuer à parcourir le chemin
                
            count = count+1 #on incremente le compteur
    
    #Méthode qui calcule la distance minimale
    def distance_min(self,graphe):
        min = sys.maxsize#la plus petite distance parcourue jusqu'à présent
        id_sommet = -1 # L'identifiant du sommet qui a la plus petite distance
        count = 0
        
        for sommet in graphe:#on parcours les sommets de  notre graphe et on compare pour trouver le min
            if sommet != None:
                if sommet.get_distance()<min: #Si un sommet à une petite distance
                    min = sommet.get_distance() #On met à jour la distance minimal
                    id_sommet = count #On récupere l'identifiant du sommet
            count = count+1
        return id_sommet
    
    #Méthode qui met à jour la entre sommet1 et sommet2
    def maj_distance(self, id_sommet1, id_sommet2):
        sommets = self.graphe[0]
        poid_sommet1_sommet2 = sommets[id_sommet1].get_arc(id_sommet2)
        sommets[id_sommet1].get_distance()
        
        #On compare les deux sommet pour trouver le sommet qui a la plus petite distance et on met à jour si nécessaire
        if sommets[id_sommet1].get_distance() + poid_sommet1_sommet2 < sommets[id_sommet2].get_distance() :
            sommets[id_sommet2].set_distance(sommets[id_sommet1].get_distance() + poid_sommet1_sommet2)    
            sommets[id_sommet2].set_predecesseur(id_sommet1)
        
        
    #Méthode qui implementes l'algorithme de Dijkstra
    def dijkstra(self,sommet_depart): 
        self.initialisation(sommet_depart)
        sommet_non_parcouru = [] #On definit une liste vide des sommets  non parcouru
        sommet_non_parcouru = sommet_non_parcouru+self.graphe[0]
        while sommet_non_parcouru.count(None)!=len(self.graphe[0]): #tant qu'il reste des sommet non parcouru
            id_sommet1 = self.distance_min(sommet_non_parcouru) #On recupère le sommetqui a la plus petite distance
            if id_sommet1 == -1:
                break
            sommet1 = sommet_non_parcouru[id_sommet1] # ON récupère un sommet 
            sommet_non_parcouru[id_sommet1] = None #On supprime le sommet récuperé
            for id_sommet2 in sommet1.get_voisin(): #On parcours ces voisins
                self.maj_distance(id_sommet1, id_sommet2)
    
    #Méthode qui renvoie le plus court chemin
    def plus_court_chemin(self, id_sommet_depart, id_sommet_fin):
        self.dijkstra(id_sommet_depart)
        chemin = []
        sommet_depart = self.graphe[0][id_sommet_depart]
        sommet_fin = self.graphe[0][id_sommet_fin]
        cout = 0
        while sommet_fin.get_predecesseur()>-1: #On parcours tous les prédecesseur du sommet d'arrivé pour retrouver le chemin
            chemin.append(sommet_fin)
            id_pred = sommet_fin.get_predecesseur()
            sommet_pred = self.graphe[0][id_pred]
            sommet_fin = self.graphe[0][sommet_fin.get_predecesseur()]
            
            cout = cout + sommet_pred.get_arc(id_sommet_fin)
            id_sommet_fin = id_pred
        chemin.append(sommet_depart)
        
        return chemin,cout
       
    
    
    
    
    