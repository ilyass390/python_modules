from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    MAX_MANA = 7

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def get_card_cost(self, card) -> int:
        return card.cost

    def prioritize_targets(self, available_targets: list) -> list:
        creature_targets = [t for t in available_targets if "Player" not in t]
        player_targets = [t for t in available_targets if "Player" in t]
        return creature_targets + player_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        # separate creatures and non-creatures
        creatures = []
        others = []
        for card in hand:
            info = card.get_card_info()
            if info.get("type") == "Creature":
                creatures.append(card)
            else:
                others.append(card)

        # sort creatures by cost — cheapest first for board presence
        creatures.sort(key=self.get_card_cost)
        others.sort(key=self.get_card_cost)

        # play creatures first then others
        sorted_hand = creatures + others

        mana = self.MAX_MANA
        played_cards = []
        for card in sorted_hand:
            if card.cost <= mana:
                played_cards.append(card)
                mana -= card.cost

        # target enemy creatures first then player
        targets = self.prioritize_targets(
            battlefield + ["Enemy Player"]
        )

        mana_used = sum(c.cost for c in played_cards)
        damage = mana_used + 3
        return {
            "cards_played": [c.name for c in played_cards],
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage
        }
