


def listeDesPieces(couleur):
    
    """
    
    Cette fonction prend en paramètre "B" pour les pions blancs 
    et "N" pour les pions noirs
    
    Elle génere la liste des pieces d'une couleur tel que :
        - i     pour un Pion
        - T     pour une Tour
        - C     pour un cavalier
        - F     pour un fou
        - +     pour un roi
        - -     pour une reine
        
    Chaque valeur est suivie de sa couleur
    
    La fonction renvoie deux listes :
        - la liste des pions
        - la liste des autres pieces

    """
    
    lignePions = ['i' + couleur] * 8
    ligneAutresPieces = [element + couleur for element in ['T', 'C', 'F', '+', '-', 'F', 'C', 'T']]
    
    return [lignePions, ligneAutresPieces]
