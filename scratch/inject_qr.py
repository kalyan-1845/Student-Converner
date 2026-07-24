import qrcode
import base64
from io import BytesIO
import re

# Generate QR Code for YUKTI portal
url = "https://yukti.mic.gov.in/"
qr = qrcode.QRCode(version=1, box_size=10, border=1)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Convert to Base64
buffered = BytesIO()
img.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

# Read HTML
html_path = r"C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\scratch\Startup_Awareness_Poster.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace Placeholder with Image
qr_html = f"""<div class="qr-placeholder" style="background:none; border:none; padding:0; margin:0;">
                <img src="data:image/png;base64,{img_str}" style="width:120px; height:120px; border-radius:10px;">
            </div>"""

html_content = re.sub(
    r'<div class="qr-placeholder">[\s\S]*?</div>',
    qr_html,
    html_content
)

# Write back
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("QR Code injected successfully.")
