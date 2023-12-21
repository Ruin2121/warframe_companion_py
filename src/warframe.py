from item import Item


class Warframe(Item):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)
