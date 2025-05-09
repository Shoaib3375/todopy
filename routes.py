from flask import Blueprint, render_template, request, redirect
from models import Task
from database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    if content:
        task = Task(content=content)
        db.session.add(task)
        db.session.commit()
    return redirect('/')

@main.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect('/')

@main.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')
