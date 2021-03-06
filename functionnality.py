import subprocess
import cv2 as cv
from cv2.cv2 import imwrite
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

# list les réponses possibles
answers_yes = ["oui", "Oui", "OUI", "O", "yes", "Yes", "YES", "y", "Y", "0"]
answers_no = ["non", "Non", "NON", "N", "no", "No", "NO", "n", "N", "1", "2"]


def show_final_result(images_list):
    for i in range(len(images_list) - 1):
        if i == 0:
            titre = "Image brut"
        else:
            titre = "Processed image"
        cv.imshow(titre, images_list[i])
        cv.waitKey(0)


def sauvegarde(choice, image):
    if choice in answers_yes:
        name = input("Veuillez rentrer le nom de l'image (format: nom_image.jpg")
        check = imwrite("/home/apb/Pictures/Cambodge_janvier/Processed/" + name, image)
        cv.destroyAllWindows()
        exit(0)
    elif choice in answers_no:
        print("a bientot!")
        cv.destroyAllWindows()
        exit(0)

    if not check:
        print("La photo n'a pas pu être sauvée..")
        cv.destroyAllWindows()
        exit(-1)


def explorateur():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    brut = cv.imread(filename)
    return brut
