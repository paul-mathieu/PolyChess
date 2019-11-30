"""


"""

from functools import reduce
from rules import Piece


class Echiquier:
        
    
    def __init__(self):
        self.positions = \
            [Piece('Tour', 'noir'), Piece('Cavalier', 'noir'), 
             Piece('Fou','noir'),
             Piece('Dame', 'noir'),Piece('Roi','noir'),
             Piece('Fou', 'noir'), 
             Piece('Cavalier', 'noir'), Piece('Tour', 'noir')] + \
                \
            [Piece('Pion', 'noir')] * 8 + \
                \
            [Piece()] * 8 * 4 + \
                \
            [Piece('Pion', 'blanc')] * 8 + \
                \
            [Piece('Tour', 'blanc'), Piece('Cavalier', 'blanc'), 
             Piece('Fou','blanc'),
             Piece('Dame','blanc'),Piece('Roi','blanc'),
             Piece('Fou','blanc'),
             Piece('Cavalier','blanc'),Piece('Tour','blanc')]
        
    #==============================================================================
    # Construction de l'échiquier
    #==============================================================================
    
    def coordonnees():
        return [lettre + str(chiffre) for chiffre in range(1,9) for lettre in ['A','B','C','D','E','F','G','H']]
    
    
    #==============================================================================
    # Affichage
    #==============================================================================
    
    
    def afficher(self):
    
        lettres = reduce(lambda ele1, ele2 : ele1 + ele2, ["  " + element + "  " for element in ['A','B','C','D','E','F','G','H']])
        interlignes = "    " + reduce(lambda ele1, ele2 : ele1 + ele2, ["-" * 4 + " "] * 8)
        
        numLigne = 1
        
        
        print("   " + lettres)
        print(interlignes)
        
        for ligne in self:
            
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
    # Déplacement
    #==============================================================================
    
    def deplacerPiece(echiquier, caseDepart, caseArrive):
        
        ec = echiquier
        
        ligDep, colDep = nomCaseToIndex(caseDepart)
        ligArr, colArr = nomCaseToIndex(caseArrive)
        
#        print(str(ligDep) + "-" + str(colDep))
#        print(str(ligArr) + "-" + str(colArr))
    
        valeur = echiquier[ligDep][colDep]
         
        ec[ligDep][colDep] = None  
        ec[ligArr][colArr] = valeur
        
    #    print(echiquier)
        
        return echiquier
    
    #==============================================================================
    # Vérification déplacement dans la zone
    #==============================================================================
    
    def deplacementsPossibles(self, piece):
        listePossibilites = []
        
        
        return listePossibilites


    def afficherDeplacementsPossibles(self, piece):
        
        #afficher '<>' aux endroits possible
        
        
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
    
    
    
    
    
    
