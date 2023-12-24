from src.base_classes.singleton_base import SingletonBase


class InventoryMenu(SingletonBase):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)
