import json
from datetime import datetime, timedelta
channel_metadata = ""
data = { }
channel_name = ""
def load_data():
        global data
        with open(channel_metadata, 'r') as file:
            data = json.load(file)
def save_data(): 
    global data
    with open(channel_metadata, 'w') as file:
        json.dump(data, file, indent=4)
        

# Check if videos can be downloaded        
def can_i_download_video():
    if not data:
        load_data()
    if data["number_of_videos_available_to_upload"] < data["number_of_channels"] :
        return data["number_of_channels"]*5
    else:
        return 0
    
# Update download videos 
def download_update(number_of_videos_downloaded):
    if not data:
        load_data()
    data["number_of_videos_available_to_upload"] += number_of_videos_downloaded
    save_data()
    return data["number_of_videos_available_to_upload"]

# Check if videos can be uploaded to YouTube
def can_i_upload_video_to_youtube():
    if not data:    
        load_data()
    last_uploaded_date_time = datetime.strptime(data["channels"][channel_name]['last_uploaded_date'] + ' ' + data["channels"][channel_name]['last_uploaded_time'], "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    if now - last_uploaded_date_time < timedelta(hours=24):
        if data["channels"][channel_name]["number_of_videos_pending_to_upload"] > 0:
            print(f"You can upload {data["channels"][channel_name]['number_of_videos_pending_to_upload']} videos.")
            return data["channels"][channel_name]["number_of_videos_pending_to_upload"]
        else:
            print("we have uploaded all the videos.")
            return 0
    else:
        data["channels"][channel_name]["number_of_videos_uploaded_today"] = 0
        data["channels"][channel_name]["number_of_videos_pending_to_upload"] = data["channels"][channel_name]["youtube_daily_limit"]
        print(f"Number of videos pending to upload: {data["channels"][channel_name]['number_of_videos_pending_to_upload']}")
        save_data()
        return data["channels"][channel_name]["number_of_videos_pending_to_upload"]

# Update upload count
def upload_update():
    if not data:
        load_data()
    data["channels"][channel_name]["number_of_videos_uploaded_today"] += 1
    data["channels"][channel_name]["number_of_videos_pending_to_upload"] -= 1
    data["number_of_videos_available_to_upload"] -= 1
    data["channels"][channel_name]['last_uploaded_date'] = datetime.now().strftime("%Y-%m-%d")
    data["channels"][channel_name]['last_uploaded_time'] = datetime.now().strftime("%H:%M:%S")
    save_data()
    return data["channels"][channel_name]["number_of_videos_pending_to_upload"]

# Handle upload failure
def youtube_upload_fail():
    if not data:
        load_data()
    data["channels"][channel_name]["number_of_videos_pending_to_upload"] -= 1
    data["number_of_videos_available_to_upload"] -= 1
    data["channels"][channel_name]['last_uploaded_date'] = datetime.now().strftime("%Y-%m-%d")
    data["channels"][channel_name]['last_uploaded_time'] = datetime.now().strftime("%H:%M:%S")
    save_data()
    return data["channels"][channel_name]["number_of_videos_pending_to_upload"]

def set_channel_metadata(channel_upload_metadata,channel_name_selected):
    global channel_metadata
    global channel_name
    channel_name = channel_name_selected
    channel_metadata = channel_upload_metadata
