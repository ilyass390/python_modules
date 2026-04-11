from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards = {}
        self._matches = []

    def register_card(self, card: TournamentCard) -> str:
        card_id = (card.name.lower().replace(" ", "_")
                   + f"_{len(self._cards) + 1:03d}")
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]
        stats1 = card1.get_combat_stats()
        stats2 = card2.get_combat_stats()
        power1 = stats1["attack"] + stats1["health"]
        power2 = stats2["attack"] + stats2["health"]
        if power1 >= power2:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id
        winner.update_wins(1)
        loser.update_losses(1)
        result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }
        self._matches.append(result)
        return result

    def get_card_rating(self, item) -> int:
        return item[1].calculate_rating()

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self._cards.items(),
            key=self.get_card_rating,
            reverse=True
        )
        leaderboard = []
        for rank, (card_id, card) in enumerate(sorted_cards, 1):
            info = card.get_rank_info()
            leaderboard.append({
                "rank": rank,
                "name": info["name"],
                "rating": info["rating"],
                "record": f"{info['wins']}-{info['losses']}"
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total = len(self._cards)
        ratings = [c.calculate_rating() for c in self._cards.values()]
        avg = round(sum(ratings) / len(ratings)) if ratings else 0
        return {
            "total_cards": total,
            "matches_played": len(self._matches),
            "avg_rating": avg,
            "platform_status": "active"
        }
