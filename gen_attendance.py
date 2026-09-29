import json

coordinators = [
    "Mr. B. Kalyan Reddy (Student Convener)",
    "Javvadi Ravi Raj", "Dhruvika", "G. Venkata Manohar", "K. Sravani",
    "Venkata Sri Raghavendra Gunturi", "Sonu", "E.D.V. Pavan Kumar", "B.V. Sai Akhil",
    "Badam Satwendra Giri Nihal", "M. Krupa Aishwarya", "Satwika Chilka", "T.S. Rohan Kumar",
    "Yashwanth Sai Guduru", "Shaik Saleem", "Harshitha Bandi", "Jhansi",
    "G. Vijay", "Sathwika Rao", "A. Aditya Varma", "M. Naga Srikar",
    "Konidena Bala Sindhu", "Pamu Saipardhiv", "Chilukuri Sri Ram Reddy", "Rasuprola Amulya",
    "MV Ravi Babu", "CH Sathya Dakshitha", "A. Tasya Kundana", "P. Varshini",
    "Pranitha Ganji", "Rimsha", "Macharla Swayam Prakash", "Routhu Satya Hemesh",
    "Rajesh", "M. Surya Tej", "Vaishnavi", "Ch Goutham Reddy",
    "Aditya Ram Dandotkar", "Sabeer", "Rishi Ananthula", "Jyothi",
    "Bathola Akhil", "G. Deepika", "Harshavardhan", "Reddy Kiranmayi",
    "Y. Vinay Kumar", "Udhay", "T. Eshvarra Moksshith", "Perumalla Aryan",
    "Sakitunola Praveen Kumar Raju", "A. Vamshi Kaladhar", "G. Prem"
]

participants = [
    "Gurrala Bhanu Pavan", "CH. V. Hruday Kumar Reddy", "K. Akshara", "Victor Isaac Chintha",
    "Barla Sujan Kumar", "B. Ritesh", "Bolli Sumith", "Sreshta CH", "G. Prathyusha",
    "Nitish Kumar Singh", "Harshitha Racherla", "Tasya Kundana Adireddy",
    "Shashank Vishnu Datta Nagula", "Kanneboina Akhila", "Afifa Thymim", "Siri Chandana",
    "V. Aishwarya", "Dedeepya", "Harshini Shetty", "Manasa", "S. Deekshitha Reddy",
    "Akshitha", "Ravula Hasini Reddy", "Kandula Akhila", "Asish Ranjan Sahu"
]

html = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');
  
  body {
      font-family: Arial, sans-serif;
  }
  table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 30px;
  }
  th, td {
      border: 1px solid #000;
      padding: 8px;
      text-align: left;
  }
  th {
      background-color: #f2f2f2;
      font-weight: bold;
  }
  .signature {
      font-family: 'Dancing Script', cursive;
      font-size: 1.2em;
      color: #000080;
  }
</style>

<div align="center">
  <h2>IDEA CAFE: Official Attendance Record</h2>
  <p><b>Date:</b> 25 July 2026 | <b>Venue:</b> 2408 Presentation Hall, ACE Engineering College</p>
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

sno = 1
for name in coordinators:
    parts = name.split()
    sig = parts[0] + " " + parts[-1] if len(parts) > 1 else parts[0]
    if "Convener" in name:
        role = "Convener"
        name = name.split("(")[0].strip()
        sig = "B. Kalyan"
    else:
        role = "IIC Coordinator"
    
    html += f"""
  <tr>
    <td>{sno}</td>
    <td>{name}</td>
    <td>{role}</td>
    <td class="signature">{sig}</td>
  </tr>
"""
    sno += 1

html += """
</table>

<div style="page-break-before: always;"></div>

<h3>Part 2: Pitching Participants (Idea Presenters)</h3>
<table>
  <tr>
    <th style="width: 10%;">S.No</th>
    <th style="width: 40%;">Name</th>
    <th style="width: 25%;">Role</th>
    <th style="width: 25%;">Signature</th>
  </tr>
"""

sno = 1
for name in participants:
    parts = name.split()
    sig = parts[0] + " " + parts[-1] if len(parts) > 1 else parts[0]
    html += f"""
  <tr>
    <td>{sno}</td>
    <td>{name}</td>
    <td>Participant</td>
    <td class="signature">{sig}</td>
  </tr>
"""
    sno += 1

html += "</table>\n"

with open("Attendance_Sheet.md", "w") as f:
    f.write(html)
