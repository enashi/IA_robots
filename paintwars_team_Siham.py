# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Kenny Lay
#  Prénom Nom: Ihsane Boubrik

import random
import math

from paintwars_config import *
import genetic_algorithms

import comportement
import braitenberg_avoider
import braitenberg_loveWall
import braitenberg_hateWall
import braitenberg_loveBot
import braitenberg_hateBot
import braitenberg_followWall


def get_team_name():
    return "Siham" # à compléter (comme vous voulez)


def step(robotId, sensors):
    sensors = comportement.get_extended_sensors(sensors)
    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)
    
    
    if robotId%5 != 0:
        if sensors["sensor_front"]["distance"] < 0.6 and sensors["sensor_front_left"]["distance"] < 0.6 and sensors["sensor_front_right"]["distance"] < 0.6:
            translation,rotation = braitenberg_avoider.step(robotId,sensors)
        elif sensors["sensor_front_left"]["distance_to_wall"] < 0.6:
            rotation = 0.5
        elif sensors["sensor_front_right"]["distance_to_wall"] < 0.6:
            rotation = -0.5
        elif sensors["sensor_left"]["distance_to_wall"] < 0.6:
            rotation = 1
        elif sensors["sensor_right"]["distance_to_wall"] < 0.6:
            rotation = -1
        else:
            translation,rotation = braitenberg_avoider.step(robotId,sensors)
    else:
        if sensors["sensor_front"]["distance_to_robot"] < 0.6 or sensors["sensor_front_left"]["distance_to_robot"] < 0.6 or sensors["sensor_front_right"]["distance_to_robot"] < 0.6:
            translation,rotation = braitenberg_avoider.step(robotId,sensors)
        elif sensors["sensor_front"]["distance"] < 0.6 and sensors["sensor_front_left"]["distance"] < 0.6 and sensors["sensor_front_right"]["distance"] < 0.6:
            translation,rotation = braitenberg_avoider.step(robotId,sensors)
        else:
            translation,rotation = braitenberg_followWall.step(robotId,sensors)

    # on évite tout blocage
    if sensors["sensor_front_left"]["distance"] < 0.2 and sensors["sensor_front_right"]["distance"] < 0.2 and sensors["sensor_front"]["distance"] < 0.2:
        translation = -1
    elif sensors["sensor_front_left"]["distance"] < 0.1 or sensors["sensor_left"]["distance"] < 0.1 or sensors["sensor_back_left"]["distance"] < 0.1:
        rotation = 0.5
    elif sensors["sensor_front_right"]["distance"] < 0.1 or sensors["sensor_right"]["distance"] < 0.1 or sensors["sensor_back_right"]["distance"] < 0.1:
        rotation = -0.5 

    # limite les valeurs de sortie entre -1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation


