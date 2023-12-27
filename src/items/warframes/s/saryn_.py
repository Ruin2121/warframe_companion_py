from enum import Enum

from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes


class Saryn(Warframe):
    @property
    def internal_name(self) -> Enum:
        return Warframes.SARYN
