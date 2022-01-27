import os
import pytest 
from threading import Thread
from todo_app import app
from todo_app.data.trello_items import create_trello_board, delete_trello_board
from dotenv import load_dotenv, find_dotenv 
from selenium import webdriver

@pytest.fixture(scope='module')
def app_with_temp_board():

    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

    # Create the new board & update the board id environment variable
    board_id = create_trello_board('test board')
    os.environ['TRELLO_BOARD_ID'] = board_id

    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'