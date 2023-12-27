from abc import ABC

from src.base_classes.item import Item
from src.meta_data import SUBSUMABLE
from player_data import SUBSUME_STATUS


class Warframe(Item, ABC):
    @property
    def subsumable(self) -> bool:
        return SUBSUMABLE[self.internal_name]

    @property
    def subsume_status(self) -> bool:
        return SUBSUME_STATUS[self.internal_name] if self.subsumable else False
