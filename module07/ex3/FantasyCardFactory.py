from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self._creature_types = ["dragon", "goblin"]
        self._spell_types = ["fireball", "ice", "lightning"]
        self._artifact_types = ["ring", "staff", "crystal"]

    def get_supported_types(self) -> dict:
        return {
            "creatures": self._creature_types,
            "spells": self._spell_types,
            "artifacts": self._artifact_types
        }

    def register_type(self, category: str, type_name: str) -> None:
        if category == "creatures":
            self._creature_types.append(type_name)
        elif category == "spells":
            self._spell_types.append(type_name)
        elif category == "artifacts":
            self._artifact_types.append(type_name)

    def create_creature(self, name_or_power=None) -> CreatureCard:
        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None) -> SpellCard:
        if name_or_power == "ice":
            return SpellCard("Ice Bolt", 2, "Common", "debuff")
        if name_or_power == "lightning":
            return SpellCard("Lightning Bolt", 3, "Common", "damage")
        return SpellCard("Fireball", 4, "Rare", "damage")

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        if name_or_power == "staff":
            return ArtifactCard("Magic Staff", 3, "Rare", 4, "+2 spell damage")
        if name_or_power == "crystal":
            return ArtifactCard("Power Crystal", 1, "Common", 3, "+1 attack")
        return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for i in range(size):
            if i % 3 == 0:
                cards.append(self.create_creature("goblin"))
            elif i % 3 == 1:
                cards.append(self.create_spell("lightning"))
            else:
                cards.append(self.create_artifact("crystal"))
        return {"deck": cards, "size": size, "theme": "Fantasy"}
