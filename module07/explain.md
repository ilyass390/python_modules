Exercise 1 — Deck Builder (Polymorphism)
The core concept: Polymorphism
Polymorphism means "many forms". You call the same method on different objects and each one responds differently. In this exercise, Deck calls card.play({}) without knowing if the card is a Creature, Spell or Artifact — each one handles it its own way.
python# Same call, 3 different behaviors
dragon.play({})   # → "Creature summoned to battlefield"
bolt.play({})     # → "Deal 3 damage to target"
crystal.play({})  # → "Permanent: +1 mana per turn"

SpellCard
Inherits from Card. Represents a one-time use magic effect.
pythondef __init__(self, name, cost, rarity, effect_type)
effect_type is the kind of spell: "damage", "heal", "buff", "debuff".
pythondef play(self, game_state: dict) -> dict
Returns what happens when the spell is cast. Spells are consumed after use — one-time.
pythondef resolve_effect(self, targets: list) -> dict
Applies the spell to a list of targets. Returns who was hit and what happened.
pythondef get_card_info(self) -> dict
Calls super().get_card_info() to get the base dict from Card, then adds "type": "Spell" and "effect_type". This is inheritance in action — reuse parent logic, extend it.

ArtifactCard
Inherits from Card. Represents a permanent item that stays in play.
pythondef __init__(self, name, cost, rarity, durability, effect)
durability = how many turns/uses it lasts. effect = what it does permanently.
pythondef play(self, game_state: dict) -> dict
Returns a "Permanent: ..." effect — unlike spells, artifacts don't disappear.
pythondef activate_ability(self) -> dict
Triggers the artifact's ongoing power. Returns current durability so you know how long it'll last.

Deck
Not a card — it's a manager class. Stores any Card object regardless of type.
pythondef __init__(self)
Creates an empty _cards list. Uses underscore to signal it's private.
pythondef add_card(self, card: Card) -> None
Appends any Card subclass to the list. Accepts CreatureCard, SpellCard, ArtifactCard — it doesn't care which one. That's polymorphism at the container level.
pythondef remove_card(self, card_name: str) -> bool
Searches by name, removes it if found, returns True. Returns False if not found. Never crashes.
pythondef shuffle(self) -> None
Uses random.shuffle() to randomize the order of _cards in place.
pythondef draw_card(self) -> Card
Pops the first card from the list (pop(0)). Raises IndexError if deck is empty rather than returning None — cleaner error handling.
pythondef get_deck_stats(self) -> dict
Iterates through all cards, calls get_card_info().get("type") on each to count creatures, spells, artifacts. Calculates average cost. This works because every card has get_card_info() — the contract defined by the abstract base class.


Exercise 2 — Ability System (Multiple Inheritance + Interfaces)
The core concept: Multiple Inheritance & Interfaces
In Python you can inherit from more than one class at the same time. EliteCard inherits from Card, Combatable AND Magical simultaneously — it must implement ALL abstract methods from all three.
pythonclass EliteCard(Card, Combatable, Magical):
Think of Combatable and Magical as interfaces — they define a contract (what methods must exist) but provide no implementation. Pure blueprints.

Combatable
Abstract interface for anything that can fight.
pythondef attack(self, target) -> dict
Must be implemented. Returns damage info — who attacked, who was hit, how much damage.
pythondef defend(self, incoming_damage: int) -> dict
Must be implemented. Returns how much damage was blocked vs taken, whether still alive.
pythondef get_combat_stats(self) -> dict
Returns the card's combat capabilities — attack power, combat type.

Magical
Abstract interface for anything that can use magic.
pythondef cast_spell(self, spell_name: str, targets: list) -> dict
Must be implemented. Returns caster, spell name, targets hit, mana spent.
pythondef channel_mana(self, amount: int) -> dict
Must be implemented. Adds mana to the card's pool, returns how much was channeled and new total.
pythondef get_magic_stats(self) -> dict
Returns current mana pool and magic capabilities.

EliteCard
The class that combines everything.
pythondef __init__(self, name, cost, rarity, attack, mana)
Calls super().__init__(name, cost, rarity) which thanks to Python's MRO (Method Resolution Order) correctly chains through Card, Combatable, Magical in order.
pythondef defend(self, incoming_damage: int) -> dict
Blocks attack // 2 damage. For example attack=5 → blocks 2 (5 // 2), takes the rest. The max(0, ...) prevents negative damage taken.
pythondef channel_mana(self, amount: int) -> dict
self._mana += amount updates the pool, then returns both the amount channeled and the new total. That's why channel_mana(3) with starting mana=4 returns total_mana: 7.
Why separate Combatable and Magical?
Because not every card needs both. A CreatureCard might only be Combatable. A SpellCard might only be Magical. EliteCard happens to need both — multiple inheritance lets you mix and match exactly what you need.


Exercise 3 — Game Engine (Strategy Pattern + Factory Pattern)
Two design patterns working together:

