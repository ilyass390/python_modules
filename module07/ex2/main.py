from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===")
print()
warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 4)

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

print("\nPlaying Arcane Warrior (Elite Card):")

print("\nCombat phase:")
print(f"Attack result: {warrior.attack('Enemy')}")
print(f"Defense result: {warrior.defend(5)}")

print("\nMagic phase:")
print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
print(f"Mana channel: {warrior.channel_mana(3)}")

print("\nMultiple interface implementation successful!")
