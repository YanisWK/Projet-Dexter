from math import *

"""Documentation : """
class Simulation:
    def __init__(self, id, robot, largeur, longueur,temps):
        self.id = id
        self.robot = robot                  #Le robot
        self.longueur = longueur            #La longueur de l'environnement
        self.largueur = largeur             #La largueur de l'environnement
        self.temps = temps                  #Le nombre de rafraichissement par seconde
        self.vitesse = 100                  #La vitesse à laquelle le robot se déplace
        self.distance = 100                 #La distance que le robot va parcourir (1 pixel = 1 cm)
        self.velociteD = []                 #Liste des déplacements vers l'avant à chaque rafraichissement
        self.velociteR = []                 #Liste des changements de direction à chaque rafraichisement
        self.angle = 90

        #Les 4 coins du robot delon la position du centre et la taille du robot
        L = robot.longueur/2
        l = robot.largeur/2
        x = robot.x
        y = robot.y
        self.coordRobot = [(x-l, y-L), (x+l, y-L), (x+l, y+L), (x-l, y+L)]

    def droiteDirection(self):
        """
        -Fonction qui retourne (a,b) tel que ax+by représente la droite de la direction dans laquelle le robot est orienté
        """
        a = cos(radians(self.angle))
        b = sin(radians(self.angle))
        return (a,b)
    
    def rafraichir(self):

        """
        -Fonction qui effectue les actions nécessaires à chaque rafraichissement 
        -Avancer d'une distance (celle de velociteD[0]) et/ou tourner d'un certain angle (celle de velocitéR[0]) si les tableaux ne sont pas vides
        -Mettre à jour les coordonnées des coins du robot (avec coinsRobot)
        """
        #Si l'un des tableaux n'est pas vide
        if self.velociteD or self.velociteR :
            #si le tableau velociteD n'est pas vide alors on avance
            if self.velociteD : 
                self.robot.avancer(self.velociteD.pop(0))
            
            #si le tableau velociteR n'est pas vide alors on tourne
            if self.velociteR : 
                self.robot.tourner(self.velociteR.pop(0))

            #Verification des bords de la simulation
            decal_x = 0
            decal_y = 0
            for coin in self.coordRobot:
                if coin[0] < 0:
                    decal_x = max(decal_x, -coin[0])
                if coin[0] > self.longueur:
                    decal_x = min(decal_x, -(coin[0] - self.longueur))

                if coin[1] < 0:
                    decal_y = max(decal_y, -coin[1])
                if coin[1] > self.largeur:
                    decal_y = min(decal_y, -(coin[1] - self.largeur))

            self.robot.x += decal_x
            self.robot.y += decal_y

            self.coinsRobot()
        
    
    def coinsRobot(self):
        """
        -Fonction qui calcule, à l'aide de la taille et de la drection, la position des 4 coins du robot
        -Nécessite obtenirAngle
        -Le centre du rectangle est la position x y du robot
        -Modifier self.coordRobot par la liste des coordonnees des 4 coins
        """
        L = self.robot.longueur / 2
        l = self.robot.largeur / 2
        dir = self.robot.direction
        x = self.robot.x
        y = self.robot.y


        c1 = ( (x + L*cos(radians(dir))) + l*cos(radians(dir + 90)), (y - L*sin(radians(dir))) - l*sin(radians(dir + 90)) )
        c2 = ( (x + L*cos(radians(dir))) + l*cos(radians(dir - 90)), (y - L*sin(radians(dir))) - l*sin(radians(dir - 90)) )
        c3 = ( (x - L*cos(radians(dir))) + l*cos(radians(dir - 90)), (y + L*sin(radians(dir))) - l*sin(radians(dir - 90)) )
        c4 = ( (x - L*cos(radians(dir))) + l*cos(radians(dir + 90)), (y + L*sin(radians(dir))) - l*sin(radians(dir + 90)) )
        self.coordRobot = [c1, c2, c3, c4]
    
    def deplacementRobot(self):
        """
        -Fonction qui effectue les calcules nécessaire afin de déplacer le robot
        -Ajout dans velociteD les distances à faire à chaque rafraichissement selon la distance à parcourir et la vitesse,
            dans la direction du robot
        -Ne retourne rien
        """
        #Calcule de la distance que parcoure le robot à chaque rafraîchissement
        distance_par_rafraichissement = self.vitesse / self.temps

        #(à voir) Calcule du nombre de rafraîchissements nécessaires pour que le robot puisse parcourir la distance totale
        #nombre_rafraichissements = self.distance / distance_par_rafraichissement

        #La distance que le robot doit parcourir
        distance_a_parcourir = self.distance

        #Ajout de la distance que le robot parcoure à chaque rafraîchissement dans la liste velociteD 
        if (distance_a_parcourir > 0):
            while distance_a_parcourir > distance_par_rafraichissement:
                    self.velociteD.append(distance_par_rafraichissement)
                    distance_a_parcourir -= distance_par_rafraichissement
        else:
            while distance_a_parcourir < -distance_par_rafraichissement:
                    self.velociteD.append(-distance_par_rafraichissement)
                    distance_a_parcourir += distance_par_rafraichissement
        self.velociteD.append(distance_a_parcourir)
    
    def rotationRobot(self):
        """
        -Fonction qui effectue les calcules nécessaire afin de faire une rotation au robot
        -Ajout dans velociteR les modifications d'angles à faire à chaque rafraichissement selon la vitesse
        -Ne retourne rien
        """
        #Calcule de la rotation que le robot doit tourner à chaque rafraîchissement
        Rotation_par_rafraichissement = self.vitesse / self.temps
        
        Angle_a_parcourir = self.angle
        
        #Ajout de la rotation que le robot parcoure à chaque rafraîchissement dans la liste velociteR
        if (Angle_a_parcourir > 0):
            while Angle_a_parcourir > Rotation_par_rafraichissement:
                self.velociteR.append(Rotation_par_rafraichissement)
                Angle_a_parcourir -= Rotation_par_rafraichissement
        else:
            while Angle_a_parcourir < -Rotation_par_rafraichissement:
                self.velociteR.append(-Rotation_par_rafraichissement)
                Angle_a_parcourir += Rotation_par_rafraichissement

        self.velociteR.append(Angle_a_parcourir)
        return