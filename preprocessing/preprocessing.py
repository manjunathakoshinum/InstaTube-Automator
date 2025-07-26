
from preprocessing.get_video_text_image_file import get_files
from preprocessing.title_description_tags import get_valid_title_description_tags
from preprocessing.duration import get_video_duration
import re

def check_content_text_file(text_file_path):
    try:
        with open(text_file_path, 'r', errors='replace') as file:
            # Read the entire content of the file and strip any leading/trailing whitespace
            content = file.read().strip()
            # Remove non-English characters using a regular expression
            content = re.sub(r'[^A-Za-z0-9\s,.!?\'\"\-\n]', '', content)
            # Print the content
            print(f'Got contents of text file...')
            return content
    except FileNotFoundError:
        print(f'Error: The file {text_file_path} does not exist.')
    except IOError:
        print(f'Error: Unable to read the file {text_file_path}.')




def preprocessing(videos_path_file,geckodriver_path,command_for_title,command_for_description,command_for_tags,commad_for_hashtags):
    video_file,text_file,image_file = get_files(videos_path_file)
    get_video_duration(video_file)
    content =check_content_text_file(text_file)
    title ,description,tags=get_valid_title_description_tags(content,geckodriver_path,command_for_title,command_for_description,command_for_tags,commad_for_hashtags)
    return video_file,title,description,tags,image_file,text_file
    