# MediCare — Healthcare Management System

MediCare is a beginner portfolio project demonstrating a small patient-management web application built with Python, Flask, SQLite, HTML, and CSS.

## Current features
- Add a patient record with name, age, phone, and reason for visit
- View all saved patient records
- Delete a patient record
- Display a total-patient count
- Validate required fields and age input
- Store records in a local SQLite database

## Run locally (Windows)
1. Install Python and Git if they are not already installed.
2. Extract this project folder.
3. Open the `MediCare` folder in VS Code.
4. Open **Terminal → New Terminal**.
5. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
6. Activate it:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt terminal and run:
   ```cmd
   .venv\Scripts\activate.bat
   ```
7. Install Flask:
   ```powershell
   python -m pip install -r requirements.txt
   ```
8. Start the app:
   ```powershell
   python app.py
   ```
9. Open `http://127.0.0.1:5000` in your browser.

The SQLite database file `medicare.db` is created automatically the first time the app runs.

## Project structure
```text
MediCare/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Important limitations
This is an educational demonstration, not a production healthcare system. It has no login, access control, encryption, audit logging, backup process, or clinical validation. Do not enter real patient information. Use fictional sample data only.

## Next improvements
- Add doctor profiles and appointment scheduling
- Add login and role-based access
- Add automated tests
- Add search and filtering
- Improve input validation and security
