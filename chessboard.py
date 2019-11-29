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
    return rules.listeDesPieces('N')[::-1] + [[None] * 8] * 4 + rules.listeDesPieces('B')




#==============================================================================
# Vérification déplacement dans la zone
#==============================================================================


#print("‎• or <>")











