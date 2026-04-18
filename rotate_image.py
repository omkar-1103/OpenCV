import cv2

image = cv2.imread('IMG.jpg')

if image is None:
    print("Image could not foun.")
else:
    h , w = image.shape[:2]
    center = (w//2, h//2)
    m = cv2.getRotationMatrix2D(center, 90, 0.3)
    rotated_image = cv2.warpAffine(image,m, (w, h))
    cv2.imshow("Original Image:", image)
    cv2.imshow("Rotated Image:", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()