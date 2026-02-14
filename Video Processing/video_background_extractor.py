import cv2
import numpy as np
from glob import glob

# Load images from a directory

image_files = glob("frames/*.jpg")
print("Reading Files")
images = [cv2.imread(img) for img in image_files]

print("Starting Processing")
# Convert images to numpy array
image_stack = np.stack(images, axis=3)

# Compute median along the image stack axis
meadian_image = np.median(image_stack, axis=3).astype(np.uint8)

# Save or diaply the background image
cv2.imwrite("background_no_man.jpg", meadian_image)
cv2.imshow("Background", meadian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()