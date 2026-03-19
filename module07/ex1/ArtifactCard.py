from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect
        })
        return info

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "ability": self.effect,
            "durability_remaining": self.durability
        }
