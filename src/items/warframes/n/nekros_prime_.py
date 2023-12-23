from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes


class NekrosPrime(Warframe):
    @property
    def internal_name(self) -> Warframes:
        return Warframes.NEKROS_PRIME
