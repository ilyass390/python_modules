from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }

    def create_creature(self, name_or_power=None) -> CreatureCard:
        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None) -> SpellCard:
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for i in range(size):
            if i % 3 == 0:
                cards.append(self.create_creature("goblin"))
            elif i % 3 == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {"deck": cards, "size": size, "theme": "Fantasy"}
