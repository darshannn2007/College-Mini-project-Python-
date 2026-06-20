import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash_messages' # Necessary for flash messages

DATA_FILE = 'data.json'

# --- DATA HANDLING ---
def load_data():
    """Load students from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(students):
    """Save students to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)

def get_next_id(students):
    """Calculate the next available student ID."""
    if not students:
        return 1
    return max(student['student_id'] for student in students) + 1

# --- ROUTES ---

@app.route('/')
def home():
    """Homepage: Shows the menu dashboard."""
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Adds a new student."""
    if request.method == 'POST':
        students = load_data()
        
        name = request.form.get('name').strip().title()
        age = int(request.form.get('age'))
        student_class = request.form.get('class').strip()
        gender = request.form.get('gender')
        
        maths = float(request.form.get('maths'))
        pps = float(request.form.get('pps'))
        eco = float(request.form.get('eco'))
        phy = float(request.form.get('phy'))

        student = {
            'student_id': get_next_id(students),
            'name': name,
            'age': age,
            'class': student_class,
            'gender': gender,
            'grades': {
                'Mathematics': maths,
                'PPS': pps,
                'Economics': eco,
                'Physics': phy
            }
        }

        students.append(student)
        save_data(students)
        
        flash(f"Student '{name}' added successfully!", "success")
        return redirect(url_for('view_students'))

    return render_template('add_student.html')

@app.route('/view')
def view_students():
    """Displays table of all students."""
    students = load_data()
    return render_template('view_students.html', students=students)

@app.route('/search', methods=['GET', 'POST'])
def search_student():
    """Search for a student by name."""
    found_students = []
    search_term = ""
    
    if request.method == 'POST':
        students = load_data()
        search_term = request.form.get('search_name', '').strip().lower()
        
        for student in students:
            if search_term in student['name'].lower():
                found_students.append(student)
        
        if not found_students and search_term:
            flash(f"No students found matching '{search_term}'.", "error")
    
    return render_template('search.html', students=found_students, search_term=search_term)

@app.route('/update', methods=['GET', 'POST'])
def update_marks():
    """Update marks based on Student ID."""
    if request.method == 'POST':
        students = load_data()
        try:
            s_id = int(request.form.get('student_id'))
        except ValueError:
            flash("Invalid Student ID.", "error")
            return redirect(url_for('update_marks'))

        student_found = None
        for student in students:
            if student['student_id'] == s_id:
                student_found = student
                break
        
        if student_found:
            student_found['grades']['Mathematics'] = float(request.form.get('maths'))
            student_found['grades']['PPS'] = float(request.form.get('pps'))
            student_found['grades']['Economics'] = float(request.form.get('eco'))
            student_found['grades']['Physics'] = float(request.form.get('phy'))
            save_data(students)
            flash(f"Marks updated successfully for {student_found['name']}.", "success")
            return redirect(url_for('view_students'))
        else:
            flash(f"Error: Student ID {s_id} not found.", "error")

    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_student():
    """Delete a student record by Student ID."""
    if request.method == 'POST':
        students = load_data()
        try:
            s_id = int(request.form.get('student_id'))
        except ValueError:
            flash("Invalid Student ID.", "error")
            return redirect(url_for('delete_student'))
        
        student_found = None
        for i, student in enumerate(students):
            if student['student_id'] == s_id:
                student_found = student
                students.pop(i)
                break
        
        if student_found:
            save_data(students)
            flash(f"Student '{student_found['name']}' (ID: {s_id}) has been deleted.", "success")
            return redirect(url_for('view_students'))
        else:
            flash(f"Error: Student ID {s_id} not found.", "error")

    return render_template('delete.html')

@app.route('/average')
def class_average():
    """Calculates class average and top performer."""
    students = load_data()
    
    if not students:
        flash("No student data available to calculate averages.", "error")
        return render_template('average.html', error=True)

    student_averages = []
    for student in students:
        total = sum(student['grades'].values())
        avg = total / len(student['grades']) if student['grades'] else 0
        student_averages.append({'name': student['name'], 'average': avg})

    class_total = sum(s['average'] for s in student_averages)
    class_avg = class_total / len(student_averages)

    top_student = max(student_averages, key=lambda x: x['average'])

    subjects = ['Mathematics', 'PPS', 'Economics', 'Physics']
    subject_stats = {}
    
    for sub in subjects:
        marks = [s['grades'].get(sub, 0) for s in students]
        if marks:
            subject_stats[sub] = {
                'avg': sum(marks) / len(marks),
                'max': max(marks),
                'min': min(marks)
            }

    return render_template('average.html', 
                           class_avg=round(class_avg, 2), 
                           top_student=top_student, 
                           subject_stats=subject_stats)

if __name__ == '__main__':
    app.run(debug=True)