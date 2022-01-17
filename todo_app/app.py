from flask import Flask, render_template, request, redirect
from todo_app.ViewModel import ViewModel
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_to_do_items, get_doing_items, get_done_items, add_item, complete_item

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        item_view_model = ViewModel(get_to_do_items(), get_doing_items(), get_done_items())
        return render_template('index.html', view_model=item_view_model)

    @app.route('/submit', methods=['POST'])
    def addItem():
        newItem = request.form.get('title')
        add_item(newItem)
        return redirect('/')

    @app.route('/completeItem<id>')
    def complete_item_route(id):
        complete_item(id)
        return redirect('/')

    return app