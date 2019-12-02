

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

    
    def nMeilleursMouvementsPoints(self, echiquier = self.echiquier, n, niveauActuel = 0):
        
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
                    valeurPiece = self.valeurPions[self.positions[index].nom]
                    
                    #si une piece adverse peut la manger après le déplacement
#                    if 
                    
                    
                    #~~ récursivité avec les mouvements suivants ~~
                    listeMouvementsSuivants = self.nMeilleursMouvementsPoints(echiquierTemp, n, niveauActuel)
                    
                    
                    #on ajoute à la liste de mouvements les objets de type mouvement
                    listeMouvements.append(Mouvement(
                            index, 
                            valeurPiece, 
                            niveauActuel + 1, 
                            echiquier.piecesAdversesPouvantManger(index),
                            listeMouvementsSuivants
                            ))
                    
            # on ne garde que les cinq meilleures valeurs :
            
            #on trie les elements par points                
            listeMouvements = self.trierMouvements(listeMouvements)
            
            #on garde les meilleures valeurs
            listeMouvements = listeMouvements[0:5]
            
            
            return listeMouvements
    
    
    def trierMouvements(self, liste):
        
        if liste == []:
            return []
        
        pivot = liste[0]
        liste1 = []
        liste2 = []
        
        for x in liste[1:]:
            
            if x.valeurPiece > pivot.valeurPiece:
                liste1.append(x)
            else:
                liste2.append(x)
        return quicksort(liste1) + [pivot] + quicksort(liste2)
    
        
    def meilleurMouvement(self, indexDeplacement, valeurDeplacement):
        
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
        
        def __init__(self, indexPiece, valeurPiece, numeroDuTour, piecesAdversesPouvantManger, mouvementsSuivants = []):
            
            self.indexPiece = indexPiece
            self.valeurPiece = valeurPiece
            self.numeroDuTour = numeroDuTour
            self.piecesAdversesPouvantManger = piecesAdversesPouvantManger
            self.mouvementsSuivants = mouvementsSuivants
            
            










