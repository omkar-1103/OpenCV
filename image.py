import cv2

image = cv2.imread('IMG.jpg')

if image is not None:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Error: Image not found.')



if image is not None:
    success = cv2.imwrite('output.jpg', image)
    if success:
        print('Image saved successfully.')
    else:
        print('Error: Could not save the image.')
else:
    print('Error: Image not found. Cannot save.')


image.shape()
