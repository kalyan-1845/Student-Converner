import re

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix encoding issue with Institution's ()
content = content.replace('Institutions', 'Institution\'s')
content = content.replace('Institution&#39;s', 'Institution\'s')

# Update Academic Year
content = re.sub(r'<strong>Academic Year:</strong> 2023 - 2024', r'<strong>Academic Year:</strong> 2025 - 2026', content)

# Update Certificate ID
content = re.sub(r'>ACE/IIC/2024/001<', r'>ACE/IIC/2026/001<', content)

# Update Date of Issue
content = re.sub(r'>August 15, 2024<', r'>September 18, 2026<', content)

# Update Signature 1 to Dr. Murali Malijeddi (Vice Principal) if it's not already
# Actually let's just make sure the signatures look premium
# The JS block for updating roles also has citation text, we need to update the dates there too!
content = content.replace('2023-2024', '2025-2026')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('TEXT FIXED')
