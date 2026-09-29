import re

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(</div>)(\s*<!-- 2\. Institution Header)', re.DOTALL)
new_content = pattern.sub(r'\1</div>\2', content, count=1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('FIXED')
