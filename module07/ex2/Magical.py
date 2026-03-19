from abc import ABC


class Magical(ABC):
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        raise NotImplementedError(
            "cast_spell() must be implemented by subclass"
        )

    def channel_mana(self, amount: int) -> dict:
        raise NotImplementedError(
            "channel_mana() must be implemented by subclass"
        )

    def get_magic_stats(self) -> dict:
        raise NotImplementedError(
            "get_magic_stats() must be implemented by subclass"
        )
