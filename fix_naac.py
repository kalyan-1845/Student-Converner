import os, base64, re
from PIL import Image

files_left = ['ace.png', 'naac.png', 'nma.png']
files_right = ['moe.png', 'aictc.jpg', 'innovation ambassodor.png', 'my team logo.jpg']
base_dir = r'C:\Users\prsnl\Downloads'

def clean_and_get_b64(f):
    path = os.path.join(base_dir, f)
    if not os.path.exists(path):
        return ''
    
    img = Image.open(path).convert('RGBA')
    
    # CROP NAAC LOGO TO REMOVE BLACK BARS
    if f == 'naac.png':
        # Crop 50 pixels off the left and right
        w, h = img.size
        img = img.crop((50, 0, w - 50, h))

    datas = img.getdata()
    new_data = []
    for item in datas:
        # Change white to transparent
        if item[0] > 235 and item[1] > 235 and item[2] > 235:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    
    temp_path = os.path.join(base_dir, 'temp_clean.png')
    img.save(temp_path, 'PNG')
    
    with open(temp_path, 'rb') as clean_img:
        b64 = base64.b64encode(clean_img.read()).decode('utf-8')
    
    os.remove(temp_path)
    return f'data:image/png;base64,{b64}'

css_style = "height: 55px; width: auto; object-fit: contain; max-width: 120px;"

html_left = '<div style=\"display:flex; gap:20px; align-items:center;\">'
for f in files_left:
    html_left += f'<img src=\"{clean_and_get_b64(f)}\" style=\"{css_style}\">'
html_left += '</div>'

html_right = '<div style=\"display:flex; gap:20px; align-items:center;\">'
for f in files_right:
    html_right += f'<img src=\"{clean_and_get_b64(f)}\" style=\"{css_style}\">'
html_right += '</div>'

full_strip = f'<div class=\"logo-strip\" id=\"logoStrip\">{html_left}{html_right}</div>'

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as file:
    content = file.read()

pattern = re.compile(r'(<div class=\"logo-strip\" id=\"logoStrip\">.*?)</div></div>(\s*<!-- 2\. Institution Header)', re.DOTALL)
new_content = pattern.sub(f'{full_strip}\\2', content, count=1)

with open(html_path, 'w', encoding='utf-8') as file:
    file.write(new_content)
print('SUCCESS')
