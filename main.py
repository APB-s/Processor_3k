# basic import
import cv2 as cv
from cv2.cv2 import imwrite
from numpy import *
import process_img
import functionnality

"""
This program helps photographer to process their image

** any feedbacks? -> a.saillour@protonmail.com **
"""

# todo ouvrir l'explorateur de fichier, sélectionner le bon format
# todo pouvoir régler le niveau d'intensité de l'histogram
# todo rajouter d'autres fonctionnalité

# Lecture de l'image original
brut = functionnality.explorateur()
#brut = cv.imread("/home/apb/Pictures/Cambodge_janvier/000036.JPG")

# Fais appel au processing
images = process_img.processing(brut)

functionnality.show_final_result(images)
choice = input("Voulez vous enregistrer la nouvelle image? ")
choice = str(choice)
functionnality.sauvegarde(choice, images[2])
