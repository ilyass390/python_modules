import random
from ex0.Card import Card


class Deck:
    def __init__(self):
        self._cards = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self._cards:
            if card.name == card_name:
                self._cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if not self._cards:
            raise IndexError("Deck is empty")
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict:
        creatures = sum(1 for c in self._cards
                        if c.get_card_info().get("type") == "Creature")
        spells = sum(1 for c in self._cards
                     if c.get_card_info().get("type") == "Spell")
        artifacts = sum(1 for c in self._cards
                        if c.get_card_info().get("type") == "Artifact")
        total = len(self._cards)
        avg_cost = (sum(c.cost for c in self._cards) / total
                    if total > 0 else 0.0)
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
