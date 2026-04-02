import sys
import importlib.util


def check_dependency(package_name: str) -> tuple[bool, str]:
    try:
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            return False, "Not installed"
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "version unknown")
        return True, version
    except ModuleNotFoundError:
        return False, "Not installed"
    except Exception as e:
        return False, f"Error: {e}"


def display_dependencies() -> bool:
    critical_packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    optional_packages = {
        "requests": "Network access ready",
    }

    print("Checking dependencies:")
    all_critical_ok = True

    for package, description in critical_packages.items():
        try:
            available, version = check_dependency(package)
            if available:
                print(f"  [OK] {package} ({version}) - {description}")
            else:
                print(f"  [MISSING] {package} - run:")
                print(f"    pip install {package}")
                all_critical_ok = False
        except Exception as e:
            print(f"  [ERROR] {package} - {e}")
            all_critical_ok = False

    for package, description in optional_packages.items():
        available, version = check_dependency(package)
        if available:
            print(f"  [OK] {package} ({version}) - {description}")
        else:
            print(f"  [OPTIONAL] {package} - not installed")

    return all_critical_ok


def display_pip_vs_poetry() -> None:
    print("--- Dependency Management: pip vs Poetry ---")
    print()
    print("pip:")
    print("  - Built into Python, no installation needed")
    print("  - Uses requirements.txt to list dependencies")
    print("  - Install command: pip install -r requirements.txt")
    print("  - No automatic virtual environment management")
    print("  - No lock file by default (use pip freeze)")
    print()
    print("Poetry:")
    print("  - Must be installed separately: pip install poetry")
    print("  - Uses pyproject.toml to list dependencies")
    print("  - Install command: poetry install")
    print("  - Automatically manages virtual environments")
    print("  - Generates poetry.lock for exact reproducibility")
    print()
    print("  Both tools are installed in this project:")
    print("  requirements.txt -> for pip users")
    print("  pyproject.toml   -> for Poetry users")
    print()


def run_analysis() -> None:
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("Analyzing Matrix data...")

        # Simple sample data - 10 values is enough to show usage
        data = {
            "time": np.arange(10),
            "signal": np.random.randint(0, 100, 10),
        }

        # Create DataFrame and show basic stats
        df = pd.DataFrame(data)
        print(f"  Mean signal: {df['signal'].mean():.2f}")
        print(f"  Max signal:  {df['signal'].max()}")
        print(f"  Min signal:  {df['signal'].min()}")

        # Simple plot - just a basic line chart
        plt.plot(df["time"], df["signal"], color="green", marker="o")
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Time")
        plt.ylabel("Signal")
        plt.savefig("matrix_analysis.png")
        plt.close()

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"Error during analysis: {e}")
        raise


def main() -> None:
    try:
        print("LOADING STATUS: Loading programs...")
        print()

        all_ok = display_dependencies()
        print()

        # Explain the difference between pip and Poetry
        display_pip_vs_poetry()

        if not all_ok:
            print("ERROR: Critical dependencies missing!")
            print("Install with pip:    pip install -r requirements.txt")
            print("Install with Poetry: poetry install")
            sys.exit(1)

        run_analysis()

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
