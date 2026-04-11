import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints a function's execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory validating power level (first int arg)."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(args[0], int):
                power = args[0]
            elif isinstance(args[1], int):
                power = args[1]
            else:
                power = args[2]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a failing spell up to max_attempts."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Guild managing mage validation and spell casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is >= 3 chars and letters/spaces only."""
        return (
            len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """Cast a spell if power meets the minimum threshold."""
        return f"Successfully cast {spell_name} with {power} power"


def make_failing_spell(fail_times: int) -> Callable:
    """Return a spell that raises an exception the first fail_times calls."""
    state = {'calls': 0}

    def spell() -> str:
        state['calls'] += 1
        if state['calls'] <= fail_times:
            raise RuntimeError("Spell unstable")
        return "Waaaaaaagh spelled !"

    return spell


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    always_fails = retry_spell(max_attempts=3)(make_failing_spell(99))
    print(always_fails())

    succeeds_after = retry_spell(max_attempts=3)(make_failing_spell(2))
    print(succeeds_after())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    make_failing_spell(3)

    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))
