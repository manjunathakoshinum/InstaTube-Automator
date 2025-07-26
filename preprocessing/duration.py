from moviepy.editor import VideoFileClip

def get_video_duration(file_path):
    # Load the video file
    if file_path:
        clip = VideoFileClip(file_path)
        duration = clip.duration
        return duration

    else:
        pass
    # Get the duration in seconds
    

