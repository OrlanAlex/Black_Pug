import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Santorini.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 105, 0, cv2.THRESH_BINARY)
plt.imshow(binary, cmap="gray")
plt.show()
