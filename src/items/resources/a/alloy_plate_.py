from src.base_classes.item import Item
from src.base_classes.recipe import Recipe
from src.enumerations.resources import Resources
from enum import Enum


class AlloyPlate(Item):
    @property
    def internal_name(self) -> Enum:
        return Resources.ALLOY_PLATE

    @property
    def recipe(self) -> Recipe | None:
        return None
