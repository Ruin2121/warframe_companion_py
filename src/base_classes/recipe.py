from src.base_classes.item import Item
from typing import Type
from src.base_classes.blueprint import Blueprint


class Recipe:
    def __init__(
        self,
        ingredient_blueprint: Blueprint,
        ingredient_credits: int,
        ingredient_1: tuple[Item, int],
        ingredient_2: tuple[Item, int],
        ingredient_3: tuple[Item, int],
        ingredient_4: tuple[Item, int],
    ):
        self.ingredient_blueprint = ingredient_blueprint
        self.ingredient_credits = ingredient_credits
        self.ingredient_1 = ingredient_1
        self.ingredient_2 = ingredient_2
        self.ingredient_3 = ingredient_3
        self.ingredient_4 = ingredient_4
