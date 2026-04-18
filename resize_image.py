import cv2

image = cv2.imread('IMG.jpg')

if image is None:
    print("Could not read the image.")
else:
    print("Image read successfully.")

    resized = cv2.resize(image,(300,300))
    cv2.imshow("Original Image",image)
    cv2.imshow("Resizec Image",resized)
    cv2.imwrite("Resized Image.jpg", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()