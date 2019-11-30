"""


"""

from functools import reduce
from rules import Piece


class Echiquier:
        
    
    def __init__(self):
        self.positions = \
            [Piece('Tour', 'noir'), Piece('Cavalier', 'noir'), 
             Piece('Fou','noir'),
             Piece('Dame', 'noir'), Piece('Tour','noir'),
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
             Piece('Dame', 'blanc'), Piece('Roi', 'blanc'),
             Piece('Fou', 'blanc'),
             Piece('Cavalier', 'blanc'), Piece('Tour', 'blanc')]
        
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
        
        
        
        print("   " + lettres)
        print(interlignes)
        
        numLigne = 8
        indexPosition = 0
        
        for piece in self.positions:
            
#            print(ligne)
            
            if indexPosition % 8 == 0:
                print(str(numLigne), end = "  |")
            
            if piece.nom != piece.pieceVide:
                
                print(" " + piece.nomAffichage + " ", end = "|")
        
            else:
                
                print("    ", end = "|")
            
            
            if (indexPosition + 1) % 8 == 0:
                
                print("  " + str(numLigne))
            
                print(interlignes)
            
                numLigne -= 1
                
            indexPosition += 1
            
        print("   " + lettres)
    
        
    
#         A    B    C    D    E    F    G    H  
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    8  | Tn | Cn | Fn | Dn | Rn | Fn | Cn | Tn |  8
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    7  | in | in | in | in | in | in | in | in |  7
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    6  |    |    |    |    |    |    |    |    |  6
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    5  |    |    |    |    |    |    |    |    |  5
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    4  |    |    |    |    |    |    |    |    |  4
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    3  |    |    |    |    |    |    |    |    |  3
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    2  | ib | ib | ib | ib | ib | ib | ib | ib |  2
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    1  | Tb | Cb | Fb | Db | Rb | Fb | Cb | Tb |  1
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#         A    B    C    D    E    F    G    H  
    
    
 
    
#==============================================================================
# Déplacement
#==============================================================================
    
    def deplacerPiece(self, caseDepart, caseArrive):
        
        lettres = ['A','B','C','D','E','F','G','H']
                
        ligDep, colDep = 8 - int(caseDepart[1]), lettres.index(caseDepart[0]) + 1
        ligArr, colArr = 8 - int(caseArrive[1]), lettres.index(caseArrive[0]) + 1
        
        indexDep = ligDep * 8 + colDep - 1
        indexArr = ligArr * 8 + colArr - 1
        
        
#        print(str(ligDep) + "-" + str(colDep))
#        print(str(ligArr) + "-" + str(colArr))
    
        
        self.positions[indexArr] = self.positions[indexDep]
        self.positions[indexDep] = Piece()  
        
    
#==============================================================================
# Vérification déplacement dans la zone
#==============================================================================

    def listeDeplacementsPossibles(self, case):
        
        indexCase = self.nomCaseToIndex(case)
        
        if self.position[indexCase].nom == self.position[indexCase].pieceVide:
            
            return []
        
        listePossibilites = []
        
        self.position[indexCase]
        
        
        return listePossibilites


    def afficherDeplacementsPossibles(self, piece):
        
        #afficher '<>' aux endroits possible
        
        
        pass




#==============================================================================
# Fin du jeu
#==============================================================================

    def isEchecEtMat(self):
        return len(list(filter(lambda piece : piece.nom == 'Roi', self.positions))) < 2
    
    
    def couleurEchecEtMat(self):
        
        if not self.isEchecEtMat():
            return None
        
        return 'blanc' if list(filter(lambda piece : piece.nom == 'Roi', self.positions))[0].couleur == 'noir' else 'noir'


#==============================================================================
# Autres fonctions
#==============================================================================
    
    def nomCaseToIndex(nomCase):
        
        lettres = ['A','B','C','D','E','F','G','H']
        lig, col = 8 - int(nomCase[1]), lettres.index(nomCase[0]) + 1
        
        return ligDep * 8 + colDep - 1
    
    #print("‎• or <>")
    
    
    

    
    
    
    
