import cv2

image = cv2.imread("IMG.jpg")

if image is None:
    print("Imageis not found.")
else:
    lined_image = cv2.line(image, (60,100),(500,100),(255,0,255),4)
    cv2.imshow("Lined_image",lined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
