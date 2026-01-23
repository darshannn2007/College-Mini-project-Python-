from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- GLOBAL DATA STORAGE (Same as your code) ---
students = []
student_id_counter = 1

# --- ROUTES (Connecting URLS to Functions) ---

@app.route('/')
def home():
    """Homepage: Shows the menu buttons."""
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Adds a new student."""
    global student_id_counter
    
    if request.method == 'POST':
        # 1. Get data from HTML Form instead of input()
        name = request.form.get('name').title()
        age = int(request.form.get('age'))
        student_class = request.form.get('class')
        gender = request.form.get('gender')
        
        # 2. Get marks
        maths = float(request.form.get('maths'))
        pps = float(request.form.get('pps'))
        eco = float(request.form.get('eco'))
        phy = float(request.form.get('phy'))

        # 3. Create Dictionary (Exactly like your original code)
        student = {
            'student_id': student_id_counter,
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

        # 4. Save and Increment
        students.append(student)
        student_id_counter += 1
        
        # Redirect to view page to see the result
        return redirect(url_for('view_students'))

    return render_template('add_student.html')

@app.route('/view')
def view_students():
    """Displays table of all students."""
    return render_template('view_students.html', students=students)

@app.route('/search', methods=['GET', 'POST'])
def search_student():
    """Search for a student by name."""
    found_students = []
    search_term = ""
    
    if request.method == 'POST':
        search_term = request.form.get('search_name').lower()
        
        # Logic from your original code
        for student in students:
            if search_term in student['name'].lower():
                found_students.append(student)
    
    return render_template('search.html', students=found_students, search_term=search_term)

@app.route('/update', methods=['GET', 'POST'])
def update_marks():
    """Update marks based on Student ID."""
    message = ""
    
    if request.method == 'POST':
        s_id = int(request.form.get('student_id'))
        
        # Find student
        student_found = None
        for student in students:
            if student['student_id'] == s_id:
                student_found = student
                break
        
        if student_found:
            # Update the marks in the dictionary
            student_found['grades']['Mathematics'] = float(request.form.get('maths'))
            student_found['grades']['PPS'] = float(request.form.get('pps'))
            student_found['grades']['Economics'] = float(request.form.get('eco'))
            student_found['grades']['Physics'] = float(request.form.get('phy'))
            message = f"Success! Marks updated for {student_found['name']}."
        else:
            message = "Error: Student ID not found."

    return render_template('update.html', message=message)

@app.route('/delete', methods=['GET', 'POST'])
def delete_student():
    """Delete a student record by Student ID."""
    message = ""
    message_type = ""
    
    if request.method == 'POST':
        s_id = int(request.form.get('student_id'))
        
        # Find and delete student
        student_found = None
        for i, student in enumerate(students):
            if student['student_id'] == s_id:
                student_found = student
                students.pop(i)  # Remove student from list
                break
        
        if student_found:
            message = f"Success! Student '{student_found['name']}' (ID: {s_id}) has been deleted."
            message_type = "success"
        else:
            message = f"Error: Student ID {s_id} not found."
            message_type = "error"

    return render_template('delete.html', message=message, message_type=message_type)

@app.route('/average')
def class_average():
    """Calculates class average and top performer."""
    if not students:
        return render_template('average.html', error="No students data available.")

    # 1. Logic for Student Averages
    student_averages = []
    for student in students:
        total = sum(student['grades'].values())
        avg = total / 4  # 4 subjects
        student_averages.append({'name': student['name'], 'average': avg})

    # 2. Logic for Class Average
    class_total = sum(s['average'] for s in student_averages)
    class_avg = class_total / len(student_averages)

    # 3. Logic for Top Performer
    top_student = max(student_averages, key=lambda x: x['average'])

    # 4. Subject Wise Logic
    subjects = ['Mathematics', 'PPS', 'Economics', 'Physics']
    subject_stats = {}
    
    for sub in subjects:
        marks = [s['grades'][sub] for s in students]
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