#Fonction permettant de v√©rifier que le graphe est bien connexe
def explorer(G, s):# Cette fonction permet d'explorer les sommets du graphe
      s.set_visited(True) #Sommet visit√© est marqu√©
      for u in s.get_voisin(): # On visite le sommet voisin du sommet visit√©
          if G[0][u].are_visited()!=True: # Alors on marque √† nouveau le sommet voisin s'il n' √©tait pas visit√© et marqu√© pour eviter les re-parcours
          
              explorer(G, G[0][u]);
                   

def parcoursProfondeur(G, id_sommet):# On va explorer le graphe en faisant un parcours en profondeur
    if G[0][id_sommet].are_visited()!=True: #Si le sommet n'est pas explorÈ on va l'Èxplorer
        explorer(G, G[0][id_sommet])#On explore les sommets non-visiter
    
def estConnexe(G, id_sommet):#On va verifier que le graphe est connexe
    parcoursProfondeur(G, id_sommet)#On fait un parcours en profondeur
    count = 0 #compteur qui va compter le nombre de sommet visitÈs
    for s in G[0]:
        if s.are_visited()==True:
            count = count+1 # On compte les sommets visitÈs
    print(count)
    if count == len(G[0]):#On compare les sommets visitÈs et le nombre de sommet du graph
        return True #Vrai si le nombre de sommets est egale au nombre de sommets visitÈs
    
    return False #Faux sinon
    


        
        