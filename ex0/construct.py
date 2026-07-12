import sys
import os
import site

if __name__ == "__main__":
    # print(f"prefix {sys.prefix}")
    # print(f"base_prefix {sys.base_prefix}")
    if (sys.prefix == sys.base_prefix):
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env/Scripts/activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current python: {sys.executable}")
        env_path: str = os.environ.get("VIRTUAL_ENV")
        print(f"Virtual Environment: {env_path.split('/')[-1]}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system")
        print("Package installation path:")
        print(site.getsitepackages()[0])
