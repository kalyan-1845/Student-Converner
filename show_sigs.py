with open(r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(540, 580):
    if i < len(lines):
        s = lines[i].rstrip()
        print(f"{i}: {s.encode('ascii', 'ignore').decode('ascii')}")
