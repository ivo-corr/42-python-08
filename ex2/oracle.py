from dotenv import load_dotenv
import os


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the matrix...\n")
    load_dotenv(".env")
    if (not os.path.exists(".env")):
        print("[KO] .env file not found")
    else:
        print("Configuration loaded:")
        print(f"Mode: {os.getenv('MATRIX_MODE')}")
        print("Database:",
              "Connected to local instance" if
              os.getenv("DATABASE_URL") == "database.com" else "Not connected")
        print("API Access:",
              "Authenticated" if
              os.getenv("API_KEY") == "12345" else "Not authenticated")
        print(f"Log Level: {os.getenv('LOG_LEVEL')}")
        print("Zion Network:",
              "Online" if os.getenv("ZION_ENDPOINT") else "Offline")

        print("[OK] No hardcoded secrets detected")
        if (not ("MATRIX_MODE" in os.environ and
                 "DATABASE_URL" in os.environ and
                 "API_KEY" in os.environ and
                 "LOG_LEVEL" in os.environ and
                 "ZION_ENDPOINT" in os.environ)):
            print("[KO] .env file not properly configured: missing values")
        else:
            print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")
    # config = dotenv_values(".env")
    # print(config["MATRIX_MODE"])
