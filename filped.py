import cv2

image = cv2.imread('IMG.jpg')


if image is None:
    print("Image could not fould.")
else:
    vertical =cv2.flip(image, 0)
    cv2.imshow("Vertical Flip", vertical)
    horizontal = cv2.flip(image, 1)
    cv2.imshow("Horizontal flip",horizontal)
    vertical_horizontal = cv2.flip(image, -1)
    cv2.imshow("Vertical and horizontal flip:", vertical_horizontal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


