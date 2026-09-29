import re

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Fix encoding artifacts
content = content.replace('Institutions', "Institution's")
content = content.replace('', "-")
content = content.replace('Institution&#39;s', "Institution's")

# Fix roles to be cleaner, dropping the redundant repetition of the full council name in the subtitle
content = content.replace('Student Convener - Institution\'s Innovation Council (IIC)', 'Student Convener (IIC)')
content = content.replace('Startup Coordinator - Institution\'s Innovation Council (IIC)', 'Startup Coordinator (IIC)')
content = content.replace('Innovation Coordinator - Institution\'s Innovation Council (IIC)', 'Innovation Coordinator (IIC)')
content = content.replace('IPR Coordinator - Institution\'s Innovation Council (IIC)', 'IPR Coordinator (IIC)')
content = content.replace('Social Media Coordinator - Institution\'s Innovation Council (IIC)', 'Social Media Coordinator (IIC)')

# Same for JS data strings
content = content.replace('Student Convener - Institution\'s Innovation Council (IIC)', 'Student Convener (IIC)')
content = content.replace('Startup Coordinator - Institution\'s Innovation Council (IIC)', 'Startup Coordinator (IIC)')
content = content.replace('Innovation Coordinator - Institution\'s Innovation Council (IIC)', 'Innovation Coordinator (IIC)')
content = content.replace('IPR Coordinator - Institution\'s Innovation Council (IIC)', 'IPR Coordinator (IIC)')
content = content.replace('Social Media Coordinator - Institution\'s Innovation Council (IIC)', 'Social Media Coordinator (IIC)')

# Update Academic Year to current (2025 - 2026)
content = re.sub(r'2023 - 2024', '2025 - 2026', content)
content = re.sub(r'2023-2024', '2025-2026', content)
content = re.sub(r'>August 15, 2024<', r'>September 18, 2026<', content)

# Update Certificate No placeholder to current year
content = re.sub(r'ACE/IIC/2024/', 'ACE/IIC/2026/', content)
content = re.sub(r'ACE/IIC/2024-25', 'ACE/IIC/2025-26', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('TEXT PERFECTED')
