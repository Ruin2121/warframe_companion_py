from abc import ABC, abstractmethod
from typing import Type
from enum import Enum
from src.base_classes.singleton_base import SingletonBase


class Item(ABC, SingletonBase):
    @property
    @abstractmethod
    def internal_name(self) -> Type[Enum]:
        """
        Expected to return an Enumeration.
        """

    @property
    def external_name(self) -> str:
        return self.internal_name.value
