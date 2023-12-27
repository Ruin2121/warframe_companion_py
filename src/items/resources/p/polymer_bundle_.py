from enum import Enum

from src.base_classes.item import Item
from src.base_classes.recipe import Recipe
from src.enumerations.resources import Resources


class PolymerBundle(Item):
    @property
    def internal_name(self) -> Enum:
        return Resources.POLYMER_BUNDLE

    @property
    def recipe(self) -> Recipe | None:
        return None
