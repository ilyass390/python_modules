from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a new function that calls both spells and returns a tuple."""
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a new spell with power multiplied before casting."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable, spell: Callable
) -> Callable:
    """Return a spell that only casts when the condition holds True."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts all spells in order as a list."""
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    """Deal fire damage to a target."""
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    """Restore health to a target."""
    return f"Heals {target}"


def shield(target: str, power: int) -> str:
    """Raise a shield around a target."""
    return f"Shield protects {target} with {power} barrier"


def lightning(target: str, power: int) -> str:
    """Strike a target with lightning."""
    return f"Lightning strikes {target} for {power} damage"


if __name__ == "__main__":
    # --- spell_combiner demo ---
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    # --- power_amplifier demo ---
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    base_power = 10
    amplified_result = mega_fireball("Dragon", base_power)
    print(f"Original: {base_power}, Amplified: {base_power * 3}")
    print(f"Amplified spell: {amplified_result}")

    print("\nTesting conditional caster...")
    high_power_only = conditional_caster(
        lambda target, power: power >= 30,
        fireball
    )
    print(f"Power 50 -> {high_power_only('Goblin', 50)}")
    print(f"Power 10 -> {high_power_only('Goblin', 10)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, shield, lightning])
    results = combo("Dragon", 40)
    for r in results:
        print(f"  {r}")
