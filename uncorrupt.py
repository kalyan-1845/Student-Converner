import os
html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Only do this if it's actually corrupted with leading hyphen
if content.startswith('-<-!-D-O-C-T-Y-P-E-'):
    restored = content[1::2]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(restored)
    print('CORRUPTION REVERSED')
else:
    print('NOT CORRUPTED LIKE EXPECTED')
