import sys
import os
import site


def is_in_virtual_env() -> bool:
    # Detect if the script is running inside a virtual environment.
    # sys.prefix points to the venv root when a venv is active.
    # sys.base_prefix always points to the real system Python.
    # If they differ, we are inside a venv.
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str | None:
    try:
        venv_path = os.environ.get("VIRTUAL_ENV")
        if venv_path:
            # basename extracts just the folder name from the full path
            # e.g. "/home/user/matrix_env" -> "matrix_env"
            return os.path.basename(venv_path)
        return None
    except Exception as e:
        print(f"Error reading VIRTUAL_ENV variable: {e}")
        return None

def get_venv_path() -> str | None:
    try:
        # Returns the full path or None if variable is not set
        return os.environ.get("VIRTUAL_ENV")
    except Exception as e:
        print(f"Error reading VIRTUAL_ENV path: {e}")
        return None



def get_site_packages_path() -> str:
    try:
        # getsitepackages() returns a list of paths,
        # the first one is always the main site-packages folder
        packages = site.getsitepackages()
        return packages[0] if packages else "Unknown"
    except AttributeError:
        # getsitepackages() can fail in some edge cases,
        # so we fall back to the user site-packages path
        try:
            return site.getusersitepackages()
        except Exception as e:
            print(f"Error getting site-packages path: {e}")
            return "Unknown"


def display_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print("  matrix_env\\Scripts\\activate     # On Windows")
    print()
    print("Then run this program again.")

def display_inside_venv() -> None:
    # Gather all environment info using our utility functions
    venv_name = get_venv_name()
    venv_path = get_venv_path()
    site_packages = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(f"  {site_packages}")


def display_inside_venv() -> None:
    # Gather all environment info using our utility functions
    venv_name = get_venv_name()
    venv_path = get_venv_path()
    site_packages = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(f"  {site_packages}")


def main() -> None:
    try:
        if is_in_virtual_env():
            display_inside_venv()
        else:
            display_outside_venv()
    except Exception as e:
        print(f"Unexpected error while checking environment: {e}")


if __name__ == "__main__":
    main()
