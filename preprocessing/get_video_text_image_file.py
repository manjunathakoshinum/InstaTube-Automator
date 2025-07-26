import os
import json

def load_json(file_path):
    """Load JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def categorize_files(file_list):
    """Categorize files by their base name."""
    categorized_files = {}
    for file_path in file_list:
        base_name, ext = os.path.splitext(file_path)
        if base_name not in categorized_files:
            categorized_files[base_name] = {}
        categorized_files[base_name][ext] = file_path
    return categorized_files

def find_files(categorized_files):
    """Find the first video file and related text and image files."""
    video_extensions = {'.mp4'}
    text_extensions = {'.txt'}
    image_extensions = {'.jpg'}
    
    for base_name, files in categorized_files.items():
        for ext in video_extensions:
            if ext in files:
                video_file = files[ext]
                text_file = next((files[ext] for ext in text_extensions if ext in files), None)
                image_file = next((files[ext] for ext in image_extensions if ext in files), None)
                return video_file, text_file, image_file
    return None, None, None

def get_files(json_file_path):
    file_list = load_json(json_file_path)
    categorized_files = categorize_files(file_list)
    
    video_file, text_file, image_file = find_files(categorized_files)
    
    return video_file, text_file, image_file



