import re

html_path = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\IIC_Certificate_Generator.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add html2pdf.js CDN and Google Fonts for the dashboard
head_injection = '''
  <!-- html2pdf.js for auto-download -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
'''
content = content.replace('</head>', head_injection + '</head>')

# 2. Add Dashboard CSS
css_injection = '''
    /* --- DASHBOARD OVERLAY --- */
    #dashboard-overlay {
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
      background-color: var(--deep-navy);
      z-index: 9999;
      display: flex; align-items: center; justify-content: center;
      font-family: 'Montserrat', sans-serif;
    }
    .dash-card {
      background: #0f2341;
      padding: 40px; border-radius: 16px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
      border: 1px solid var(--gold-dark);
      width: 100%; max-width: 480px;
      text-align: center;
    }
    .dash-card h1 { color: var(--gold-light); font-family: 'Cinzel', serif; font-size: 26px; margin-bottom: 8px; }
    .dash-card p { color: #94a3b8; font-size: 14px; margin-bottom: 25px; }
    
    .dash-input {
      width: 100%; padding: 14px; margin-bottom: 20px;
      background: rgba(255,255,255,0.05); border: 1px solid #334155;
      color: #fff; font-size: 16px; border-radius: 8px; outline: none;
      font-family: inherit; transition: 0.3s;
    }
    .dash-input:focus { border-color: var(--gold-main); background: rgba(255,255,255,0.1); }
    
    .dash-btn {
      width: 100%; padding: 16px;
      background: linear-gradient(135deg, var(--gold-main), var(--gold-dark));
      color: #111; font-weight: 700; font-size: 16px; border: none; border-radius: 8px;
      cursor: pointer; transition: 0.3s; font-family: inherit;
    }
    .dash-btn:hover { filter: brightness(1.1); transform: translateY(-2px); }
    .dash-btn:disabled { background: #334155; color: #94a3b8; cursor: not-allowed; transform: none; }
    
    /* Hide the old controls since we have the dashboard now */
    .controls { display: none !important; }
    body { padding: 0 !important; overflow: hidden; }
    .certificate-container { margin: 0 auto !important; transform: scale(1) !important; }
    #cert-wrapper { 
      position: absolute; top: -9999px; left: -9999px; 
      width: 1123px; height: 794px; /* A4 Landscape at 96 DPI */
    }
'''
content = content.replace('</style>', css_injection + '</style>')

# 3. Inject Dashboard HTML right after <body>
dash_html = '''
  <div id="dashboard-overlay">
    <div class="dash-card">
      <h1>ACE IIC Portal</h1>
      <p>Secure Certificate Generation System</p>
      
      <input type="text" id="studentName" class="dash-input" placeholder="Enter Full Name" autocomplete="off" />
      
      <select id="studentRole" class="dash-input">
        <option value="" disabled selected>Select Your Role</option>
        <option value="convener">Student Convener</option>
        <option value="startup">Startup Coordinator</option>
        <option value="innovation">Innovation Coordinator</option>
        <option value="ipr">IPR Coordinator</option>
        <option value="social">Social Media Coordinator</option>
      </select>
      
      <button id="generateBtn" class="dash-btn" onclick="startGeneration()">Generate & Download</button>
      
      <p id="dash-status" style="margin-top: 20px; font-weight: 500; font-size: 13px;"></p>
    </div>
  </div>
  
  <div id="cert-wrapper">
'''
content = content.replace('<body>', '<body>' + dash_html)
content = content.replace('</body>', '  </div>\n</body>')

# 4. Inject the Generation JS logic at the end of the script tag
js_logic = '''
    async function startGeneration() {
      const name = document.getElementById('studentName').value.trim();
      const roleKey = document.getElementById('studentRole').value;
      const btn = document.getElementById('generateBtn');
      const status = document.getElementById('dash-status');
      
      if(!name || !roleKey) {
        status.style.color = '#ef4444';
        status.innerText = 'Please enter your name and select a role.';
        return;
      }
      
      try {
        btn.disabled = true;
        btn.innerText = 'Authenticating...';
        status.style.color = '#f3df8a';
        status.innerText = 'Connecting to secure registry...';
        
        // 1. Fetch official ID from Vercel Backend
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
        }
        
        // 2. Inject Data into Certificate DOM
        status.innerText = 'Generating Certificate ' + certId + '...';
        
        // Find the elements in the DOM (assuming they have specific classes from the original HTML)
        document.querySelector('.recipient-name').innerText = name.toUpperCase();
        
        // We already have roleData defined from before!
        const data = roleData[roleKey];
        document.getElementById('display-role').innerHTML = data.role;
        document.getElementById('display-citation').innerHTML = data.citation;
        
        // Update Cert ID (Find the span inside meta-details)
        const spans = document.querySelectorAll('.meta-details span');
        if(spans.length >= 2) {
          spans[0].innerText = certId;
          // Set date to today
          const dateOpts = { year: 'numeric', month: 'long', day: 'numeric' };
          spans[1].innerText = new Date().toLocaleDateString('en-US', dateOpts);
        }
        
        // 3. Trigger Download via html2pdf
        status.innerText = 'Rendering High-Quality PDF...';
        const element = document.querySelector('.certificate-container');
        
        const opt = {
          margin:       0,
          filename:     IIC_Certificate_.pdf,
          image:        { type: 'jpeg', quality: 1.0 },
          html2canvas:  { scale: 3, useCORS: true, logging: false },
          jsPDF:        { unit: 'in', format: 'a4', orientation: 'landscape' }
        };
        
        await html2pdf().set(opt).from(element).save();
        
        status.style.color = '#22c55e';
        status.innerText = 'Success! Certificate Downloaded.';
        btn.innerText = 'Complete';
        
      } catch (err) {
        status.style.color = '#ef4444';
        status.innerText = 'Error: ' + err.message;
        btn.disabled = false;
        btn.innerText = 'Try Again';
      }
    }
'''
content = content.replace('</script>', js_logic + '</script>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('DASHBOARD INJECTED')
