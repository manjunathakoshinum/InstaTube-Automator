import subprocess
import sys

def get_installed_packages():
    """Get a list of currently installed packages that are outdated."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--outdated", "--format=freeze"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error listing installed packages: {e}")
        print("Troubleshooting suggestions:")
        print("1. Make sure you have a stable internet connection.")
        print("2. Ensure that pip is properly installed and updated.")
        print("3. Try running the command manually to see if there is an issue: "
              f"{sys.executable} -m pip list --outdated --format=freeze")
        sys.exit(1)

def update_package(package_name):
    """Update a specific package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
    except subprocess.CalledProcessError as e:
        print(f"Error updating package {package_name}: {e}")
        sys.exit(1)

def main():
    print("Checking for outdated packages...")
    outdated_packages = get_installed_packages()
    
    if not outdated_packages:
        print("All packages are up to date.")
        return

    print("The following packages have updates available:")
    for package in outdated_packages:
        print(package)

    # Optional: ask user for confirmation before updating
    confirmation = input("Do you want to update these packages? (yes/no): ").strip().lower()
    if confirmation in ['yes', 'y']:
        print("Updating packages...")
        for package in outdated_packages:
            package_name = package.split('=')[0]  # Extract package name before '=='
            update_package(package_name)
        print("All packages are updated.")
    else:
        print("Update canceled by user.")

if __name__ == "__main__":
    main()
