import os
import shutil
import json

from concurrent.futures import ThreadPoolExecutor

# Set up logging
def load_existing_paths(json_file):
    """Load existing file paths from JSON file."""
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            try:
                return set(json.load(f))
            except json.JSONDecodeError:
                print(f"Error decoding JSON file {json_file}. Starting with an empty list.")
                return set()
    return set()

def save_existing_paths(json_file, paths):
    """Save updated file paths to JSON file."""
    with open(json_file, 'w') as f:
        json.dump(list(paths), f, indent=4)

def move_file(src_file, dest_path, existing_paths_set):
    """Move a file and log the action."""
    if dest_path not in existing_paths_set:
        try:
            shutil.move(src_file, dest_path)
            existing_paths_set.add(dest_path)
            return dest_path
        except Exception as e:
            print(f"Failed to move file {src_file} to {dest_path}: {e}")
    return None

def process_directory(src_directory, dest_directory, existing_paths_set):
    """Process directories and move files concurrently."""
    moved_files = []
    with ThreadPoolExecutor() as executor:
        futures = []
        for item in os.scandir(src_directory):
            if item.is_dir() and item.name.startswith("reel"):
                for entry in os.scandir(item.path):
                    if entry.is_file():
                        dest_path = os.path.join(dest_directory, entry.name)
                        futures.append(executor.submit(move_file, entry.path, dest_path, existing_paths_set))

                # Wait for all move operations to complete before removing the directory
                for future in futures:
                    result = future.result()
                    if result:
                        moved_files.append(result)
                futures.clear()

                # Remove directory if empty
                try:
                    os.rmdir(item.path)

                except OSError as e:
                    print(f"Directory {item.path} not empty or could not be removed. Attempting to clean up.")
                    remove_directory(item.path)
    return moved_files

def remove_directory(directory):
    """Remove a directory and its contents."""
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except Exception as e:
                print(f"Failed to remove file {os.path.join(root, name)}: {e}")
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))

            except Exception as e:
                print(f"Failed to remove directory {os.path.join(root, name)}: {e}")
    try:
        os.rmdir(directory)
    except Exception as e:
        print(f"Failed to remove directory {directory}: {e}")

def remove_reel_files(src_directory):
    """Remove files starting with 'reel' from the source directory."""
    for item in os.scandir(src_directory):
        if item.is_file() and item.name.startswith("reel"):
            try:
                os.remove(item.path)
            except Exception as e:
                print(f"Failed to remove file {item.path}: {e}")

def move_and_log_files(data):
    """Main function to move files and update JSON log."""
    src_directory = data["src_directory"]
    dest_directory = data["dest_directory"]
    json_file = data["json_file"]
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    existing_paths_set = load_existing_paths(json_file)
    moved_files = process_directory(src_directory, dest_directory, existing_paths_set)
    remove_reel_files(src_directory)
    save_existing_paths(json_file, existing_paths_set)

    return moved_files
