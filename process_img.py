import cv2 as cv
from cv2.cv2 import imwrite

def processing(image_brut):

    list_return = []

    imwidth = image_brut.shape[0]
    imheight = image_brut.shape[1]



    original_rescale = cv.resize(image_brut, dsize=(1098, 744), interpolation=cv.INTER_LINEAR)
    list_return.append(original_rescale)

    img_y_cr_cb_rescale = cv.cvtColor(original_rescale, cv.COLOR_BGR2YCrCb)
    y_rescale, cr_rescale, cb_rescale = cv.split(img_y_cr_cb_rescale)

    # Applying equalize Hist operation on Y channel.
    y_eq = cv.equalizeHist(y_rescale)

    img_y_cr_cb_eq = cv.merge((y_eq, cr_rescale, cb_rescale))
    img_rgb_eq = cv.cvtColor(img_y_cr_cb_eq, cv.COLOR_YCR_CB2BGR)
    list_return.append(img_rgb_eq)

    # Processing pour avoir format brut
    img_y_cr_cb_brut = cv.cvtColor(image_brut, cv.COLOR_BGR2YCrCb)
    y, cr, cb = cv.split(img_y_cr_cb_brut)
    y_eq_brut = cv.equalizeHist(y)
    img_y_cr_cb_eq_brut = cv.merge((y_eq_brut, cr, cb))
    img_rgb_eq_brut = cv.cvtColor(img_y_cr_cb_eq_brut, cv.COLOR_YCR_CB2BGR)
    list_return.append(img_rgb_eq_brut)

    return list_return