from youtube_channel.check_up_policy_upload import can_i_download_video,download_update
from  instagram_download.instagram_download import main_download_reels 
def download_instagram_videos(download_configuration_file):
    try:
        number_of_videos_to_downalod = can_i_download_video()
        if number_of_videos_to_downalod >0:
            total_downloaded_videos = main_download_reels(number_of_videos_to_downalod,download_configuration_file)
            if total_downloaded_videos < number_of_videos_to_downalod:
                to_download = number_of_videos_to_downalod - total_downloaded_videos 
                downloaded = main_download_reels(to_download,download_configuration_file)
                total_downloaded_videos +=downloaded
            remainng_videos = download_update(total_downloaded_videos)
            print(f"sucessfully downaloded videos 📽️ f{total_downloaded_videos} now we have in total 😎 {remainng_videos}")
    except Exception as e:
        print(f"error in downalod check {e}")
        