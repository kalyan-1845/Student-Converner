import re
html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace replacement character with apostrophe or hyphen depending on context
content = content.replace('Institutions', "Institution's")
content = content.replace('Convener  Institution', 'Convener - Institution')
content = content.replace('Coordinator  Institution', 'Coordinator - Institution')
content = content.replace('', "'")

# And because the role replacement failed earlier due to the weird character, let's run it again!
content = content.replace('Student Convener - Institution\'s Innovation Council (IIC)', 'Student Convener (IIC)')
content = content.replace('Startup Coordinator - Institution\'s Innovation Council (IIC)', 'Startup Coordinator (IIC)')
content = content.replace('Innovation Coordinator - Institution\'s Innovation Council (IIC)', 'Innovation Coordinator (IIC)')
content = content.replace('IPR Coordinator - Institution\'s Innovation Council (IIC)', 'IPR Coordinator (IIC)')
content = content.replace('Social Media Coordinator - Institution\'s Innovation Council (IIC)', 'Social Media Coordinator (IIC)')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('FIXED')
