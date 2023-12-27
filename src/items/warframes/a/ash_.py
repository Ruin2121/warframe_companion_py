from enum import Enum

from src.base_classes.recipe import Recipe
from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes
from src.items.blueprints import AshBlueprint
from src.items.warframe_components import AshNeuroptics


class Ash(Warframe):
    @property
    def internal_name(self) -> Enum:
        return Warframes.ASH

    @property
    def recipe(self) -> Recipe | None:
        return Recipe(
            ingredient_blueprint=AshBlueprint(),
            ingredient_credits=25_000,
            ingredient_1=(AshNeuroptics(), 1),
            ingredient_2=,
            ingredient_3=,
            ingredient_4=,
        )
