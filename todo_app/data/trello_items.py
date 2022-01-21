import requests
import os

BASE_URL = "https://api.trello.com/1/"

def convert_trello_list(trello_list):
    items = []
    for card in trello_list['cards']:
        items.append(Item.from_trello_card(card, trello_list))
    print(items)
    return items


def get_to_do_items():
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'cards': 'open' }
    to_do_list = requests.get(f"{BASE_URL}boards/{os.getenv('TRELLO_BOARD_ID')}/lists", params=params).json()[0]
    return convert_trello_list(to_do_list)

def get_doing_items():
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'cards': 'open' }
    doing_list = requests.get(f"{BASE_URL}boards/{os.getenv('TRELLO_BOARD_ID')}/lists", params=params).json()[1]
    return convert_trello_list(doing_list)

def get_done_items():
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'cards': 'open' }
    done_list = requests.get(f"{BASE_URL}boards/{os.getenv('TRELLO_BOARD_ID')}/lists", params=params).json()[2]
    return convert_trello_list(done_list)


def add_item(title):
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'cards': 'open' }
    to_do_list_id = requests.get(f"{BASE_URL}boards/{os.getenv('TRELLO_BOARD_ID')}/lists", params=params).json()[0]['id']
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'name': title, 'idList': to_do_list_id }
    return requests.post(f"{BASE_URL}cards", params=params)


def complete_item(id):
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'cards': 'open' }
    done_list_id = requests.get(f"{BASE_URL}boards/{os.getenv('TRELLO_BOARD_ID')}/lists", params=params).json()[2]['id']
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'idList': done_list_id }
    return requests.put(f"{BASE_URL}cards/{id}", params=params)

def create_trello_board(name):
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN'), 'name': name}
    response = requests.post(f"{BASE_URL}boards", params=params)
    return response.json()['id']

def delete_trello_board(id):
    params = {'key': os.getenv('TRELLO_API_KEY'), 'token': os.getenv('TRELLO_TOKEN')}
    requests.delete(f"{BASE_URL}boards/{id}", params=params)

class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])
