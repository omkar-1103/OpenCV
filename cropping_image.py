import cv2

image = cv2.imread('IMG.jpg')

if image is not None:
    h, w, c, =image.shape
    print(f"Width: {w}, Height: {h}, Channels: {c}")
else:
    print('Error: Image not found.')


if image is not None:
    cropped_image = image[200:900, 200:900]   
    cv2.imshow("Original Image;", image) 
    cv2.imshow("Cropped Image:", cropped_image)
    cv2.imwrite("Cropped Image.jpg", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Error: Image not found. Cannot crop.')