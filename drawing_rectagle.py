import cv2

image = cv2.imread("IMG.jpg")

if image is None:
    print("Image is not found.")
else:
    rectangle_image = cv2.rectangle(image,(700,700),(50,50),(0,0,255),3)
    cv2.imshow("Rectangle",rectangle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()