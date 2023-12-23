from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes


class GarudaPrime(Warframe):
    @property
    def internal_name(self) -> Warframes:
        return Warframes.GARUDA_PRIME
