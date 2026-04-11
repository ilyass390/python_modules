from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

print("=== DataDeck Game Engine ===")
print()
print("Configuring Fantasy Card Game...")

factory = FantasyCardFactory()
strategy = AggressiveStrategy()
engine = GameEngine()

print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}")

engine.configure_engine(factory, strategy)

print("\nSimulating aggressive turn...")
hand_names = [f"{c.name} ({c.cost})" for c in engine.get_hand()]
print(f"Hand: {hand_names}")

result = engine.simulate_turn()
print("\nTurn execution:")
print(f"Strategy: {result['strategy']}")
print(f"Actions: {result['actions']}")

print("\nGame Report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
