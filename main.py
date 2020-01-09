"""

"""


from chessboard import Echiquier
from rules import Piece
# =============================================================================
# Gestion de l'interface - boucle du moteur
# =============================================================================


echiquier = Echiquier()
#echiquier.afficher()


# =============================================================================
# Fonctions
# =============================================================================

def estUneCoordonnee(string):
    if not type(string) == str:
        return False
    
    if not len(string) == 2:
        return False
    
    if not string[0] in 'ABCDEFGH':
        return False
    
    if not string[1] in '12345678':
        return False
    
    return True

def testCouleur(position):
    index = echiquier.nomCaseToIndex(position)
    piece = echiquier.get_piece(index)
    
    return  piece.couleur

    
# =============================================================================
#  Fonction Pour Jouer
# =============================================================================
    
#tourDuJoueur
def tourDuJoueur (couleur):
    liste_aide_joueur = {1 : (
                      "Pour jouer", 
                      [
                       "jouer [coordonnées départ] [coordonnées arrivée]", 
                       "[coordonnées départ] [coordonnées arrivée]"
                       ]
                      ), 
                 2 : (
                      "Pour connaitre les coups possibles", 
                      ["coups"]
                      ),
                 3 : (
                      "Pour connaitre la liste des coups possibles d'une piece", 
                      ["piece"]
                     ),
                 4 : (
                      "Pour afficher l'échiquier", 
                      ["afficher"]
                      ),
                 5 : (
                      "Pour afficher l'échiquier avec les coups possibles d'une piece", 
                      ["afficher [coordonnées]"]
                     )
                 }
    
    aide_joueur = "\n".join(
                    [str(numero) 
                    + " - " 
                    + liste_aide_joueur[numero][0] 
                    + ", entrez : " 
                    + " ou ".join(liste_aide_joueur[numero][1]) 
                    + " ou " 
                    + str(numero) 
                    + [" [coordonnées départ] [coordonnées arrivée]" if numero == 1 else ""][0]
                       + [" [coordonnées]" if numero == 3 else ""][0]
                       + [" [coordonnées]" if numero == 5 else ""][0] for numero in liste_aide_joueur.keys()]
                   ) + "\n\n"
    
    str_ne_plus_afficher_laide = "Pour ne plus afficher l'aide, entrez : fin aide\n\n"
    str_afficher_laide = "Pour afficher l'aide, entrez : aide\n\n"
    ne_plus_afficher_laide = False
    
    while True:
            
        if ne_plus_afficher_laide:
            entree_joueur = input(str_afficher_laide)
        else:
            entree_joueur = input(aide_joueur + str_ne_plus_afficher_laide)
        
        #ne plus afficher l'aide
        if entree_joueur == 'fin aide':
            ne_plus_afficher_laide = True
    #        elif entree_
        
        if entree_joueur in ['Brest', 'Megademon',  'Les vielles']:
            print('\n'*3 + 'Vous venez de quitter la partie.')
            return ''
    
        elif len(entree_joueur) == 0:
            pass
        
        # 2 - "Pour connaitre les pièces pouvant bouger"
        elif entree_joueur in liste_aide_joueur[2][1] + ['2']:
            
            print(echiquier.listePiecesPouvantEtreDeplaceesFormatCase(couleur))
                
        
        # 3 - "Pour connaitre la liste des coups possibles d'une piece"
        elif entree_joueur[:-3] in liste_aide_joueur[3][1] + ['3']:
            if testCouleur(entree_joueur[-2:])!= couleur:
                print("Case invalide")
            elif estUneCoordonnee(entree_joueur[-2:]):
                print(echiquier.listeCoupsPossiblesFormatCase(entree_joueur[-2:]))
                
            
        # 4 - "Pour afficher l'échiquier"
        elif entree_joueur in liste_aide_joueur[4][1] + ['4']:
            
            echiquier.afficher()
        
        # 5 - "Pour afficher l'échiquier avec les coups possibles d'une piece"
        elif entree_joueur[:-3] in liste_aide_joueur[5][1] + ['5']:
            if estUneCoordonnee(entree_joueur[-2:]):
                if testCouleur(entree_joueur[-2:])!= couleur:
                    print("Case invalide")
                else:
                    echiquier.afficherCoupsPossibles(entree_joueur[-2:])
            
    
        # 1 - si il veut jouer 
        elif entree_joueur[:-6] in [element[:-43] for element in liste_aide_joueur[1][1]] + ['1']:
            deplacement(entree_joueur , couleur )
            break 
       
    
    
