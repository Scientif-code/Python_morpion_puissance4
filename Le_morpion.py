'Projet NSI1 - Morpion'

'Def 1'

def grille_vide() :
    '''
    renvoie une grille vide
    :param: none
    :return: (list)liste de listes contenant des 0
    :CU: none
    '''
    g=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    return(g)


'Def 2'

def affiche(g) :
    '''
    affiche une grille de morpion, avec le caractère "." pour une case vide,
    le caractère "X" pour le joueur 1 et le caractère "O" pour le joueur 2. affichage des lignes de haut en bas.
    :param g: (list) liste de listes d'entiers 0, 1 ou 2. 
    :return: (list) liste de listes de caractères
    :CU: grille de dimensions 3*3 (grille de morpion).
    '''
    for l in range (0,3):
        g2=""
        for c in range (0,3):
            if g[l][c] == 0:
                g2 = g2 + "."
            if g[l][c] == 1:
                g2 = g2 + "X"
            if g[l][c] == 2:
                g2 = g2 + "O"
        print(g2)
    return
    
    
'Def 3'

def coup_possible(g) :
    '''
    renvoie un booléen indiquant s'il est possible de jouer dans une position de la grille précise.
    :param g: (list) liste de liste d'entiers 0,1 et 2 et c:(int) 
    :return: (bool) renvoie True ou False 
    :CU: grille de dimensions 3*3 (grille de morpion).
    '''   
    if g[l][c] == 0:
        return True
    else :
        return False
            

'Def 5'

def horiz(g,j,l) :

    '''
    détermine s'il y a 3 croix ou ronds alignés horizontalement.
    :param g: (list) liste de liste d'entiers 0,1 et 2, j: (int), et l: (int)  
    :return: (bool) True ou False.
    :CU: grille de dimensions 3*3 (grille de morpion), l compris entre 0 et 1 et j = 1 ou 2.
    '''
    compteur = 0
    
    if g[l][0] == j :
        compteur+=1
    if g[l][1] == j :
        compteur+=1
    if g[l][2] == j :
        compteur+=1
    
    if compteur == 3 :
        return True
    else :
        return False

'Def 6'

def vert(g,j,c) :
    '''
    détermine s'il y a 3 ronds ou croix alignés verticalement.
    :param g: (list) liste de liste d'entiers 0,1 et 2, j: (int) et c:(int)  
    :return: (bool) True ou False.
    :CU: grille de dimensions 3*3 (grille de morpion), c compris entre 0 et 1 et j = 1 ou 2.
    ''' 
    compteur = 0
    
    if g[0][c] == j :
        compteur+=1
    if g[1][c] == j :
        compteur+=1
    if g[2][c] == j :
        compteur+=1

    if compteur == 3 :
        return True
    else :
        return False

'Def 7'

def diag(g,j) :           
    '''
    détermine s'il y a 3 pions alignés diagonalement.
    :param g: (list) liste de liste d'entiers 0,1 et 2, j: (int), l: (int) et c:(int)  
    :return: (bool) True ou False.
    :CU: grille de dimensions 3*3 (grille de morpion), l et c compris entre 0 et 1 et j = 1 ou 2.
    ''' 
    compteur = 0
    if g[0][0] == j :
        compteur+=1
    if g[1][1] == j :
        compteur+=1
    if g[2][2] == j :
        compteur+=1
        
    if compteur == 3 :
        return True
    
    compteur = 0
    if g[0][2] == j :
        compteur+=1
    if g[1][1] == j :
        compteur+=1
    if g[2][0] == j :
        compteur+=1

    if compteur == 3 :
        return True
    else :
        return False

'Def 8'

def victoire(g,j) :  
    '''
    renvoie un booléen si le joueur j a gagné.
    :param g: (list) liste de liste d'entiers 0,1 et 2 et j:(int) 
    :return: (bool) renvoie True ou False 
    :CU: grille de dimensions 3*3 (grille de morpion) et j = 1 ou 2  
    '''
    for l in range (0,3) :
        if horiz(g,j,l) :
            return True 
    for c in range (0,3) :        
        if vert(g,j,c) :       
            return True 
    if diag(g,j) :
        return True
    else :             # je retourne faux une fois après tout car au sinon ma fonction s'arrête.
        return False   # je veux que ma fonction teste toutes les possibilités.
                
                
'Def 9'

def match_nul(g) :
    '''
    renvoie un booléen indiquant s'il y a match nul, si la grille est remplie.
    :param g: (list) liste de liste d'entiers 0,1 et 2. 
    :return: (bool) renvoie True ou False 
    :CU: grille de dimensions 3*3 (grille de morpion) et pas de victoire constatée avant. 
    '''
    compteur = 0           
    for l in range(0,3) : # boucle for.
        for c in range(0,3) :
            if g[l][c]>0 :     # compteur qui augmente de 1 à chaque fois qu'il y a un pion des deux joueurs.
                compteur+=1      
            
    if compteur == 9 :     # si le compteur est à 9, la grille est remplie.     
        return True
    else :
        return False


def game_P_vs_C():
    '''
    fait jouer 1 joueur contre l'ordinateur, jusqu'à la victoire
    :param: none
    :return: none
    :CU: none
    '''
    
    #Areski
    
'Programme 2'
   
def game_P_vs_P():
    '''
    fait jouer 2 joueurs jusqu'à la victoire
    :param: none
    :return: none
    :CU: none
    '''
    
g = grille_vide()
affiche(g)
joueurs = [1,2]*5  # liste pour jouer à tour de rôle avec le joueur 1 qui commence.
for pos in range(len(joueurs)):  # boucle pour que la partie à tour de rôle fonctionne.
    j=joueurs[pos]  
    if not victoire(g,j) and not match_nul(g) :  # tant que la partie termine pas par une victoire ou un match nul.
         print ("joueur " + str(j))
         c = int(input("Quelle colonne voulez-vous jouer? (entier compris entre 0 et 2) : "))
         l = int(input("A quelle ligne voulez-vous jouer? (entier compris entre 0 et 2) : ")) # le joueur joue.
         while not coup_possible(g) :
             print("impossible, merci de rejouer !")
             print ("joueur " + str(j))
             affiche(g)
             c = int(input("Quelle colonne voulez-vous jouer? (entier compris entre 0 et 2) : "))
             l = int(input("A quelle ligne voulez-vous jouer? (entier compris entre 0 et 2) : ")) # le joueur joue. 
         g[l][c] = j
         affiche(g)             
         if victoire(g,1) :
             print("joueur 1 a gagné!")
             break
         if victoire(g,2) :
             print("joueur 2 a gagné!")
             break
         if match_nul(g) :
             print("Il y a match nul!")
             
