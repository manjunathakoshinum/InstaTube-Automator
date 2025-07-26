import json

# Load specific upload configuration for a YouTube channel
def channel_upload_data_selection(upload_details):
    with open(upload_details, 'r') as file:
        data = json.load(file)
        return (
            data["video_file_path"],
            data["geckodriver_path"],
            data["made_for_kids"],
            data["age_restriction"],
            data["category"],
            data["sort_by"],
            data["visibility"],
            data["command_for_title"],
            data["command_for_description"],
            data["command_for_tags"],
            data["command_for_hashtags"]
        )


# Select upload configuration paths for the given channel
def channel_selection(channel_to_match):
    match channel_to_match:
        case "channel_name": #replace this with your channel name
            # Path to metadata containing uploaded video history, counts, etc.
            metadata_path = r"path/to/youtube_channel/meems/channels/channel_managements.json"

            # Path to download filters: view count, time range, etc.
            download_config_path = r"path/to/youtube_channel/meems/download_configuration.json"

            # Path to upload details: title rules, tags, category, visibility, etc.
            upload_details_path = r"path/to/youtube_channel/meems/meems_upload_details.json"

            # Path to the Firefox browser profile used for Selenium YouTube automation
            firefox_profile_path = r"path/to/firefox/profile/used/for/youtube/upload"

            return metadata_path, download_config_path, upload_details_path, firefox_profile_path

        case _:
            print("Please enter a valid channel name")
            return None, None, None, None
