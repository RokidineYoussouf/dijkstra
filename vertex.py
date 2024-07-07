import sys
class Vertex:
    def __init__(self, info):
        self.info = info
        self.arcs = []
        self.visited = False;
        self.predecesseur = -1
        self.distance = 0
        
    def get_info(self):
        return self.info
    
    def get_name(self):
        return self.info[0]
    
    def get_longitude(self):
        return self.info[1]
    
    def get_latitude(self):
        return self.info[2]
    
    
    def get_arcs(self):
        return self.arcs
    
    def get_arc(self, id_sommet):
        if self.arcs[id_sommet] ==-1:
            return -999999
        return self.arcs[id_sommet]
    
    def are_visited(self):
        return self.visited
    
    def get_voisin(self):
        voisin = []
        for id_sommet in range(len(self.arcs)):
            if self.arcs[id_sommet] !=float(-1):
                voisin.append(id_sommet)
        return voisin
    
    def get_predecesseur(self):
        return self.predecesseur
    
    def get_distance(self):
        return self.distance
    
    def set_info(self, info):
        self.info = info
    
    def set_arcs(self, arcs):
        self.arcs = arcs
        
    def add_arc(self, arc):
        self.arcs.append(arc)
    
    def set_visited(self, visited):
        self.visited = visited
        
    def set_predecesseur(self, id_sommet):
        self.predecesseur = id_sommet
    
    def set_distance(self, distance):
        self.distance =distance
    