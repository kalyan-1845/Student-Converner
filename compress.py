from PIL import Image
import os

files = [
    'ace_iic_logo_1784051671009.png',
    'IMG-20260725-WA0250.jpg',
    'IMG-20260725-WA0103.jpg',
    'IMG_20260725_102758.jpg',
    'IMG-20260725-WA0222.jpg',
    'media__1785386951912.jpg',
    'media__1785387012357.png',
    'media__1785387015613.png',
    'media__1785389661951.png',
    'media__1785389690945.png'
]

for file in files:
    if os.path.exists(file):
        try:
            img = Image.open(file)
            fmt = img.format
            img.thumbnail((800, 800))
            
            if fmt == 'JPEG':
                img.save(file, "JPEG", quality=20, optimize=True)
            elif fmt == 'PNG':
                img = img.convert("RGB")
                img.save(file.replace(".png", ".jpg"), "JPEG", quality=20, optimize=True)
            else:
                img.save(file, fmt)
            print(f"Compressed {file}")
        except Exception as e:
            print(f"Failed {file}: {e}")
