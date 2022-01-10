import requests
import os

API_KEY = os.getenv('TRELLO_API_KEY')
TOKEN = os.getenv('TRELLO_TOKEN')
BOARD_ID = os.getenv('TRELLO_BOARD_ID')
BASE_URL = "https://api.trello.com/1/"

def convert_trello_list(trello_list):
    items = []
    for card in trello_list['cards']:
        items.append(Item.from_trello_card(card, trello_list))
    return items


def get_to_do_items():
    params = {'key': API_KEY, 'token': TOKEN, 'cards': 'open' }
    to_do_list = requests.get(f"{BASE_URL}boards/{BOARD_ID}/lists", params=params).json()[0]
    global to_do_list_id
    to_do_list_id = to_do_list['id']
    return convert_trello_list(to_do_list)


def get_done_items():
    params = {'key': API_KEY, 'token': TOKEN, 'cards': 'open' }
    done_list = requests.get(f"{BASE_URL}boards/{BOARD_ID}/lists", params=params).json()[2]
    global done_list_id
    done_list_id = done_list['id']
    return convert_trello_list(done_list)


def add_item(title):
    params = {'key': API_KEY, 'token': TOKEN, 'name': title, 'idList': to_do_list_id }
    return requests.post(f"{BASE_URL}cards", params=params)


def complete_item(id):
    params = {'key': API_KEY, 'token': TOKEN, 'idList': done_list_id }
    return requests.put(f"{BASE_URL}cards/{id}", params=params)


class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])
