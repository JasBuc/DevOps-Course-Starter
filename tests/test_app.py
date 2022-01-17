from todo_app.data.trello_items import Item, convert_trello_list

# TODO - Also need to document how to run tests in the readme - should include running from terminal - should include running individually or as a whole
# TODO - poetry run pytest or poetry run pytest path/to/test_file from a terminal
# TODO - Get the NoneType error mentioned for integration test when run from terminal - see recording
# TODO - Update read me about integration and end to end tests too? 

# TODO - If you have an e2e test, the e2e test loads real credentials and performs some browser interaction resulting in requests to Trello

# TODO - Can I change integration tests to use test_board_id or something, look through hints maybe im overwriting env vars in wrong order or smth 

def test_convert_trello_list():
    trello_list = {'id': '123', 'name': 'To Do', 'idBoard': '456', 'cards': [{'id': '789', 'name': 'Item Name'}]}
    assert convert_trello_list(trello_list)[0].id == '789'
    assert convert_trello_list(trello_list)[0].name == 'Item Name'
    assert convert_trello_list(trello_list)[0].status == 'To Do'