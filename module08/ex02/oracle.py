import os
import sys

try:
    import dotenv
except Exception as e:
    print(e)
    sys.exit(1)


def load_config(override: bool) -> None:
    try:
        print("\nORACLE STATUS: Reading the Matrix...\n")

        # List of required configuration variables
        config_keys = [
            'MATRIX_MODE', 'DATABASE_URL',
            'API_KEY', 'LOG_LEVEL', 'ZION_ENDPOINT',
        ]

        # Read each variable from the environment
        config = {}
        missing = False
        for key in config_keys:
            value = os.getenv(key)
            if value:
                config[key] = value
            else:
                print(f"Missing configuration: {key}")
                missing = True

        # Display loaded configuration
        # Mask API_KEY to avoid exposing secrets in output
        raw_key = config.get('API_KEY', 'NOT SET')
        masked_key = raw_key[:4] + "****" if raw_key != "NOT SET" else raw_key
        MATRIX_MODE = config.get('MATRIX_MODE', 'NOT SET')

        print("\nConfiguration loaded:")
        print(f"  Mode:         {config.get('MATRIX_MODE', 'NOT SET')}")
        print(f"  Database:     {config.get('DATABASE_URL', 'NOT SET')}")
        print(f"  API Access:   {masked_key}")
        print(f"  Log Level:    {config.get('LOG_LEVEL', 'NOT SET')}")
        print(f"  Zion Network: {config.get('ZION_ENDPOINT', 'NOT SET')}")

        # Security checks
        print("\nEnvironment security check:")

        # Check for hardcoded secrets by scanning variable names
        # in the current scope against the configex2 keys
        hardcoded = False
        scope = {**globals(), **locals()}
        for var in scope:
            if var.upper() in config_keys:
                print("  [KO] Hardcoded secrets detected")
                hardcoded = True
                break
        if not hardcoded:
            print("  [OK] No hardcoded secrets detected")

        # Check if all required variables were loaded
        if not missing:
            print("  [OK] .env file properly configured")
        else:
            print("  [KO] .env file missing some variables")

        # Check if production override is active
        if override:
            print("  [OK] Production overrides available")
        else:
            print("  [KO] Production overrides unavailable")

        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")
        sys.exit(1)

# API_KEY="dfghjnk"
if __name__ == "__main__":
    # override=True means .env vars take priority over system env
    override = True
    dotenv.load_dotenv(override=override)
    load_config(override)
    
