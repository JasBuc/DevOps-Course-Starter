class ViewModel:
    def __init__(self, to_do_items, doing_items, done_items):
        self._to_do_items = to_do_items
        self._doing_items = doing_items
        self._done_items = done_items

    @property 
    def to_do_items(self): 
        return self._to_do_items

    @property 
    def doing_items(self): 
        return self._doing_items

    @property 
    def done_items(self): 
        return self._done_items