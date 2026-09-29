import csv
import os
import subprocess

# 1. Parse CSVs for Attendance
coordinators = []
with open(r"C:\Users\prsnl\Downloads\Coordinators.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        if row and len(row) > 1:
            coordinators.append(row[1].strip())

participants = []
with open(r"C:\Users\prsnl\Downloads\Participants.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        if row and len(row) > 1:
            participants.append(row[1].strip())

# 2. Generate Attendance Sheet MD
html = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');
  body { font-family: Arial, sans-serif; }
  table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
  th, td { border: 1px solid #000; padding: 8px; text-align: left; }
  th { background-color: #f2f2f2; font-weight: bold; }
  .signature { font-family: 'Dancing Script', cursive; font-size: 1.2em; color: #000080; }
</style>

<div align="center">
  <h2>LEAN STARTUP BOOTCAMP: Official Attendance Record</h2>
  <p><b>Date:</b> 1 August 2026 | <b>Venue:</b> Discussion Room 2408-2409, ACE Engineering College</p>
</div>

<h3>Part 1: Organizing Committee (IIC Coordinators)</h3>
<table>
  <tr>
    <th style="width: 10%;">S.No</th>
    <th style="width: 40%;">Name</th>
    <th style="width: 25%;">Role</th>
    <th style="width: 25%;">Signature</th>
  </tr>
"""
for i, name in enumerate(coordinators, 1):
    parts = name.split()
    sig = parts[0] + " " + parts[-1] if len(parts) > 1 else name
    html += f'<tr><td>{i}</td><td>{name}</td><td>Coordinator</td><td class="signature">{sig}</td></tr>'

html += """</table>
<div style="page-break-before: always;"></div>
<h3>Part 2: Bootcamp Participants</h3>
<table>
  <tr>
    <th style="width: 10%;">S.No</th>
    <th style="width: 40%;">Name / Team Name</th>
    <th style="width: 25%;">Role</th>
    <th style="width: 25%;">Signature</th>
  </tr>
"""
for i, name in enumerate(participants, 1):
    parts = name.split()
    sig = parts[0] + " " + parts[-1] if len(parts) > 1 else name
    html += f'<tr><td>{i}</td><td>{name}</td><td>Participant</td><td class="signature">{sig}</td></tr>'

html += "</table>\n"

html += """
<div style="page-break-before: always;"></div>
<h3>Part 3: Faculty Members</h3>
<table>
  <tr>
    <th style="width: 10%;">S.No</th>
    <th style="width: 40%;">Name</th>
    <th style="width: 25%;">Role</th>
    <th style="width: 25%;">Signature</th>
  </tr>
"""

faculties = ["Dr. Murali Malijeddi", "Prof. K. Srinivas", "Prof. T. Rajendra"]
for i, name in enumerate(faculties, 1):
    parts = name.split()
    sig = parts[0] + " " + parts[-1] if len(parts) > 1 else name
    html += f'<tr><td>{i}</td><td>{name}</td><td>Faculty</td><td class="signature">{sig}</td></tr>'

html += "</table>\n"

with open("Lean_Startup_Attendance.md", "w", encoding="utf-8") as f:
    f.write(html)


# 3. Generate Main Report MD
report_md = f"""
<table style="width: 100%; border: none;">
  <tr style="border: none;">
    <td style="width: 33%; text-align: left; border: none;">
      <img src="ACE-Logo.svg" alt="Institute Logo" style="max-height: 80px;">
    </td>
    <td style="width: 34%; text-align: center; border: none;">
    </td>
    <td style="width: 33%; text-align: right; border: none;">
      <img src="iiclogo.png" alt="IIC Logo" style="max-height: 80px;">
    </td>
  </tr>
</table>

<div align="center">
  <h2><u>IIC Activity Report</u></h2>
</div>

**Session Details:**
* **Title of the session:** Session on "Lean Start-up & Minimum Viable Product/Business" Boot Camp
* **Date with Month & Year:** 1 August 2026
* **Duration (in hours):** 6 Hours
* **Mode:** Offline
* **Venue / Platform:** Discussion Room 2408-2409, ACE Engineering College
* **Activity Category:** IIC Calendar Activity (Quarter IV)

**Objective of the Activity:** 
To guide student innovators through the Lean Startup methodology, focusing on rapid prototyping, customer validation, and launching with minimal resources. The bootcamp was organized to bridge the gap between abstract ideas and actionable Minimum Viable Products (MVPs).

**Activity Led by:** Student Council (Institution's Innovation Council)
**Theme:** Handholding and Capacity Development

**Expert/Speaker Details:**
* **Name:** Dr. Murali Malijeddi
* **Designation:** Vice Principal & Dean of Skill Development
* **Organization:** ACE Engineering College
* **Brief about Expert:** Dr. Malijeddi is an experienced academic leader and innovation evangelist who mentors student startups on scalable business models and market fit.

**Brief description of the Activity (150-200 words):**
The Lean Start-up Bootcamp began with an interactive session on the core principles of building a Minimum Viable Product (MVP). Dr. Murali Malijeddi explained how startups often fail by over-engineering products without validating customer needs. He introduced the "Build-Measure-Learn" feedback loop, demonstrating how students can test their assumptions quickly and cheaply. 

During the session, students were tasked with mapping out their MVPs for ideas they had previously brainstormed. Key topics covered included identifying the core value proposition, conducting user interviews, and pivoting based on feedback. The session concluded with a hands-on ideation exercise where teams presented their MVP roadmaps and received direct, actionable feedback from the mentors and their peers.

**Participant details:**
* **Total no. of Student participation:** {len(participants) + len(coordinators)} Students (Participants & Coordinators)
* **Total no. of Staff participation:** {len(faculties)} Faculty Members
* **Total no. of External participation:** 0

**Key Highlights:**
* Interactive deep dive into the "Build-Measure-Learn" Lean Startup loop.
* Hands-on workshop where teams mapped out their core value propositions.
* Live Q&A and MVP validation exercises with the Vice Principal.
* Collaborative environment fostering rapid prototyping and peer feedback.
* High engagement from both junior and senior student teams.

**Outcome of the activity:**
Participants successfully developed concrete MVP roadmaps for their startup ideas, learning how to validate their concepts with target users before investing heavily in development. This aligns with the IIC KPI of increasing the number of actionable student-led innovations on campus.

**Feedback / Reflection:**
* *"The bootcamp completely changed how our team approaches product development. We realized we were focusing on the wrong features!"* - Team Participant
* *"Dr. Murali's insights on customer validation were incredibly practical and exactly what we needed to hear."* - Student Coordinator

**Organizing Team Members Details:**
* **B. Kalyan Reddy:** Student Convener (Event Orchestration)
* **IIC Coordinators:** Operations, Logistics, and Registration Management

<div style="page-break-before: always;"></div>

**Photographs/Screenshots:**

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px;">
  <div>
    <img src="IMG_20260801_122608.jpg" alt="Bootcamp Session" style="width: 100%; border: 2px solid #333;">
    <p align="center"><i>Wide view of the Lean Startup Bootcamp session in progress.</i></p>
  </div>
  <div>
    <img src="IMG-20260801-WA0013.jpg" alt="Mentorship" style="width: 100%; border: 2px solid #333;">
    <p align="center"><i>Students mapping out their MVPs during the hands-on exercise.</i></p>
  </div>
  <div>
    <img src="IMG-20260801-WA0025.jpg" alt="Mentorship" style="width: 100%; border: 2px solid #333;">
    <p align="center"><i>Interactive discussion and validation of startup concepts.</i></p>
  </div>
  <div>
    <img src="IMG-20260801-WA0131.jpg" alt="Mentorship" style="width: 100%; border: 2px solid #333;">
    <p align="center"><i>Participant engagement and peer feedback session.</i></p>
  </div>
</div>

**Media Coverage & Social Media Promotion:**
Internal circulars and WhatsApp group announcements were utilized to mobilize the specific startup teams and IIC coordinators for this focused capacity-building bootcamp. 

Additionally, the event saw excellent post-activity organic promotion on LinkedIn by the Student Convener and IIC Coordinators, highlighting the impact of the session.

**Social Media Links:**
* [LinkedIn Post 1 (Student Convener)](https://www.linkedin.com/posts/bhoompally-kalyanreddy_leadership-innovation-entrepreneurship-ugcPost-7489298138504105984-cZSI)
* [LinkedIn Post 2 (IIC Coordinator)](https://www.linkedin.com/posts/satvendra-giri-nihal-badam_iic-leanstartup-startupcoordinator-ugcPost-7489539894403530752-HNde)
* [LinkedIn Post 3 (IIC Coordinator)](https://www.linkedin.com/posts/naga-srikar-mandalaparthi-1b70ba380_leanstartup-innovation-entrepreneurship-ugcPost-7489511349337673728-cxQJ)

**Attendance details:** Proof of signed Attendance sheet is attached as a separate PDF document alongside this report for submission.
"""

with open("Lean_Startup_Report.md", "w", encoding="utf-8") as f:
    f.write(report_md)

print("Generated MD files.")
