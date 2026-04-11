from ex0.CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===")
print()
print("Testing Abstract Base Class Design:")
print()
dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
game_state = {"mana_player": 6, "enemy_mana": 10}
print("CreatureCard Info:")
print(dragon.get_card_info())

print("\nPlaying Fire Dragon with 6 mana available:")
print(f'Playable: {dragon.is_playable(game_state.get("mana_player"))}')
print(f"Play result: {dragon.play(game_state)}")
if dragon.is_playable(game_state.get("mana_player")):
    game_state["mana_player"] -= dragon.cost

print("\nFire Dragon attacks Goblin Warrior:")
print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")

print("\nTesting insufficient mana (3 available):")
print(f"Playable: {dragon.is_playable(3)}")

print("\nAbstract pattern successfully demonstrated!")
