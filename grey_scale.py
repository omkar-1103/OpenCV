import cv2

image = cv2.imread('IMG.jpg')

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black_white", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("Black and white.jpg", gray)
else:
    print('Error: Image not found.')
