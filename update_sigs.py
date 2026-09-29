import re
html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

left_sig = '''      <!-- Left Signatory: Student Convener -->
      <div style="text-align: center;">
        <div class="sig-line"></div>
        <div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;">Kalyan Reddy</div>
        <div class="sig-title" style="margin-top: 2px;">Student Convener</div>
      </div>'''

right_sig = '''      <!-- Right Signatory: President / Head of Institution -->
      <div style="text-align: center;">
        <div class="sig-line"></div>
        <div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;">Dr. Murali Malijeddi</div>
        <div class="sig-title" style="margin-top: 2px;">Vice Principal & IIC President</div>
      </div>'''

# Replace left signatory block
content = re.sub(r'<!-- Left Signatory: Student Convener -->.*?<div class=\"sig-title\">Student Convener</div>\s*<div class=\"sig-org\">ACE Engineering College</div>\s*</div>', left_sig, content, flags=re.DOTALL)

# Replace right signatory block
content = re.sub(r'<!-- Right Signatory: President / Head of Institution -->.*?<div class=\"sig-title\">Vice Principal</div>\s*<div class=\"sig-org\">ACE Engineering College</div>\s*</div>', right_sig, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('SIGNATURES UPDATED')
