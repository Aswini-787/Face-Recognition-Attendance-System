# Face Recognition Attendance and Alert System

## Overview

The Face Recognition Attendance and Alert System is an automated attendance management application built using Python. It uses facial recognition technology to detect and identify individuals through a webcam and mark attendance automatically.

The system records attendance digitally and can also send alert emails for absentees or attendance updates, making attendance tracking faster, easier, and more accurate.

---

## Features

* Real-time face detection and recognition
* Automatic attendance marking
* Attendance storage using CSV / Excel
* Email alert system for absentees
* Teacher notification support
* Attendance report generation
* Simple desktop interface using Tkinter

---

## Technologies Used

* Python
* OpenCV
* Tkinter
* OpenPyXL
* Matplotlib

### Python Modules Used

* `tkinter`
* `openpyxl`
* `matplotlib`
* `csv`
* `os`
* `sys`
* `threading`
* `smtplib`
* `datetime`

---

## Project Structure

```bash
Face-Recognition-Attendance-System/
│
├── Loginpage.py
├──
├── alertemails.py
├── sendteacher.py
├── README.md
├── requirements.txt
├── images/
└── attendance/
```

## How It Works

1. The webcam captures live video.
2. The system detects and recognizes faces.
3. Attendance is marked automatically for identified individuals.
4. Attendance data is saved in CSV/Excel files.
5. Email alerts can be sent to notify absentees or teachers.
6. Reports can be generated and visualized.

---

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## Applications

* School attendance management
* College attendance management
* Employee attendance tracking
* Event check-in systems

---

## Future Improvements

* Database integration
* Web dashboard
* Cloud-based attendance storage
* Mobile application support
* Advanced analytics

---

## Author

S Aswini and Vishruth Arulselvam
