from tkinter import IntVar,Button,Label
import Dexturret.interface2D as interface2D
from time import sleep, time
import logging
import Dexturret.controller as controller
from Dexturret import stratAvancer, stratTournerDroite, stratTournerGauche, stratCarreD, stratCarreG, stratCarres, stratCarresFor, robotSim, robotSimu, robotFake, robotIRL, simu, long, larg, fps, choix_robot, cote_condition, carre_condition, dist_sup_25, avancerPeu, avancerViteMur

#Configuration des logs 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode="w",filename="test.log")

robotAdapt,refresh = choix_robot()
if refresh == 1:
    window, couleur, canvas, frame, text_distance = interface2D.creer_graphique(simu)
elif refresh == None:
    print("Arrête du programme")
    exit()

controller_choisi = stratCarresFor
controller_choisi.start()

robotSim.dernier_rafraichissement = time()
#Boucle principale de la simu
while simu.awake and not controller_choisi.stop():

    #Mise a jour tous les 1/temps
    sleep(1/fps)

    controller_choisi.etape()
    if refresh == 1 :
        simu.rafraichir()
        interface2D.dessiner(robotAdapt,simu,canvas,text_distance)
        
robotAdapt.set_vitesse_roue(3, 0)

#Affichage d'une fenêtre pop-up en cas de collision
if (robotAdapt == robotIRL):
    print("Fin du programme robot IRL")
    exit()

if not simu.awake:
    interface2D.popup_collision(window)
    logging.info(f'Le Robot est entré en collision avec un obstacle')

print("Fin du programme robotSimu")

window.mainloop()