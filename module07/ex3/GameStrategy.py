from abc import ABC


class GameStrategy(ABC):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        raise NotImplementedError(
            "execute_turn() must be implemented by subclass"
        )

    def get_strategy_name(self) -> str:
        raise NotImplementedError(
            "get_strategy_name() must be implemented by subclass"
        )

    def prioritize_targets(self, available_targets: list) -> list:
        raise NotImplementedError(
            "prioritize_targets() must be implemented by subclass"
        )
