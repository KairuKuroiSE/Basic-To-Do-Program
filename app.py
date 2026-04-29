from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This is the "Database" (Don't judge)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    task_deadline = request.form.get('deadline')

    if task_content:
        # We ensure every task starts with 'complete': False
        tasks.append({'content': task_content, 'deadline': task_deadline, 'complete': False})
    
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    # This logic checks if the ID is valid, then flips the status
    if 0 <= task_id < len(tasks):
        tasks[task_id]['complete'] = not tasks[task_id]['complete']
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)