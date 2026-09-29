import re

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix apostrophes properly using regex to catch the bad symbol
content = re.sub(r'Institution.s', "Institution's", content)

# Clean roles
content = content.replace('Student Convener – Institution\'s Innovation Council (IIC)', 'Student Convener (IIC)')
content = content.replace('Startup Coordinator – Institution\'s Innovation Council (IIC)', 'Startup Coordinator (IIC)')
content = content.replace('Innovation Coordinator – Institution\'s Innovation Council (IIC)', 'Innovation Coordinator (IIC)')
content = content.replace('IPR Coordinator – Institution\'s Innovation Council (IIC)', 'IPR Coordinator (IIC)')
content = content.replace('Social Media Coordinator – Institution\'s Innovation Council (IIC)', 'Social Media Coordinator (IIC)')

# Also catch standard hyphens just in case
content = content.replace('Student Convener - Institution\'s Innovation Council (IIC)', 'Student Convener (IIC)')
content = content.replace('Startup Coordinator - Institution\'s Innovation Council (IIC)', 'Startup Coordinator (IIC)')
content = content.replace('Innovation Coordinator - Institution\'s Innovation Council (IIC)', 'Innovation Coordinator (IIC)')
content = content.replace('IPR Coordinator - Institution\'s Innovation Council (IIC)', 'IPR Coordinator (IIC)')
content = content.replace('Social Media Coordinator - Institution\'s Innovation Council (IIC)', 'Social Media Coordinator (IIC)')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('CLEANUP SUCCESS')
