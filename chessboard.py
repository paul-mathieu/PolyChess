"""


"""

from functools import reduce
import rules

#==============================================================================
# Affichage
#==============================================================================


def afficherEchiquier(echiquier):

    lettres = reduce(lambda ele1, ele2 : ele1 + ele2, ["  " + element + "  " for element in ['A','B','C','D','E','F','G','H']])
    interlignes = "    " + reduce(lambda ele1, ele2 : ele1 + ele2, ["-" * 4 + " "] * 8)
    
    numLigne = 1
    
    
    print("   " + lettres)
    print(interlignes)
    
    for ligne in echiquier:
        
        print(str(numLigne), end = "  |")
        
        for element in ligne:
            
            if element != None:
                
                print(" " + element + " ", end = "|")
        
            else:
                
                print("    ", end = "|")
        
        
        print("  " + str(numLigne))
        
        print(interlignes)
        
        numLigne += 1
        
    print("   " + lettres)

    

#
#   A  B  C  D  E  F  G  H
#   -- -- -- -- -- -- -- --
#1 |  |  |  |  |  |  |  |  | 1
#   -- -- -- -- -- -- -- --
#2 |  |  |  |  |  |  |  |  | 2
#   -- -- -- -- -- -- -- --
#3 |  |  |  |  |  |  |  |  | 3
#   -- -- -- -- -- -- -- --
#4 |  |  |  |  |  |  |  |  | 4
#   -- -- -- -- -- -- -- --
#5 |  |  |  |  |  |  |  |  | 5
#   -- -- -- -- -- -- -- --
#6 |  |  |  |  |  |  |  |  | 6
#   -- -- -- -- -- -- -- --
#7 |  |  |  |  |  |  |  |  | 7
#   -- -- -- -- -- -- -- --
#8 |  |  |  |  |  |  |  |  | 8
#   -- -- -- -- -- -- -- --
#   A  B  C  D  E  F  G  H


#==============================================================================
# Initialisation
#==============================================================================


def echiquierVide():
    return [[None] * 8] * 8

def echiquierInitialise():
    return rules.listeDesPieces('N')[::-1] + [[' 1'] * 8] * 4 + rules.listeDesPieces('B')




#==============================================================================
# Déplacement
#==============================================================================

def deplacerPiece(echiquier, caseDepart, caseArrive):
    
    ec = echiquier
    
    ligDep, colDep = nomCaseToIndex(caseDepart)
    ligArr, colArr = nomCaseToIndex(caseArrive)
    
    print(str(ligDep) + "-" + str(colDep))
    print(str(ligArr) + "-" + str(colArr))

    valeur = echiquier[ligDep][colDep]
     
    ec[ligDep][colDep] = None  
    ec[ligArr][colArr] = valeur
    
#    print(echiquier)
    
    return echiquier

#==============================================================================
# Vérification déplacement dans la zone
#==============================================================================

def deplacementsPossibles(echiquier, piece):
    pass

def afficherDeplacementsPossibles(echiquier, piece):
    pass

#==============================================================================
# Autres fonctions
#==============================================================================

def nomCaseToIndex(nomCase):
    return int(nomCase[1]) - 1, ['A','B','C','D','E','F','G','H'].index(nomCase[0])

#print("‎• or <>")



ec = echiquierInitialise()
afficherEchiquier(ec)
afficherEchiquier(deplacerPiece(ec, "A7", "A5"))






