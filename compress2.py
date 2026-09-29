from PIL import Image
import glob
import os

for file in glob.glob("*20260801*.jpg"):
    try:
        img = Image.open(file)
        fmt = img.format
        img.thumbnail((800, 800))
        img.save(file, "JPEG", quality=25, optimize=True)
        print(f"Compressed {file}")
    except Exception as e:
        print(f"Failed {file}: {e}")
