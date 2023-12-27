from abc import ABC, abstractmethod
from enum import Enum

from player_data.inventory import INVENTORY
from src.base_classes.recipe import Recipe
from src.base_classes.singleton_base import SingletonBase


class Item(ABC, SingletonBase):
    @property
    @abstractmethod
    def internal_name(self) -> Enum:
        """
        Returns the internal name of the item.

        Returns:
            Enum: The internal name as an Enumeration.
        """

    @property
    def external_name(self) -> str:
        """
        Returns the external name of the item.

        Returns:
            str: The external name of the item.
        """
        return self.internal_name.value

    @property
    def quantity_owned(self) -> int:
        """
        Returns the quantity of the item owned.

        Returns:
            int: The quantity of the item owned.
        """

        return INVENTORY[self.internal_name]

    @property
    @abstractmethod
    def recipe(self) -> Recipe | None:
        """
        Returns the recipe of the item, if there is one.

        Returns:
            Recipe | None: the recipe class of the item, or None if applicable.
        """
