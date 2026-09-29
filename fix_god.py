import os
html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Reverse the double corruption!
if "'-'" in content:
    restored = content.replace("'-'", "")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(restored)
    print('CORRUPTION REVERSED')
else:
    print('NO CORRUPTION FOUND')
