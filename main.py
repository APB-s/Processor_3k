# basic import
from numpy import *
import process_img
import functionnality

"""
This program helps photographer to process their image

** any feedbacks? -> a.saillour@protonmail.com **
"""

# todo sélectionner le bon format
# todo pouvoir régler le niveau d'intensité de l'histogram
# todo rajouter d'autres fonctionnalité

# Lecture de l'image original
brut = functionnality.explorateur()

# Fais appel au processing
images = process_img.processing(brut)

functionnality.show_final_result(images)
choice = input("Voulez vous enregistrer la nouvelle image? ")
choice = str(choice)
functionnality.sauvegarde(choice, images[2])
