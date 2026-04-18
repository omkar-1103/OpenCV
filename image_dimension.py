import cv2

image = cv2.imread('IMG.jpg')


if image is not None:
    h, w, c = image.shape
    print(f"Width: {w}, Height: {h}, Channels: {c}")
else:
    print('Error: Image not found.')