#Programme     
def deplacement(entree_joueur,couleur):
    valeurDeplacement = entree_joueur[-5:]
    while True :
       #on teste si l'entrée est bien un couple de coordonné
        if  (estUneCoordonnee(valeurDeplacement[:2]) and estUneCoordonnee(valeurDeplacement[-2:])) and valeurDeplacement[2] == ' ' : 
            #on teste si la pièce est de la bonne couleurJ
            if testCouleur(valeurDeplacement[:2]) == couleur:
                #on teste si la case a une pièce de la bonne couleur
                if  valeurDeplacement[:2] in echiquier.listePiecesPouvantEtreDeplaceesFormatCase(couleur) :
                    #On teste si la case d'arrivé est valide
                    if valeurDeplacement[-2:] in echiquier.listeCoupsPossiblesFormatCase(valeurDeplacement[:2]) :
                       
                        echiquier.deplacerPiece(valeurDeplacement[:2], valeurDeplacement[-2:])
                        
                        break
                    else:
                        print('La pièce ne peut pas ce déplacer sur cette case')
                else:
                    print('La pièce ne peut pas bouger')
            else:
                print("La pièce choisie n'est pas " + couleur )
        else: 
            print("Entrée invalide, entrez un déplacement valide")
        
        valeurDeplacement = input('')[-5:]


def tourIA(couleur):
    pass

#==============================================================================
# Fonctions de JcJ ou JcIA
#==============================================================================
    



def jouerEnModeJcIA():
    
    entree_joueur = input('blanc ou noir')
    
    if entree_joueur == 'blanc' :
        for numero_du_tour in range(50):
            
            #-- le joueur joue --
            tourDuJoueur('blanc')
            if echiquier.isEchecEtMatBlanc():
                print("Vous avez gagné" )
                break
            echiquier.afficher()
            
            #-- l'ordinateur joue --
            tourIA('noir')
            if echiquier.isEchecEtMatNoir():
                print("Défaite" )
                break
            
            
    elif entree_joueur == 'noir' :
        for numero_du_tour in range(50):
            
            #-- l'ordinateurr joue --
            tourIA('blanc')
            if echiquier.isEchecEtMat():
                print("Vous avez gagné" )
                break
            echiquier.afficher()
            
            #-- le joueur joue --
            tourDuJoueur('noir')
            if echiquier.isEchecEtMat():
                print("Défaite" )
                break
        
        
            
# =============================================================================
#         """IA doit joué"""
# =============================================================================
        
        
        
        
        
    
    #verification de fin de partie
    
    
    #-- l'IA joue --
    #déplacement d'une piece
    
    
    #vérification de la fin de partie
    

def jouerEnModeJcJ():
    
    echiquier.afficher()
       

    for numero_du_tour in range(50):
        
        #-- le joueur joue --
         
        #qu'est-ce qu'il veut faire ?
        print("C'est au joueur blanc de jouer" )
        tourDuJoueur('blanc')
        echiquier.afficher()
        
        
        if echiquier.isEchecEtMatBlanc():
            print("Les blancs ont gagné" )
            break
        
            
        print("C'est au joueur noir de jouer" )
        tourDuJoueur('noir')
        echiquier.afficher()    
            
        if echiquier.isEchecEtMatNoir():
            print("Les noirs ont gagné" )
            break
        
        
        

            
            
            
            


modeDeJeu = input("Voulez vous jouez contre L'ordinateur (entrer : JcIA) ou contre un joueur (entrer : JcJ) ?\n\n")
if modeDeJeu == "JcJ":
    jouerEnModeJcJ()

elif modeDeJeu == "JcIA":
    jouerEnModeJcIA()
                    
            




#==============================================================================
# Appel de l'échiquier
#==============================================================================

echiquier = Echiquier()
#
#print(echiquier.listeCoupsPossiblesFormatCase('C7'))
#print(echiquier.listeCoupsPossiblesFormatCase('B7'))
#
##echiquier.afficherCoupsPossibles('D7')
#
#echiquier.deplacerPiece('A2', 'A3')
#echiquier.afficher()
#
#echiquier.deplacerPiece('C2', 'E4')
#echiquier.afficher() 
#
#echiquier.afficherCoupsPossibles('E4')
#
##print(echiquier.listeDeplacementsPossibles('A6'))
#
##print(echiquier.isEchecEtMat())
##print(echiquier.couleurEchecEtMat())



#==============================================================================
# Appel de l'IA
#==============================================================================

#
#couleur = 'noir'
##
##
#ia = IA(echiquier, 'noir')
#
#print(ia.meilleurMouvement(echiquier, couleur))
#
#possibilites = ia.nMeilleursMouvementsPoints(5)
#







#while not echiquier.isEchecEtMat():
#    
#    #au joueur blanc de déplacer une pièce
#    
#    #à l'IA de jouer
#
#    pass

#une fois la boucle finie


# =============================================================================
# Fonctions du main
# =============================================================================



#
#Fait jusqu'à présent (liste pas a jour) :
#    - classe Echiquier et classe Piece
#    - définition des pieces
#    - initialisation de l'échiquier
#    - gestion des déplacements dans l'échiquier
#    - vérification de l'échec et mat
#    
#À faire bientôt :
#    - déplacements possibles (fait pour pion dans Piece() mais pas les autres 
#           et ensuite compléter listeDeplacementsPossibles dans Echiquier())
#    - affichage des déplacements possibles
#
























