from math import *
from Entite import *

class Robot(Entite):
    def __init__(self, id):
        super().__init__(id)
        self.direction = 90

    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id) + " qui se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "°"

        self.direction = 0
        self.unite_de_temps = 10 #inutile pour le moment

    def __repr__(self):
        return "C'est le robot d'identifiant " + str(self.id) + " se trouve en (" + str(self.x) + "," + str(self.y) + ")" + " et est tourné de " + str(self.direction) + "°"
    
    #à déterminer selon la taille des roues? Pour l'instant 1 tour = 10cm 
    #Et on part du principe que la roue tourne à 6 tour / min (ce qui est très lent)

    #Les instructions pour faire tourner les roues sont a déterminer, 
        #Les roues a priori tourneront tout le temps à la même vitesse, mais pas nécessairement dans le même sens
        #Il faut donc déterminer le nb de tours à faire pour parcourir une distance donnée
        #Ces fonctions vous permettront de faire tourner les roues dans un sens ou dans l'autre
        #Il faudt les appeler dans les méthodes avancer, reculer, tourner_a_gauche et tourner_a_droite
    #Fin des méthodes pour faire tourner les roues


    def avancer(self, distance):
        #calcule le nb de tours nécessaires pour parcourir la distance donnée
        nb_tours = float(distance)/10

        #Il faut les faire tourner en même temps
        #fait tourner les roues gauche et droite en avant pendant le nb de tours calculé
        #self.tourner_roue_gauche_avant(nb_tours)
        #self.tourner_roue_droite_avant(nb_tours)

        print("La voiture a avancé de ", distance, "cm")

        self.x += round( distance * cos(radians(self.direction)) , 10)
        self.y += round( distance * sin(radians(self.direction)) , 10)
        #Mettre à jour les coordonnées x et y (triginonmétrie)

    def reculer(self, distance):
        nb_tours = float(distance)/10

        #Il faut les faire tourner en même temps
        #self.tourner_roue_gauche_arriere(nb_tours)
        #self.tourner_roue_droite_arriere(nb_tours)

        print("La voiture a reculé de ", distance, "cm")

        self.x -= round( distance * cos(radians(self.direction)) , 10)
        self.y -= round( distance * sin(radians(self.direction)) , 10)

        #Mettre à jour les coordonnées

    def tourner_a_gauche(self, angle):
        #calcule le nb de tours pour tourner à gauche de l'angle donné
        nb_tours = float(angle) / 10

        #tourne la roue droite en avant pendant le nb de tours 
        #self.tourner_roue_droite_avant(nb_tours)

        self.direction += angle

        #ajuste la direction pour rester dans [0, 360)
        if (self.direction > 360):
            self.direction -= 360

        self.direction -= angle
        if (self.direction < 0):
            self.direction += 360

        print("Le robot a tourné de ", angle, "° à gauche")

    def tourner_a_droite(self, angle):
        nb_tours = float(angle) / 10
        #self.tourner_roue_gauche_avant(nb_tours)

        #met à jour la direction du robot en fonction de l'angle 
        self.direction -= angle

        #ajuste la direction pour rester dans [0, 360)
        if (self.direction < 0):
            self.direction += 360
            
        print("Le robot a tourné de ", angle, "° à droite")
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getDirection(self):
        return self.direction
    
    def getUniteTemps(self):
        return self.unite_de_temps
    
    def setDirection(self, dire):
        self.direction = dire

    def trace_carre(self, distance):
        for i in range(4):
            self.avancer(distance)
            self.tourner_a_droite(90)
