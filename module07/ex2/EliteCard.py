from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 power: int, mana: int):
        super().__init__(name, cost, rarity)
        self._power = power
        self._mana = mana

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Elite", "attack": self._power,
                     "mana": self._mana})
        return info

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed with combat and magic abilities"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self._power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = incoming_damage // 2
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self._power,
            "combat_type": "melee"
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict:
        self._mana += amount
        return {
            "channeled": amount,
            "total_mana": self._mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "mana": self._mana
        }