Strategy Pattern
Defines a family of algorithms, puts each in a separate class, makes them interchangeable. The GameEngine doesn't care WHICH strategy it uses — it just calls strategy.execute_turn() and gets a result.
python# You can swap strategies without changing GameEngine
engine.configure_engine(factory, AggressiveStrategy())
engine.configure_engine(factory, DefensiveStrategy())  # hypothetical
GameStrategy (abstract)
pythondef execute_turn(self, hand: list, battlefield: list) -> dict
Takes your hand of cards and the battlefield state. Returns what actions were taken.
pythondef get_strategy_name(self) -> str
Returns the strategy's name — used in reports and logs.
pythondef prioritize_targets(self, available_targets: list) -> list
Decides which targets to attack first. Aggressive = attack everything. Defensive = protect yourself first.
AggressiveStrategy (concrete)
pythondef execute_turn(self, hand, battlefield) -> dict
Sorts hand by cost (cheapest first), plays as many cards as possible within 7 mana. Targets "Enemy Player" directly. Returns cards played, mana spent, targets attacked, damage dealt.
The logic: sort by cost → play cheapest cards first → maximize board presence → deal maximum damage. That's "aggressive" playstyle.

Factory Pattern
Instead of calling CreatureCard(...) directly everywhere, you ask the factory to create it. The factory knows all the details — you just say "give me a dragon".
python# Without factory — you need to know all parameters
card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

# With factory — clean, no details needed
card = factory.create_creature("dragon")
CardFactory (abstract)
pythondef create_creature(self, name_or_power=None) -> Card
def create_spell(self, name_or_power=None) -> Card
def create_artifact(self, name_or_power=None) -> Card
Three creation methods — one per card type. The name_or_power parameter lets you optionally specify which variant you want.
pythondef create_themed_deck(self, size: int) -> dict
Creates a full deck of size cards with a balanced mix. Returns a dict with the cards list and theme info.
pythondef get_supported_types(self) -> dict
Returns what this factory can create. Useful for the game engine to know its options.
FantasyCardFactory (concrete)
Implements all factory methods with fantasy-themed cards:

create_creature("goblin") → GoblinWarrior (cheap, weak)
create_creature() → FireDragon (expensive, powerful)
create_spell() → LightningBolt
create_artifact() → ManaRing

pythondef create_themed_deck(self, size: int) -> dict
Uses modulo (i % 3) to alternate creature/spell/artifact evenly.
GameEngine
The orchestrator — connects factory and strategy together.
pythondef configure_engine(self, factory, strategy) -> None
Sets the factory and strategy, then immediately uses the factory to build a starting hand of 3 cards. This is where factory and strategy patterns connect.
pythondef simulate_turn(self) -> dict
Delegates entirely to strategy.execute_turn(). Engine doesn't know how the turn is played — strategy does. Tracks damage and turn count.
pythondef get_engine_status(self) -> dict
Returns a report: turns played, strategy used, total damage dealt, cards created.


Exercise 4 — Tournament Platform (Full Composition)
The core concept: Interface Composition
This exercise combines EVERYTHING — Card (ex0), Combatable (ex2), and a new Rankable interface — into one class using multiple inheritance. It's the capstone that shows how all the patterns work together.

Rankable
Abstract interface for anything that has a competitive rating.
pythondef calculate_rating(self) -> int
Returns the current ELO-style rating number.
pythondef update_wins(self, wins: int) -> None
Adds wins and increases rating. In our implementation +16 per win (ELO-inspired).
pythondef update_losses(self, losses: int) -> None
Adds losses and decreases rating. -16 per loss.
pythondef get_rank_info(self) -> dict
Returns full rank info — name, rating, wins, losses.

TournamentCard
Inherits from Card, Combatable, AND Rankable — 3 interfaces at once.
pythondef __init__(self, name, cost, rarity, attack, health, rating=1200)
Default rating is 1200 — standard starting ELO. Tracks _wins and _losses from birth.
pythondef update_wins(self, wins: int) -> None
self._wins += wins then self._rating += wins * 16. So one win: 1200 → 1216.
pythondef update_losses(self, losses: int) -> None
self._losses += losses then self._rating -= losses * 16. One loss: 1150 → 1134.
pythondef get_tournament_stats(self) -> dict
Returns the card's full tournament profile — name, rating, record ("1-0"), and the list of interfaces it implements. Used in main.py to prove multiple inheritance is working.

TournamentPlatform
The management system. Stores cards, runs matches, tracks rankings.
pythondef register_card(self, card: TournamentCard) -> str
Creates a unique ID from the card name: "Fire Dragon" → "fire_dragon_001". Stores it in _cards dict with the ID as key. Returns the ID so main.py can reference it later.
pythondef create_match(self, card1_id: str, card2_id: str) -> dict
Looks up both cards by ID. The one with higher attack wins. Calls winner.update_wins(1) and loser.update_losses(1). Stores result in _matches history. Returns the match result dict.
pythondef get_leaderboard(self) -> list
Sorts all cards by calculate_rating() descending. Returns ranked list — 1st place at top. Uses enumerate(sorted_cards, 1) to start rank numbering at 1.
pythondef generate_tournament_report(self) -> dict
```
Summary stats: total cards registered, matches played, average rating (integer division `//`), platform status.

---

## The Big Picture — How it all connects
```
ex0: Card (abstract base)
      ↓
ex1: CreatureCard, SpellCard, ArtifactCard (concrete cards) + Deck (manager)
      ↓
ex2: Combatable, Magical (interfaces) + EliteCard (multiple inheritance)
      ↓
ex3: GameStrategy, CardFactory (patterns) + AggressiveStrategy, FantasyCardFactory, GameEngine
      ↓
ex4: Rankable (interface) + TournamentCard (3 interfaces) + TournamentPlatform (full system)
Each exercise adds one layer. By ex4 you have a complete system where every piece talks to every other piece through the abstract contracts defined in ex0 and ex2. That's the power of abstract programming — you build the rules once, then everything follows them automatically