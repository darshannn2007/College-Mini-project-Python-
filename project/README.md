# Student Management System (SMS)

A simple, lightweight web application built to manage student records and track academic performance. This project replaces traditional command-line interfaces with a clean web GUI using **Flask** for the backend logic and dynamic **HTML/CSS/JS** for the frontend. 

It handles complete CRUD operations and automatically calculates class statistics, subject averages, and identifies the top performer.

---

## 🚀 Key Features

* **Interactive Dashboard:** A centralized landing page with an easy-to-use navigation bar.
* **Add Student Records:** Simple form interface to save student profiles (Name, Age, Class, Gender) along with internal marks for **Mathematics, PPS, Economics, and Physics**.
* **View Ledger:** Pulls data from the dynamic data store and renders it cleanly in a structured HTML table.
* **Search Engine:** Built-in string matching that lets you search students by typing full or partial names.
* **Update Marks:** Allows quick modification of subject scores via unique Student IDs.
* **Delete Records:** Safely removes data entries from the system with a red alert/warning prompt to prevent accidental deletions.
* **Performance Analytics:** No manual math required. Automatically outputs:
    * Overall Class Average
    * Top Performer of the batch
    * Subject-wise breakdowns (Highest, Lowest, and Average marks for each subject)

---

## 🛡️ Input Validation (Client-Side)

To avoid junk data or fat-finger entry errors, we implemented a custom validation script in `script.js`:
* **Range Enforcement:** Automatically checks all numeric inputs on form submission.
* **Bound Checking:** Restricts marks strictly between **0 and 100**. If a user enters a negative value or something above 100, a browser alert pops up immediately and blocks the backend submission.

---

## 📁 Project Directory Structure

```text
├── app.py                 # Core Flask backend (routes, logic, data array)
├── static/
│   ├── style.css          # UI styling, responsive design rules, table presets
│   └── script.js          # JavaScript client-side input checking logic
└── templates/
    ├── base.html          # Parent layout file (contains navbar & boilerplate)
    ├── index.html         # Dashboard home view
    ├── add_student.html   # Form to insert a new student record
    ├── view_students.html # Tabular view showing all student records
    ├── search.html        # Filter / search UI
    ├── update.html        # Score editing page
    ├── delete.html        # Record removal panel (with database warning)
    └── average.html       # Automated class stats & analytics charts
