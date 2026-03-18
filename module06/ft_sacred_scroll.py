import alchemy
import alchemy.elements

print("=== Sacred Scroll Mastery ===")

print("Testing direct module access:")


# print(alchemy.create_fire())
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")


print()

print("Testing package-level access (controlled by __init__.py)")
try:
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
except AttributeError as e:
    print(f"alchey.create_fire(): {type(e).__name__ } - not exposed")

try:
    print(f"alchemy.create_water(): {alchemy.create_water()}")
except AttributeError as e:
    print(f"alchey.create_water(): {type(e).__name__ } - not exposed")


try:
    print(f"alchemy.create_earth(): {alchemy.create_earth()}")
except AttributeError as e:
    print(f"alchmey.create_earth(): {type(e).__name__ } - not exposed")

try:
    print(f"alchemy.create_air(): {alchemy.create_air()}")
except AttributeError as e:
    print(f"alchemy.create_air(): {type(e).__name__ } - not exposed")

print()

print("Package metadata:")
print("Version: ", alchemy.__version__)
print("Author: ", alchemy.__author__)
