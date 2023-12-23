from abc import ABC, abstractmethod
from typing import Type
from enum import Enum
from singleton_base import SingletonBase


class Item(ABC, SingletonBase):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)

    @property
    @abstractmethod
    def internal_name(self) -> Type[Enum]:
        """
        Expected to return an Enumeration.
        """
