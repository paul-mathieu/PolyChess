"""

"""


from chessboard import Echiquier
from ia import IA, Mouvement



# =============================================================================
# Gestion de l'interface - boucle du moteur
# =============================================================================


echiquier = Echiquier()
echiquier.afficher()

demande_au_joueur = "Que voulez-vous faire ?"
liste_aide_joueur = {1 : ("Pour jouer", ["jouer", ""]), 
                     2 : ("Pour connaitre les coups possibles", ["coups"]),
                     3 : ("Pour connaitre la liste des coups possibles d'une piece", ["piece"]),
                     4 : ("Pour afficher l'échiquier", ["afficher"]),
                     5 : ("Pour afficher l'échiquier avec les coups possibles d'une piece", ["afficher [coordonnées]"])}

aide_joueur = ""

for numero_du_tour in range(50):
    
    #-- le joueur joue --
     
    #qu'est-ce qu'il veut faire ?
    while True:
        
        #si il veut jouer
        if 
        
        #si il veut déplacer d'une piece
    
    
    
    #verification de fin de partie
    
    
    #-- l'IA joue --
    #déplacement d'une piece
    
    
    #vérification de la fin de partie

#==============================================================================
# Appel de l'échiquier
#==============================================================================


echiquier = Echiquier()
echiquier.afficher()

print(echiquier.listeCoupsPossiblesFormatCase('C7'))
print(echiquier.listeCoupsPossiblesFormatCase('B7'))

#echiquier.afficherCoupsPossibles('D7')

echiquier.deplacerPiece('A2', 'A3')
echiquier.afficher()

echiquier.deplacerPiece('C2', 'E4')
echiquier.afficher() 

echiquier.afficherCoupsPossibles('E4')

#print(echiquier.listeDeplacementsPossibles('A6'))

#print(echiquier.isEchecEtMat())
#print(echiquier.couleurEchecEtMat())







#==============================================================================
# Appel de l'IA
#==============================================================================

couleur = 'noir'
#
#
ia = IA(echiquier, 'noir')

print(ia.meilleurMouvement(echiquier, couleur))

possibilites = ia.nMeilleursMouvementsPoints(5)








#while not echiquier.isEchecEtMat():
#    
#    #au joueur blanc de déplacer une pièce
#    
#    #à l'IA de jouer
#
#    pass

#une fois la boucle finie






#
#Fait jusqu'à présent :
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

