from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

print("=== DataDeck Deck Builder ===")
print()
print("Building deck with different card types...")

deck = Deck()
deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
deck.add_card(ArtifactCard("Mana Crystal", 4, "Rare", 5, "+1 mana per turn"))
deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))

print(f"Deck stats: {deck.get_deck_stats()}")

print("\nDrawing and playing cards:")

bolt = deck.draw_card()
print(f"\nDrew: {bolt.name} ({bolt.get_card_info().get('type')})")
print(f"Play result: {bolt.play({})}")

crystal = deck.draw_card()
print(f"\nDrew: {crystal.name} ({crystal.get_card_info().get('type')})")
print(f"Play result: {crystal.play({})}")

dragon = deck.draw_card()
print(f"\nDrew: {dragon.name} ({dragon.get_card_info().get('type')})")
print(f"Play result: {dragon.play({})}")

print("\nPolymorphism in action: Same interface, different card behaviors!")
