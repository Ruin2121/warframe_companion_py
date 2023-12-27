from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes
from enum import Enum


class MagPrime(Warframe):
    @property
    def internal_name(self) -> Enum:
        return Warframes.MAG_PRIME
