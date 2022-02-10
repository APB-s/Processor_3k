import cv2 as cv
from cv2.cv2 import imwrite
from numpy import *

import process_img

"""
This program helps photographer to process their image

** any feedbacks? -> a.saillour@protonmail.com **
"""

#todo ouvrir l'explorateur de fichier, sélectionner le bon format
#todo pouvoir régler le niveau d'intensité de l'histogram
#todo rajouter d'autres fonctionnalité

# Lecture de l'image original
brut = cv.imread("/home/apb/Pictures/Cambodge_janvier/000036.JPG")

# Fais appel au processing
process_img.processing(brut)


def show_final_result():

    cv.imshow('Native image', original)

    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imshow('Native image', img_rgb_eq)

    cv.waitKey(0)
    cv.destroyAllWindows()

choice = input("Voulez vous enregistrer la nouvelle image?")

def sauvegarde():

if choice == "1" or "oui":
    name = input("Veuillez rentrer le nom de l'image (format: nom_image.jpg")
    check = imwrite("/home/apb/Pictures/Cambodge_janvier/" + name, img_rgb_eq)

    if not check:
        print("La photo n'a pas pu être sauvée..")
        exit(-1)

else:
    print('a bientot')
    exit(0)