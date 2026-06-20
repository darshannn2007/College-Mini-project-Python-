# Student Management System 🎓

A full-stack web application built using **Flask (Python)**, **HTML5/CSS3 (with glassmorphic UI elements)**, and **JavaScript**. This project serves as a comprehensive tool to manage student profiles, handle academic mark entries for key subjects, track real-time analytics like class averages, and identify top performers. 

Built as part of the B.Tech academic curriculum submission / mini-project coursework.

---

## 🚀 Features

* **Dashboard Overview:** Clean, interactive UI panel built with modern CSS grids and hover animations.
* **CRUD Operations:** Fully functional backend logic to **Add**, **View**, **Update**, and **Delete** student records seamlessly.
* **Persistent Storage:** Data is stored locally using a structured `data.json` database, preventing loss on server restarts.
* **Search Engine:** Quick lookup functionality supporting partial or full name string matching.
* **Real-time Frontend Validation:** Built-in client-side validation logic using JavaScript to restrict subject marks strictly between `0` and `100` before submission.
* **Class Analytics & Insights:** Dynamic calculation of overall class average scores and automated tracking of individual subject performance metrics (Highest, Lowest, and Average marks).

---

## 🛠️ Tech Stack & Concepts Used

* **Backend Framework:** Python Flask
* **Frontend Design:** HTML5, CSS3 (Glassmorphism, CSS Custom Grids, FontAwesome Icons)
* **Client Validation:** JavaScript (DOM Manipulation & Form Validation events)
* **Database File System:** JSON Serializer Serialization/Deserialization
* **Concepts applied:** Dynamic Routing, Session Flash Messages, Templating Engine (Jinja2).

---

## 🗂️ Repository Structure

```text
├── app.py                 # Core Flask Application & Route Handlers
├── data.json              # Local Database file storing JSON objects
├── static/
│   ├── style.css          # Global stylesheet containing Glassmorphism & Animations
│   └── script.js          # JS code handling client validation & flash message fades
└── templates/             # Jinja2 HTML Templates
    ├── base.html          # Global Parent Layout Template
    ├── index.html         # Dashboard Hub Homepage
    ├── add_student.html   # Student Entry Enrollment Form
    ├── view_students.html # Student Records Data Table View
    ├── search.html        # Name Search Engine page
    ├── update.html        # Marks Modification Panel
    ├── delete.html        # Record Purge View with safety prompts
    └── average.html       # Analytics & Top Performer metrics view
