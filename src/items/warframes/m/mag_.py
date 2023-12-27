from enum import Enum

from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes


class Mag(Warframe):
    @property
    def internal_name(self) -> Enum:
        return Warframes.MAG
