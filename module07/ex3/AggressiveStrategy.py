from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        mana = 7
        played = []
        mana_used = 0
        for card in sorted_hand:
            if card.cost <= mana:
                played.append(card.name)
                mana_used += card.cost
                mana -= card.cost
        targets = self.prioritize_targets(["Enemy Player"])
        damage = mana_used + 3
        return {
            "cards_played": played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage
        }
