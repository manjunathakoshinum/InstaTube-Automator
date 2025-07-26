import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def delete_files_and_update_json(video_file_path, text_file_path, image_file_path, json_file_path):
    """
    Deletes the specified files and updates the JSON file to remove the paths of deleted files.

    :param video_file_path: Path to the video file to delete.
    :param text_file_path: Path to the text file to delete.
    :param image_file_path: Path to the image file to delete.
    :param json_file_path: Path to the JSON file to update.
    """
    files_to_delete = {
        "video_file": video_file_path,
        "text_file": text_file_path,
        "image_file": image_file_path
    }

    # Attempt to delete each file
    for file_type, file_path in files_to_delete.items():
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
                logging.info(f"Deleted {file_type}: {file_path}")
            except Exception as e:
                logging.error(f"Error deleting {file_type}: {file_path}. Error: {e}")
        else:
            logging.warning(f"{file_type} not found or already deleted: {file_path}")

    # Load the existing JSON file
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
    except Exception as e:
        logging.error(f"Error reading JSON file: {json_file_path}. Error: {e}")
        return

    # Remove paths from the JSON data
    paths_to_remove = {video_file_path, text_file_path, image_file_path}
    updated_data = [path for path in data if path not in paths_to_remove]

    # Update the JSON file
    try:
        with open(json_file_path, 'w') as json_file:
            json.dump(updated_data, json_file, indent=4)
        logging.info(f"Updated JSON file: {json_file_path}")
    except Exception as e:
        logging.error(f"Error updating JSON file: {json_file_path}. Error: {e}")

if __name__ == "__main__":
    # Example paths to delete
    video_file_path = "D:\\update_to_make_robuts\\video.mp4"
    text_file_path = "D:\\update_to_make_robuts\\ga.txt"
    image_file_path = "D:\\update_to_make_robuts\\image.jpg"

    # Path to the JSON file to update
    json_file_path = "output.json"

    #delete_files_and_update_json(video_file_path, text_file_path, image_file_path, json_file_path)
