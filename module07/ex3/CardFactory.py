from abc import ABC
from typing import Union
from ex0.Card import Card


class CardFactory(ABC):
    def create_creature(self,
                        name_or_power: Union[str, int, None] = None) -> Card:
        raise NotImplementedError(
            "create_creature() must be implemented by subclass"
        )

    def create_spell(self,
                     name_or_power: Union[str, int, None] = None) -> Card:
        raise NotImplementedError(
            "create_spell() must be implemented by subclass"
        )

    def create_artifact(self,
                        name_or_power: Union[str, int, None] = None) -> Card:
        raise NotImplementedError(
            "create_artifact() must be implemented by subclass"
        )

    def create_themed_deck(self, size: int) -> dict:
        raise NotImplementedError(
            "create_themed_deck() must be implemented by subclass"
        )

    def get_supported_types(self) -> dict:
        raise NotImplementedError(
            "get_supported_types() must be implemented by subclass"
        )
