from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This is the "Database" (Don't judge)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # 1. Gather data from the form
    task_content = request.form.get('content')
    t_time = request.form.get('deadline_time')
    t_date = request.form.get('deadline_date')

    # 2. Check if the user actually typed a task
    if task_content:
        # Combine date and time into one readable string
        full_deadline = f"{t_date} at {t_time}" if t_date and t_time else t_date or t_time
        
        # 3. Add the new task to our list
        tasks.append({
            'content': task_content, 
            'deadline': full_deadline, 
            'complete': False
        })
    
    # 4. Send the user back to the home page
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    # This logic checks if the ID is valid, then flips the status
    if 0 <= task_id < len(tasks):
        tasks[task_id]['complete'] = not tasks[task_id]['complete']
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)