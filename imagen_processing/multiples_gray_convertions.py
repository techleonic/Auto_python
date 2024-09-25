import cv2
from pathlib import Path

color_images = Path("color")
for color in color_images.glob("*.jpeg"):
    img = cv2.imread(str(color), 0)
    print(f"gray/{color.name}")
    cv2.imwrite(f"gray/{color.name}", img)

