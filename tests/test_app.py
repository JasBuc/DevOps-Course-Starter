from todo_app.data.trello_items import convert_trello_list

def test_convert_trello_list():
    trello_list = {'id': '123', 'name': 'To Do', 'idBoard': '456', 'cards': [{'id': '789', 'name': 'Item Name'}]}
    assert convert_trello_list(trello_list)[0].id == '789'
    assert convert_trello_list(trello_list)[0].name == 'Item Name'
    assert convert_trello_list(trello_list)[0].status == 'To Do'