from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes
from enum import Enum


class HarrowPrime(Warframe):
    @property
    def internal_name(self) -> Enum:
        return Warframes.HARROW_PRIME
