from .Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    @property
    def attack(self):
        return self._attack
    @attack.setter
    def attack(self, attack):
        if not isinstance(attack, int):
            raise TypeError("attack must be an integer")
        if attack <= 0:
            raise ValueError("Attack nust be non-negative")
        self._attack = attack
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, health):
        if not isinstance(health, int):
            raise TypeError("health must be an integer")
        if health <= 0:
            raise ValueError("health nust be non-negative")
        self._health = health

    def get_card_info(self):
        info = super().get_card_info()
        info.update({"type": "Creature", "attack": self.attack, "health": self.health})
        return info

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
