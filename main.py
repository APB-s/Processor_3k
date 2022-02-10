import cv2 as cv
from cv2.cv2 import imwrite
from numpy import *
"""
This program helps photographer to process their image

** any feedbacks? -> a.saillour@protonmail.com **
"""

#ouvrir l'explorateur de fichier, sélectionner le bon format
#pouvoir régler le niveau d'intensité de l'histogram
#rajouter d'autres fonctionnalité

# lecture de l'image original
brut = cv.imread("/home/apb/Pictures/Cambodge_janvier/000036.JPG")
original = cv.resize(brut, dsize=(1647, 1116), interpolation=cv.INTER_CUBIC)

imwidth = original.shape[0]
imheight = original.shape[1]

img_y_cr_cb = cv.cvtColor(original, cv.COLOR_BGR2YCrCb)
y, cr, cb = cv.split(img_y_cr_cb)

# Applying equalize Hist operation on Y channel.
y_eq = cv.equalizeHist(y)

img_y_cr_cb_eq = cv.merge((y_eq, cr, cb))
img_rgb_eq = cv.cvtColor(img_y_cr_cb_eq, cv.COLOR_YCR_CB2BGR)

cv.imshow('Native image', original)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Native image', img_rgb_eq)

cv.waitKey(0)
cv.destroyAllWindows()

plt.show()

choice = input("Voulez vous enregistrer la nouvelle image?")

if choice == "1" or "oui":
    name = input("Veuillez rentrer le nom de l'image (format: nom_image.jpg")
    check = imwrite("/home/apb/Pictures/Cambodge_janvier/" + name, img_rgb_eq)

    if not check:
        print("La photo n'a pas pu être sauvée..")
        exit(-1)

else:
    print('a bientot')
    exit(0)