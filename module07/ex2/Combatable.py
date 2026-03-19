from abc import ABC


class Combatable(ABC):
    def attack(self, target) -> dict:
        raise NotImplementedError("attack() must be implemented by subclass")

    def defend(self, incoming_damage: int) -> dict:
        raise NotImplementedError("defend() must be implemented by subclass")

    def get_combat_stats(self) -> dict:
        raise NotImplementedError(
            "get_combat_stats() must be implemented by subclass"
        )
