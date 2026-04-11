import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the specified operation."""
    if not spells:
        return 0

    ops: dict[str, Callable] = {
        'add':      operator.add,
        'multiply': operator.mul,
        'max':      max,
        'min':      min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: '{operation}'")

    if operation in ('max', 'min'):
        return functools.reduce(ops[operation], spells)

    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable
) -> dict[str, Callable]:
    """Create 3 specialised partial versions of base_enchantment."""
    return {
        'fire':  functools.partial(base_enchantment, power=50,
                                   element='fire'),
        'ice':   functools.partial(base_enchantment, power=50,
                                   element='ice'),
        'storm': functools.partial(base_enchantment, power=50,
                                   element='storm'),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using lru_cache memoization."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a singledispatch function that handles spells by type."""

    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting memoized fibonacci...")
    for n in (0, 1, 10, 15):
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "storm"]))
    print(dispatch(3.14))

    # print("\nTesting partial enchanter...")

    # def base_enchantment(power: int, element: str, target: str) -> str:
    #     return (
    #         f"{element.capitalize()} enchantment on {target}"
    #         f" (power={power})"
    #     )

    # variants = partial_enchanter(base_enchantment)
    # print(f"Fire   -> {variants['fire'](target='Sword')}")
    # print(f"Ice    -> {variants['ice'](target='Shield')}")
    # print(f"Storm  -> {variants['storm'](target='Staff')}")
