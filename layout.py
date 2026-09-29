import os, base64, re
from PIL import Image

files_left = ['ace.png', 'naac.png', 'nma.png']
file_center = 'my team logo.jpg'
files_right = ['moe.png', 'aictc.jpg', 'innovation ambassodor.png']
base_dir = r'C:\Users\prsnl\Downloads'

def clean_and_get_b64(f):
    path = os.path.join(base_dir, f)
    if not os.path.exists(path):
        return ''
    
    img = Image.open(path).convert('RGBA')
    
    if f == 'naac.png':
        w, h = img.size
        img = img.crop((50, 0, w - 50, h))

    datas = img.getdata()
    new_data = []
    for item in datas:
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

# Make logos larger, up to 70px height, responsive width
css_style = "height: 65px; width: auto; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.05));"

html_left = '<div style=\"display:flex; gap:22px; align-items:center; justify-content:flex-start; flex:1;\">'
for f in files_left:
    html_left += f'<img src=\"{clean_and_get_b64(f)}\" style=\"{css_style}\">'
html_left += '</div>'

html_center = '<div style=\"display:flex; align-items:center; justify-content:center; flex:1;\">'
html_center += f'<img src=\"{clean_and_get_b64(file_center)}\" style=\"height: 80px; width: auto; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.08)); transform: scale(1.1);\">'
html_center += '</div>'

html_right = '<div style=\"display:flex; gap:22px; align-items:center; justify-content:flex-end; flex:1;\">'
for f in files_right:
    html_right += f'<img src=\"{clean_and_get_b64(f)}\" style=\"{css_style}\">'
html_right += '</div>'

full_strip = f'<div class=\"logo-strip\" id=\"logoStrip\" style=\"display:flex; justify-content:space-between; align-items:center; width:100%; border-bottom: 2px solid rgba(197, 155, 39, 0.4); padding-bottom: 15px; margin-bottom: 5px;\">{html_left}{html_center}{html_right}</div>'

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Pattern to replace the existing logo-strip
pattern = re.compile(r'(<div class=\"logo-strip\" id=\"logoStrip\">.*?)</div></div>(\s*<!-- 2\. Institution Header)', re.DOTALL)
new_content = pattern.sub(f'{full_strip}\\2', content, count=1)

with open(html_path, 'w', encoding='utf-8') as file:
    file.write(new_content)
print('SUCCESS')
