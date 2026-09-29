with open(r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'sig-' in line or 'President' in line or 'Principal' in line or 'Convener' in line or 'Kalyan' in line or 'Malijeddi' in line:
        print(f'{i}: {line.strip()}')
