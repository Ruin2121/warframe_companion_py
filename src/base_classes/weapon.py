from item import Item


class Weapon(Item):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)
