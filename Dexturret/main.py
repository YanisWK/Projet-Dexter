from Turret.robot import Robot
from Turret.simulation import Simulation
#from main_interface2D import main

#Rayon des roues à 10 pour tester
robot_t = Robot("Dexter", 50, 25, 10, 0, 0) 

def affichage():
    print(robot_t)
    print("Pour pouvoir faire bouger le robot, veuillez taper le numéro de l'action :\n")
    print("0 : Sortir du programme")
    print("1 : Avancer d'une certaine durée")
    print("2 : Choisir la vitesse de la roue gauche")
    print("3 : Choisir la vitesse de la roue droite")
    print("4 : Obtenir la distance avec le mur le plus proche à l'avant du robot")
    while True:
        try:
            choix = int(input("Entrez un chiffre : "))
            if (choix >= 0 and choix <= 4):
                break
            else:
                print("Veuillez choisir un chiffre entre 0 à 4\n")
                continue
        except ValueError:
            print("Veuillez entrer un chiffre \n")

    print("\n")
    return choix

larg = 700
long = 1000
robot1 = Robot(1,50,25,10,long/2,larg/2)
simu = Simulation(1,robot1,larg,long,60)
"""
#permet de relier les main de l'interface et de la simulation
if __name__ == "__main__":
    main()
"""
while True:
    choix_ut = affichage()
    vrd = 0
    vrg = 0
    if choix_ut == 0:
        break
    elif choix_ut == 1:
        while True:
            try:
                choix_d = int(input("Veuillez écrire la durée que vous voulez faire : "))
                break
            except ValueError:
                print("Veuillez entrer un chiffre \n")
        for loop in range(choix_d):
            #Sleep ?
            robot_t.rafraichir(vrg,vrd)

    