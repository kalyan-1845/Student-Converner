html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Dr. M. Balaraju', 'Dr. M. BALARAJU')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('NAME CAPITALIZED')
