import cv2
import os

video_file = "./vi.mp4"
output_dir = "frames"

os.makedirs(output_dir, exist_ok=True)

vid = cv2.VideoCapture(video_file)
count = 0

while True:
    success, image = vid.read()
    if not success:
        break

    cv2.imwrite(f"{output_dir}/frame_{count}.jpg", image)
    print("|", end="")
    count += 1

vid.release()
print("\nDONE")
