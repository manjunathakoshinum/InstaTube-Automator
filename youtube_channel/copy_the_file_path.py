import os
import json

def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def save_to_json(file_paths, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(file_paths, json_file, indent=4)

def main():
    directory = r"D:\instagram_to_youtube\youtube_channel\movies\downloaded_videos"
    output_file = r"D:\instagram_to_youtube\youtube_channel\movies\video_files_path.json"

    file_paths = get_all_file_paths(directory)
    save_to_json(file_paths, output_file)

    print(f"All file paths have been saved to {output_file}")

if __name__ == "__main__":
    main()
