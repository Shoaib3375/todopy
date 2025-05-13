from flask import Blueprint, render_template, request, redirect
import task_manager

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/')
def index():
    tasks = task_manager.load_tasks()
    return render_template('index.html', tasks=tasks)

@task_routes.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    if content:
        task_manager.add_task(content)
    return redirect('/')

@task_routes.route('/complete/<int:id>')
def complete(id):
    task_manager.toggle_task_completion(id)
    return redirect('/')

@task_routes.route('/delete/<int:id>')
def delete(id):
    task_manager.delete_task(id)
    return redirect('/')
