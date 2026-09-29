import re
html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_sigs = '''<div class="signatures-section">
      <!-- Left Signatory: IIC Coordinator -->
      <div style="text-align: center;">
        <div class="sig-line"></div>
        <div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;" contenteditable="true" spellcheck="false">Kalyan Reddy</div>
        <div class="sig-title" style="margin-top: 2px;" contenteditable="true" spellcheck="false">IIC Coordinator</div>
      </div>

      <!-- Center Signatory: Vice Principal & IIC President -->
      <div style="text-align: center;">
        <div class="sig-line"></div>
        <div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;" contenteditable="true" spellcheck="false">Dr. Murali Malijeddi</div>
        <div class="sig-title" style="margin-top: 2px;" contenteditable="true" spellcheck="false">Vice Principal & IIC President</div>
      </div>

      <!-- Right Signatory: Principal -->
      <div style="text-align: center;">
        <div class="sig-line"></div>
        <div style="font-weight: 800; font-size: 14px; color: #0b1a30; margin-top: 5px;" contenteditable="true" spellcheck="false">[Principal Name]</div>
        <div class="sig-title" style="margin-top: 2px;" contenteditable="true" spellcheck="false">Principal</div>
      </div>
    </div>'''

content = re.sub(r'<div class=\"signatures-section\">.*?</div>\s*</div>', new_sigs + '\n  </div>', content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('UPDATED 3 SIGNATURES')
