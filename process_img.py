import cv2 as cv
from cv2.cv2 import imwrite

def processing(image_brut):

    list_return = []

    original = cv.resize(image_brut, dsize=(1098, 744), interpolation=cv.INTER_CUBIC)
    list_return.append(original)

    img_y_cr_cb = cv.cvtColor(original, cv.COLOR_BGR2YCrCb)
    y, cr, cb = cv.split(img_y_cr_cb)

    # Applying equalize Hist operation on Y channel.
    y_eq = cv.equalizeHist(y)

    #todo rétablir l'image originel

    img_y_cr_cb_eq = cv.merge((y_eq, cr, cb))
    img_rgb_eq = cv.cvtColor(img_y_cr_cb_eq, cv.COLOR_YCR_CB2BGR)
    list_return.append(img_rgb_eq)

    return list_return