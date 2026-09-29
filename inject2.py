import os, base64, re

files_left = ['ace.png', 'naac.png', 'nma.png']
files_right = ['moe.png', 'aictc.jpg', 'innovation ambassodor.png', 'my team logo.jpg']
base_dir = r'C:\Users\prsnl\Downloads'

def get_b64(f):
    path = os.path.join(base_dir, f)
    with open(path, 'rb') as img:
        b64 = base64.b64encode(img.read()).decode('utf-8')
        ext = f.split('.')[-1]
        mime = 'jpeg' if ext.lower() == 'jpg' else 'png'
        return f'data:image/{mime};base64,{b64}'

css_style = "height: 55px; width: auto; object-fit: contain; max-width: 120px; mix-blend-mode: multiply; filter: contrast(1.15) saturate(1.1); image-rendering: high-quality;"

html_left = '<div style=\"display:flex; gap:20px; align-items:center;\">'
for f in files_left:
    html_left += f'<img src=\"{get_b64(f)}\" style=\"{css_style}\">'
html_left += '</div>'

html_right = '<div style=\"display:flex; gap:20px; align-items:center;\">'
for f in files_right:
    html_right += f'<img src=\"{get_b64(f)}\" style=\"{css_style}\">'
html_right += '</div>'

full_strip = f'<div class=\"logo-strip\" id=\"logoStrip\">{html_left}{html_right}</div>'

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as file:
    content = file.read()

pattern = re.compile(r'<div class=\"logo-strip\" id=\"logoStrip\">.*?</div>', re.DOTALL)
new_content = pattern.sub(full_strip, content)

with open(html_path, 'w', encoding='utf-8') as file:
    file.write(new_content)
print('SUCCESS')
