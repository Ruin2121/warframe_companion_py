from enum import Enum

from src.base_classes.item import Item
from src.base_classes.recipe import Recipe
from src.enumerations.resources import Resources


class NeuralSensors(Item):
    @property
    def internal_name(self) -> Enum:
        return Resources.NEURAL_SENSORS

    @property
    def recipe(self) -> Recipe | None:
        return None
