from enum import Enum

from src.base_classes.blueprint import Blueprint
from src.base_classes.recipe import Recipe
from src.enumerations.blueprints import Blueprints


class AshBlueprint(Blueprint):
    @property
    def internal_name(self) -> Enum:
        return Blueprints.ASH_BLUEPRINT

    @property
    def recipe(self) -> Recipe | None:
        return None
