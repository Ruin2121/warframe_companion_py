from abc import ABC
from singleton_base import SingletonBase


class Item(ABC, SingletonBase):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)
