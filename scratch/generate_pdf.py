import markdown
from fpdf import FPDF

md_path = r"C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\Idea_Camp_Event_Proposal.md"
pdf_path = r"C:\Users\prsnl\Downloads\Idea_Camp_Event_Proposal.pdf"

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Convert Markdown to HTML
html = markdown.markdown(text, extensions=['tables'])

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

# Write HTML to PDF
pdf.write_html(html)

# Output
pdf.output(pdf_path)
print(f"PDF successfully generated at {pdf_path}")
