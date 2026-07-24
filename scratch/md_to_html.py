import markdown
import os

md_path = r"C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c\Idea_Camp_Event_Proposal.md"
html_path = r"C:\Users\prsnl\Downloads\Idea_Camp_Event_Proposal.html"

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add basic CSS to make the PDF look professional
css = """
<style>
body { font-family: 'Segoe UI', Arial, sans-serif; padding: 40px; line-height: 1.6; color: #222; }
h1 { color: #0d47a1; border-bottom: 2px solid #0d47a1; padding-bottom: 10px; }
h2 { color: #1565c0; margin-top: 30px; }
table { border-collapse: collapse; width: 100%; margin-top: 20px; margin-bottom: 20px; }
th, td { border: 1px solid #ccc; padding: 12px; text-align: left; }
th { background-color: #e3f2fd; color: #0d47a1; }
hr { border: 0; border-top: 1px solid #ccc; margin: 30px 0; }
</style>
"""

html_content = markdown.markdown(text, extensions=['tables'])
final_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'>{css}</head><body>{html_content}</body></html>"

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)
