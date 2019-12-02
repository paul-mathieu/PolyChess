

class MeilleurMouvement:
    
    def __init__(self, echiquier, couleur):
        
        self.echiquier = echiquier
        
        self.couleur = couleur
        self.couleurOpposee = 'noir' if couleur == 'blanc' else 'noir'
        
        
        self.valeurPions = {
                ('Pion', self.couleur) : -10,
                ('Tour', self.couleur) : -50,
                ('Cavalier', self.couleur) : -30,
                ('Fou', self.couleur) : -30,
                ('Dame', self.couleur) : -90,
                ('Roi', self.couleur) : -900,
                ('Pion', self.couleurOpposee) : 10,
                ('Tour', self.couleurOpposee) : 50,
                ('Cavalier', self.couleurOpposee) : 30,
                ('Fou', self.couleurOpposee) : 30,
                ('Dame', self.couleurOpposee) : 90,
                ('Roi', self.couleurOpposee) : 900
                }
    
    
    def nMeilleursMouvements(self, echiquier = self.echiquier, n, niveauActuel = 0):
        
        listeMouvements = []
        niveauActuel += 1
        
        #si le niveau actuel est le maximum souhaité (ici 5), on ne va pas plus profondement
        if not niveauActuel == 5:


            #~~ pour tous les mouvements ~~

            #pour toutes les pieces de la couleur pouvant être déplacées
            for index in self.echiquier.listePiecesPouvantEtreDeplacees(self.couleur):
                
                #pour tous les déplacements de la piece
                for indexArr in self.echiquier.listeCoupsPossibles(self.indexToNomCase(index)):
                    
                    
                    # le nouvel echiquier contient la piece deplacee
                    echiquierTemp = echiquier.deplacerPieceEnIndex(index, indexArr)
                    
                    
                    #~~ on ajoute des points de pénalité ~~
                    valeurPion = self.valeurPions[self.positions[index].nom]
                    
                    #si une piece adverse peut la manger après le déplacement
#                    if 
                    
                    
                    #~~ récursivité avec les mouvements suivants ~~
                    listeMouvementsSuivants = self.nMeilleursMouvements(echiquierTemp, n, niveauActuel)
                    
                    
                    #on ajoute à la liste de mouvements les objets de type mouvement
                    listeMouvements.append(Mouvement(
                            index, 
                            valeurPion, 
                            niveauActuel + 1, 
                            echiquier.piecesAdversesPouvantManger(index),
                            listeMouvementsSuivants
                            ))
                    
            # on ne garde que les cinq meilleures valeurs :
            
            #on trie les elements par points
            for element in listeMouvements:
                
                
            
            
            return listeMouvements
    
    def nMeilleursMouvements(liste, n):
    
        
    def mouvement(self, indexDeplacement, valerDeplacement):
        
        pass


        
        
        

class Mouvement:
        """
        une liste de mouvements est composee de :
            - un index de piece a deplacer
            - une valeur de déplacement
            - le numero de tour dans lequel le deplacement pourrait être réalise
            - le nombre de pieces adverses pouvant manger la piece actuelle
            - les mouvements suivant si il y en a
        """ 
        
        def __init__(self, indexPiece, valeurDeplacement, numeroDuTour, piecesAdversesPouvantManger, mouvementsSuivants = []):
            
            self.indexPiece = indexPiece
            self.valeurDeplacement = valeurDeplacement
            self.numeroDuTour = numeroDuTour
            self.piecesAdversesPouvantManger = piecesAdversesPouvantManger
            self.mouvementsSuivants = mouvementsSuivants
            
            










