from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print("=== DataDeck Tournament Platform ===")
print("Registering Tournament Cards...")

dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, 4, 1150)

platform = TournamentPlatform()
dragon_id = platform.register_card(dragon)
wizard_id = platform.register_card(wizard)

stats_dragon = dragon.get_tournament_stats()
print(f"\n{dragon.name} (ID: {dragon_id}):")
print(f"- Interfaces: {stats_dragon['interfaces']}")
print(f"- Rating: {dragon.calculate_rating()}")
print(f"- Record: {stats_dragon['record']}")

stats_wizard = wizard.get_tournament_stats()
print(f"\n{wizard.name} (ID: {wizard_id}):")
print(f"- Interfaces: {stats_wizard['interfaces']}")
print(f"- Rating: {wizard.calculate_rating()}")
print(f"- Record: {stats_wizard['record']}")

print("\nCreating tournament match...")
result = platform.create_match(dragon_id, wizard_id)
print(f"Match result: {result}")

print("\nTournament Leaderboard:")
for entry in platform.get_leaderboard():
    print(f"{entry['rank']}. {entry['name']} - "
          f"Rating: {entry['rating']} ({entry['record']})")

print(f"\nPlatform Report:")
print(platform.generate_tournament_report())

print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
