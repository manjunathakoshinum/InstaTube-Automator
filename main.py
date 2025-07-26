from instagram_download.download_check import download_instagram_videos
from youtube_channel.channel_selection import channel_selection,channel_upload_data_selection
from youtube_channel.check_up_policy_upload import load_data,can_i_upload_video_to_youtube,upload_update,youtube_upload_fail,set_channel_metadata
from preprocessing.preprocessing import preprocessing
from upload_to_youtube.youtube_upload import youtube_upload_video
from cleanup.delete_uploaded_files import delete_files_and_update_json
from preprocessing.duration import get_video_duration
def main(channel_name):
    try:
    
        channel_metadata,download_configuration_file,upload_details,firefox_profile_upload = channel_selection(channel_name)
        set_channel_metadata(channel_metadata,channel_name)#channel details linke total upload today
        load_data() # load channel meta data
        #downlaod videos 
        number_of_video_can_we_upload = can_i_upload_video_to_youtube()
        if number_of_video_can_we_upload >0:
            print(f"iam downloding {number_of_video_can_we_upload} videos")
            download_instagram_videos(download_configuration_file)
            videos_path_file,geckodriver_path,made_for_kids,age_restriction,category,sort_by,visibility,command_for_title,command_for_description,command_for_tags,commad_for_hashtags =channel_upload_data_selection(upload_details)
            #prepare for upload get video file,thumbnail, get title, tags, description 
            
            video_file,title,description,tags,image_file,text_file= preprocessing(videos_path_file,geckodriver_path,command_for_title,command_for_description,command_for_tags,commad_for_hashtags) 
            duration = get_video_duration(video_file)
            if duration:
                if duration <= 95:
                    print(duration)
                    print(f"starting  😜 🚗...... {channel_name}")
                    sucess = youtube_upload_video(duration,firefox_profile_upload,video_file,title,description,tags,made_for_kids,age_restriction,sort_by,visibility,category)
                    match sucess:
                        case 0:
                            print("video uploaded sucessfully 😎")
                            upload_update()
                        case 1:
                            print("upload fail")
                            youtube_upload_fail()
        
                    delete_files_and_update_json(video_file, text_file, image_file, videos_path_file)
                    print("sucessfully cleaned 🧹 ")
                else:
                    delete_files_and_update_json(video_file, text_file, image_file, videos_path_file)
                    print("sucessfully cleaned")
    except Exception as e:
        print(f"{e}")
   
   
        
if __name__ == "__main__":
    
    #channels = ["channel_one","channel_two"] #you can add as much channels along with changing the config , channel selection etc same as in meems
    #or selection in channels:
        main("MrKoshinum_meems")