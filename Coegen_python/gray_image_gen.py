import numpy as np
import cv2

img = cv2.imread(r"path of original image", cv2.IMREAD_GRAYSCALE)

cv2.imwrite('out_gray.bmp', img)

cv2.waitKey(0)
cv2.destroyAllWindows()