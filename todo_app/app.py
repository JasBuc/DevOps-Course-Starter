from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config

from todo_app.data.trello_items import get_done_items, get_to_do_items, add_item, complete_item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    to_do_items = get_to_do_items()
    done_items = get_done_items()
    return render_template('index.html', to_do_items=to_do_items, done_items=done_items)

@app.route('/submit', methods=['POST'])
def addItem():
    newItem = request.form.get('title')
    add_item(newItem)
    return redirect('/')

@app.route('/completeItem')
def completeItem():
    complete_item(id)
    return redirect('/')