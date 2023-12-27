from enum import Enum

from src.base_classes.item import Item
from src.base_classes.recipe import Recipe
from src.enumerations.warframe_components import WarframeComponents
from src.items.blueprints.a.ash_neuroptics_blueprint_ import AshNeuropticsBlueprint
from src.items.resources import AlloyPlate, NeuralSensors, PolymerBundle, Rubedo


class AshNeuroptics(Item):
    @property
    def internal_name(self) -> Enum:
        return WarframeComponents.ASH_NEUROPTICS

    @property
    def recipe(self) -> Recipe | None:
        return Recipe(
            ingredient_blueprint=AshNeuropticsBlueprint(),
            ingredient_credits=15_000,
            ingredient_1=(AlloyPlate(), 150),
            ingredient_2=(NeuralSensors(), 1),
            ingredient_3=(PolymerBundle(), 150),
            ingredient_4=(Rubedo(), 500),
        )
