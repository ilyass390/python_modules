from abc import ABC


class Rankable(ABC):
    def calculate_rating(self) -> int:
        raise NotImplementedError(
            "calculate_rating() must be implemented by subclass"
        )

    def update_wins(self, wins: int) -> None:
        raise NotImplementedError(
            "update_wins() must be implemented by subclass"
        )

    def update_losses(self, losses: int) -> None:
        raise NotImplementedError(
            "update_losses() must be implemented by subclass"
        )

    def get_rank_info(self) -> dict:
        raise NotImplementedError(
            "get_rank_info() must be implemented by subclass"
        )
