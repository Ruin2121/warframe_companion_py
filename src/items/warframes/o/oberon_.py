from src.base_classes.warframe import Warframe
from src.enumerations.warframes import Warframes


class Oberon(Warframe):
    @property
    def internal_name(self) -> Warframes:
        return Warframes.OBERON