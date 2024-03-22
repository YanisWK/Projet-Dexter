from math import pi, degrees


class adaptateurIRL():
    """
    Classe simulant le robot IRL en convertissant les commandes en commandes compréhensibles pour le robot IRL.

    Paramètre :
    - turret.Robot2IN013Fake : robot IRL de la classe Robot2IN013Fake

    """

    def __init__(self,robot):
        """ Initialise le robot de la classe Robot2IN013Fake"""
        self.robot=robot
    def set_vitesse_roue(self, port, vitesse):
        """
        Ajuste la vitesse linéaire d'une ou des deux roues du robot en fonction du port.

        Paramètres :
        - port : numéro du port de la roue 
                -> 1 pour roue gauche
                -> 2 pour roue droite
                -> 3 pour les deux roues
        - vitesse : nouvelle vitesse linéaire de la roue (en cm/s)
        """
        dps = vitesse * 2 * pi / (self.robot.rayon_des_roues * 10)
        self.robot.set_motor_dps(port, dps)

    def detect_distance(self,_simu_longueur, _simu_largeur):
        """
        Simule le capteur distance et retourne la distance détectée
        
        Paramètres :
        - _simu_longueur : longueur de l'environnement du robot
        - _simu_largeur : largeur de l'environnement du robot
        """
        dist=self.get_distance()/10
        if (dist==819):
            return 800
        return dist

    def get_position_moteurs(self):
        """
        Retourne la position des moteurs du robot au dernier rafraichissement.
        """
        return self.get_motor_position()
    
    def set_position_moteurs(self, port, offset):
        """
        Définit la position des moteurs avec un décalage spécifié.

        Paramètres :
        - port : numéro du port du moteur
        - offset : offset de décalage en degrés
        """
        return self.offset_motor_encoder(port, offset)
    
    def rafraichir(self):
        """
        Met à jour la position des moteurs en fonction de leur vitesse actuelle.
        """
        self.position_moteurs[0] += self.vit_roue_gauche
        self.position_moteurs[1] += self.vit_roue_droite


class adaptateurSimu():

    def __init__(self,robot):
        """
        Initialise un adaptateur de simulation pour le robot.

        Paramètres :
        - id : identifiant du robot
        - longueur, largeur : dimensions du robot
        - rayon_des_roues : rayon des roues du robot
        - x,y : position du robot
        - dernier_rafraichissement : timestamp du dernier rafraîchissement des données du robot
        """
        self.robot=robot

    def set_vitesse_roue(self,port,vitesse):
        """
        Ajuste la vitesse linéaire d'une ou des deux roues du robot en fonction du port.

        Paramètres :
        - port : numéro du port de la roue 
                -> 1 pour roue gauche
                -> 2 pour roue droite
                -> 3 pour les deux roues
        - vitesse : nouvelle vitesse linéaire de la roue (en cm/s)
        """
        if (port == 1 or port == 3):
            self.vitesse_lineaire_roue_gauche = vitesse
        if (port == 2 or port == 3):
            self.vitesse_lineaire_roue_droite = vitesse

    def get_position_moteurs(self):
        """Retourne la position des moteurs au dernier rafraîchissement"""
        return (self.position_moteurs[0], self.position_moteurs[1])
    
    def set_position_moteurs(self, port, offset):
        """
        Définit la position des moteurs avec un décalage spécifié.

        Paramètres :
        - port : numéro du port du moteur
        - offset : offset de décalage en degrés
        """
        if (port == 1 or port == 3):
            self.position_moteurs[0] = offset
        if (port == 2 or port == 3):
            self.position_moteurs[1] = offset