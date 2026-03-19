from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self._factory = None
        self._strategy = None
        self._turns = 0
        self._total_damage = 0
        self._cards_created = 0
        self._hand = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy
        self._hand = [
            factory.create_creature(),
            factory.create_creature("goblin"),
            factory.create_spell()
        ]
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict:
        result = self._strategy.execute_turn(self._hand, [])
        self._turns += 1
        self._total_damage += result.get("damage_dealt", 0)
        return {
            "strategy": self._strategy.get_strategy_name(),
            "actions": result
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._turns,
            "strategy_used": self._strategy.get_strategy_name(),
            "total_damage": self._total_damage,
            "cards_created": self._cards_created
        }
