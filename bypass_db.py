import re

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the fetch logic with a localStorage counter that requires NO database
old_js = '''        // 1. Fetch official ID from Vercel Backend
        // If testing locally without backend, it will gracefully fallback after failing
        let certId = 'ACE/IIC/2025-26/000';
        try {
          const res = await fetch('/api/generate', { method: 'POST' });
          const data = await res.json();
          if (res.ok) {
            certId = data.certId;
          } else {
            throw new Error(data.error || 'Server error');
          }
        } catch (e) {
          console.warn('Backend not detected, using fallback ID');
          certId = 'ACE/IIC/2025-26/001'; // Fallback for local testing
        }'''

new_js = '''        // 1. Offline Auto-Counter (No Database Required!)
        let count = parseInt(localStorage.getItem('iic_cert_count') || '0') + 1;
        if (count > 70) {
          throw new Error('All 70 certificates have been generated!');
        }
        localStorage.setItem('iic_cert_count', count.toString());
        
        const formattedNum = String(count).padStart(3, '0');
        let certId = ACE/IIC/2025-26/;'''

content = content.replace(old_js, new_js)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('UPDATED JAVASCRIPT COUNTER')
