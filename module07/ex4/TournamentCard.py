from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 power: int, health: int, rating: int = 1200):
        super().__init__(name, cost, rarity)
        self._power = power
        self._health = health
        self._rating = rating
        self._wins = 0
        self._losses = 0

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Tournament",
                     "attack": self._power, "health": self._health})
        return info

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card deployed"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self._power,
            "combat_type": "tournament"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = incoming_damage // 2
        taken = incoming_damage - blocked
        self._health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self._health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self._power,
            "health": self._health
        }

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self._rating,
            "record": f"{self._wins}-{self._losses}",
            "interfaces": ["Card", "Combatable", "Rankable"]
        }
