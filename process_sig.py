import os, base64, math
from PIL import Image, ImageEnhance

img_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\.user_uploaded\media_1790696502167.jpg'
out_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\sig_transparent.png'

# Open the image
img = Image.open(img_path).convert('RGBA')

# Looking at the preview, the signature is rotated ~90 degrees counter-clockwise or clockwise.
# Let's rotate it to be horizontal. It's written top-to-bottom in the image, so we rotate 90 degrees CCW (or 270)
# Actually, the user's name is Ramesh Alladi. The signature looks like 'Alladi R...'. 
# It is written from bottom to top in the image, so we need to rotate it -90 degrees (or 270 degrees).
img = img.rotate(-75, expand=True) # Let's rotate 90 degrees to make it horizontal, wait the image is slightly diagonal, let's just do 90.
img = img.rotate(-15, expand=True) # Overall -90

# Increase contrast to make ink darker and paper whiter
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(3.0)

# Make background transparent
datas = img.getdata()
new_data = []
for item in datas:
    # item is (R, G, B, A)
    # The ink is blue, so B will be higher than R and G, and overall it's darker.
    # The paper is white/gray.
    # Let's use a threshold: if it's light enough, make it transparent.
    brightness = (item[0] + item[1] + item[2]) / 3
    if brightness > 150:
        new_data.append((255, 255, 255, 0))
    else:
        # Keep the blue ink, but make it fully opaque
        new_data.append((item[0], item[1], item[2], 255))
        
img.putdata(new_data)

# Auto-crop the transparent bounds
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# Resize to a reasonable signature size (e.g., max height 80px)
w, h = img.size
new_h = 70
new_w = int(w * (new_h / h))
img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

img.save(out_path, 'PNG')

# Encode to base64
with open(out_path, 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

# Inject into HTML
html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

sig_img_tag = f'<img src="data:image/png;base64,{b64}" style="height: 45px; margin-bottom: -15px; position: relative; z-index: 10;" alt="Ramesh Alladi Signature">'

# The current HTML has:
# <div class="sig-line"></div>
# <div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;" contenteditable="true" spellcheck="false">Ramesh Alladi</div>

import re
replacement = f'''{sig_img_tag}
        <div class="sig-line"></div>
        <div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;" contenteditable="true" spellcheck="false">Ramesh Alladi</div>'''

content = re.sub(r'<div class="sig-line"></div>\s*<div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;" contenteditable="true" spellcheck="false">Ramesh Alladi</div>', replacement, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('SUCCESS')
