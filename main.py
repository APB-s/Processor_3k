# basic import
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
brut = cv.imread("/home/apb/Pictures/Cambodge_janvier/000084.JPG")

# Fais appel au processing
images = process_img.processing(brut)

# list les réponses possibles
answers_yes = ["oui", "Oui", "OUI", "O", "yes", "Yes", "YES", "y", "Y", "0"]
answers_no = ["non", "Non", "NON", "N", "no", "No", "NO", "n", "N", "1", "2"]

def sauvegarde(choice, image):
    print(choice)
    print(type(choice))

    if choice in answers_yes:
        name = input("Veuillez rentrer le nom de l'image (format: nom_image.jpg")
        check = imwrite("/home/apb/Pictures/Cambodge_janvier/Processed" + name, image)
        exit(0)
    elif choice in answers_no:
        print("a bientot!")
        exit(0)

    if not check:
        print("La photo n'a pas pu être sauvée..")
        exit(-1)

def show_final_result(images_list):

    for i in range(len(images_list)):
        if i == 0:
            titre = "Image brut"
        else:
            titre = "Processed image"
        cv.imshow(titre, images_list[i])
        cv.waitKey(0)
    cv.destroyAllWindows()

show_final_result(images)
choice = input("Voulez vous enregistrer la nouvelle image? ")
choice = str(choice)
sauvegarde(choice, images[1])

