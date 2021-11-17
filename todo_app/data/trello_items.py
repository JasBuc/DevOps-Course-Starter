import requests, os

#refactor way I include key/id/token
API_KEY = os.getenv('TRELLO_API_KEY')
TOKEN = os.getenv('TRELLO_TOKEN')
BOARD_ID = os.getenv('TRELLO_BOARD_ID')

def get_to_do_items():
    to_do_list = requests.get(f"https://api.trello.com/1/boards/{BOARD_ID}/lists?key={API_KEY}&token={TOKEN}&cards=open").json()[0]
    global to_do_list_id 
    to_do_list_id = to_do_list['id']
    return to_do_list['cards']

def get_done_items():
    done_list = requests.get(f"https://api.trello.com/1/boards/{BOARD_ID}/lists?key={API_KEY}&token={TOKEN}&cards=open").json()[2]
    global done_list_id 
    done_list_id = done_list['id']
    return done_list['cards']

def add_item(title):
    return requests.post(f"https://api.trello.com/1/cards?key={API_KEY}&token={TOKEN}&name={title}&idList={to_do_list_id}")

def complete_item(id):
    return requests.put(f"https://api.trello.com/1/cards?key={API_KEY}&token={TOKEN}&id={id}&idList={done_list_id}")
    