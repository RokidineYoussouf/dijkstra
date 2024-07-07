from coord import Coord
class A_Star:
    def __init__(self, G, s, t):
        self.G = G
        self.s = s
        self.t = t
    #Méthode qui donne l'heuristique utilisé dans A Star
    def heuristic(self,s,t):
        sommetS = self.G[0][s]
        sommetT = self.G[0][t]
        point1 = Coord(sommetS.get_latitude(), sommetS.get_longitude(), sommetS.get_name())#On transforme le sommet en point
        point2 = Coord(sommetT.get_latitude(), sommetT.get_longitude(), sommetT.get_name())#On transforme le sommet en point
        return point1.distance_haversine(point2) #On utilise la distance de Haversine sur les deux points
    
    def extraire_le_min(self,F):
        return F.pop(0)
    
    def algo(self):
        F = []
        F.append(self.s)
        p = []
        closed_list = []
        g_score = []
        f_score = []
        
        for i in range(len(self.G[0])):
            p.append(-1)
            g_score.append(0)
            f_score.append(0)
            
        f_score[self.s] = g_score[self.s] + self.heuristic(self.s, self.t)
        while len(F) != 0:
            u = self.extraire_le_min(F)
            #u = F.pop(0)
            if u==self.t:
                return p,g_score[self.t]
            closed_list.append(u)
            for v in self.G[0][u].get_voisin():
                if v not in closed_list:
                    tentative_g_score = g_score[u] + self.G[0][u].get_arc(v)
                    if v not in F or tentative_g_score < g_score[v]:
                        p[v] = u
                        g_score[v] = tentative_g_score
                        f_score[v] = g_score[v] + self.heuristic(v, self.t)
                        if v not in F:
                            F.append(v)
        raise NameError('ERREUR')
        
    def chemin(self):
        result = self.algo()
        chemin = []
        for i in result[0]:
            chemin.append(self.G[0][i])
        return chemin,result[1]


            
        
        
    
    
    
