#Fonction permettant de vérifier que le graphe est bien connexe
def explorer(G, s):# Cette fonction permet d'explorer les sommets du graphe
      s.set_visited(True) #Sommet visité est marqué
      for u in s.get_voisin(): # On visite le sommet voisin du sommet visité
          if G[0][u].are_visited()!=True: # Alors on marque à nouveau le sommet voisin s'il n' était pas visité et marqué pour eviter les re-parcours
          
              explorer(G, G[0][u]);
                   

def parcoursProfondeur(G, id_sommet):# On va explorer le graphe en faisant un parcours en profondeur
    if G[0][id_sommet].are_visited()!=True: #Si le sommet n'est pas explor� on va l'�xplorer
        explorer(G, G[0][id_sommet])#On explore les sommets non-visiter
    
def estConnexe(G, id_sommet):#On va verifier que le graphe est connexe
    parcoursProfondeur(G, id_sommet)#On fait un parcours en profondeur
    count = 0 #compteur qui va compter le nombre de sommet visit�s
    for s in G[0]:
        if s.are_visited()==True:
            count = count+1 # On compte les sommets visit�s
    print(count)
    if count == len(G[0]):#On compare les sommets visit�s et le nombre de sommet du graph
        return True #Vrai si le nombre de sommets est egale au nombre de sommets visit�s
    
    return False #Faux sinon
    


        
        