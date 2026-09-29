with open(r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<svg' in line and 'fill="#d4af37"' in line or 'seal' in line.lower() or 'ribbon' in line.lower() or 'gold' in line.lower():
        print(f"{i}: {line.strip()[:100]}")
