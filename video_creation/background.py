import random
from os import listdir, environ
from pathlib import Path
from random import randrange
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from utils.console import print_step, print_substep


def get_start_and_end_times(video_length, length_of_clip):
    random_time = randrange(180, int(length_of_clip) - int(video_length))
    return random_time, random_time + video_length


def download_background():
    """Downloads the background video from YouTube."""
    Path("./assets/backgrounds/").mkdir(parents=True, exist_ok=True)
    background_options = [  
        ("https://www.youtube.com/watch?v=n_Dv4JMiwK8", "parkour.mp4", "bbswitzer"),
        # (
        #    "https://www.youtube.com/watch?v=2X9QGY__0II",
        #    "rocket_league.mp4",
        #    "Orbital Gameplay",
        # ),
    ]
    # note: make sure the file name doesn't include an - in it
    if not len(listdir("./assets/backgrounds")) >= len(
        background_options
    ):  # if there are any background videos not installed
        print_step(
            "Initializing background video download. This is a one time occurance."
        )
        print_substep("Download started...")
        for uri, filename, credit in background_options:
            if Path(f"assets/backgrounds/{credit}-{filename}").is_file():
                continue  # adds check to see if file exists before downloading
            print_substep(f"Downloading {filename} from {uri}")
            YouTube(uri).streams.filter(res="1080p").first().download(
                "assets/backgrounds", filename=f"{credit}-{filename}"
            )

        print_substep("Background vidoe has been successfully downloaded!", style="bold green")


def chop_background_video(video_length):
    print_step("Locating duration in background video to integrate...")
    choice = random.choice(listdir("assets/backgrounds"))
    environ["background_credit"] = choice.split("-")[0]

    background = VideoFileClip(f"assets/backgrounds/{choice}")

    start_time, end_time = get_start_and_end_times(video_length, background.duration)
    ffmpeg_extract_subclip(
        f"assets/backgrounds/{choice}",
        start_time,
        end_time,
        targetname="assets/temp/background.mp4",
    )
    print_substep("Background video chopped successfully!", style="bold green")
    return True
