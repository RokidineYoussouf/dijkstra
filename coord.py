import math
#Classe coordonnées
class Coord:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    
    #Methode qui calcule la distance de Haversine
    def distance_haversine(self, coord):
      
        dLat = (coord.x - self.x) * math.pi / 180.0
        dLon = (coord.y - self.y) * math.pi / 180.0
      
        self.x = (self.x) * math.pi / 180.0
        coord.x = (coord.x) * math.pi / 180.0
      
        a = (pow(math.sin(dLat / 2), 2) + 
             pow(math.sin(dLon / 2), 2) * 
                 math.cos(self.x) * math.cos(coord.x)) 
        rad = 6371
        c = 2 * math.asin(math.sqrt(a)) 
        return rad * c

