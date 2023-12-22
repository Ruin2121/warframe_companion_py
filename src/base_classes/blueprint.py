from item import Item


class Blueprint(Item):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)
