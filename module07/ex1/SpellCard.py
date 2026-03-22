from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self._used = False
        self._resolved = False

    def play(self, game_state: dict) -> dict:
        if self._used:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Spell already consumed - cannot play again"
            }
        self._used = True
        effects = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Grant +2 attack to target",
            "debuff": "Reduce target attack by 2"
        }
        effect = effects.get(self.effect_type, f"Apply {self.effect_type} effect")
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def resolve_effect(self, targets: list) -> dict:
        if not self._used:
            return {
                "spell": self.name,
                "result": "Spell not played yet",
                "resolved": False
            }
        if self._resolved:
            return {
                "spell": self.name,
                "result": "Spell already resolved - one time use only",
                "resolved": False
            }
        self._resolved = True  # mark as resolved, blocks future calls
        effects = {
            "damage": f"Dealt 3 damage to {targets}",
            "heal": f"Restored 3 health to {targets}",
            "buff": f"Granted +2 attack to {targets}",
            "debuff": f"Reduced attack of {targets} by 2"
        }
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "result": effects.get(
                self.effect_type, f"Applied {self.effect_type} to {targets}"
            ),
            "resolved": True
        }
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Spell", "effect_type": self.effect_type})
        return info
