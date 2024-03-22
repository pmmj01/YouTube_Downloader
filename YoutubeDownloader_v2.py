from pytube import YouTube
import os
import time
import sys
import json
from datetime import datetime

current_user_directory = os.path.expanduser("~")
current_user = os.path.basename(current_user_directory)

speed_list = []

settings = {}

base_path = os.path.dirname(os.path.abspath(__file__))
settings_path = os.path.join(base_path, 'settings.txt')
translations_path = os.path.join(base_path, 'translations.json')

with open(settings_path, 'r') as settings_file:
    for line in settings_file:
        key, value = line.strip().split('=')
        settings[key.strip()] = value.strip()
        
with open(translations_path, 'r', encoding='utf-8') as translate_file:
    translations = json.load(translate_file)

if settings['language'] in translations:
    translate_file = translations[settings['language']]
else:
    translate_file = translations['english']


def progress(stream, chunk, bytes_remaining):
    global start_time
    
    total_size = stream.filesize
    file_size = total_size / 1024000
    
    bytes_downloaded = total_size - bytes_remaining
    
    live_progress = (bytes_downloaded / total_size) * 100
    live_MB_downloaded = bytes_downloaded / 1024000
    
    end_time = time.time()
    time_diff = end_time - start_time
    live_speed = len(chunk) / (1024 * time_diff)
    
    real_speed = live_speed
    
    if real_speed >= 1024:
        real_speed /= 1024
        speed_unit = "Mb/s"
    else:
        speed_unit = "kb/s"
    
    speed_list.append(live_speed)
    
    if stream.resolution != None:
        current_quality = (f" {translate_file['1c']}{stream.resolution}")
    else:
        current_quality = ""
    
    sys.stdout.write(f"\r{translate_file['1a']} {live_progress:.2f}% - ({live_MB_downloaded:.3f} MB / {file_size:.3f} MB){current_quality}. {translate_file['1b']}{real_speed:.2f} {speed_unit}     ")
    sys.stdout.flush()
    
    start_time = end_time


def user_choice():
    while True:
        format_choice = input(f"{translate_file['2a']}\n{translate_file['string_to_exit']}\n").lower()
        if format_choice in ["mp4", "4", "mp3", "3"]:
            print(f"\n{translate_file['3a']}\n\033[92mmp{format_choice}\033[0m" if format_choice in ['3', '4'] else f"\nZostał wybrany format: \n\033[92m{format_choice}\033[0m")
            break
        elif format_choice.lower() == 'exit' or format_choice.lower() == 'e':
            exit()
        else:
            print(f"\n\033[91m{translate_file['4a']}\033[0m\n")
        
    while True:
        link_input = input(f"\n{translate_file['5a']}\n{translate_file['string_to_exit']}\n")
        print("")
        
        if link_input.lower() == 'exit' or link_input.lower() == 'e':
            exit()
        elif link_input.startswith("https://www.youtube.") or link_input.startswith("youtube.") or link_input.startswith("www.youtube."):
            try:
                yt = YouTube(link_input, on_progress_callback=progress)
                break
            except Exception as e:
                print(f"\n\033[91mBłąd: {translate_file['6a']}\nError:\n{e}\033[0m\n")
                response = input(f"\033[96m{translate_file['6b']}\033[0m ")
                if response.lower() != 'tak' or response.lower() != 't' or response.lower() != 'yes' or response.lower() != 'y':
                    exit()
        else:
            print(f"\n\033[91m{translate_file['7a']}\033[0m\n")
        
    return format_choice, yt


def save_data_to_file(title, weight, speed, output_path):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = f"| {current_datetime} | {title} | {weight:.2f} MB | {speed:.2f} KB/s | {output_path}\n"
    
    file_exists = os.path.exists("download_data.txt")
    
    with open('download_data.txt', 'a' if file_exists else 'w', encoding='utf-8') as file:
        if not file_exists:
            file.write("|   Data i godzina    |                 Tytuł                  |    Waga    |   Prędkość    |\n")
        file.write(data)


def download_video(format_choice, yt, output_path=None):
    try:
        global start_time
        start_time = time.time()
        
        if format_choice in ["mp4", "4"]:
            quality_levels = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']

            for quality in quality_levels:
                video = yt.streams.filter(file_extension="mp4", progressive=True, resolution=quality).first()
                if video:
                    break

            if not video:
                print(f"\033[91m{translate_file['11a']}\033[0m")
            else:
                print(f"\033[96m{translate_file['11b']}\033[0m\033[92m{video.resolution}\033[0m")
            
        elif format_choice in ["mp3", "3"]:
            video = yt.streams.filter(only_audio=True).first()

        if output_path is None:
            output_path = video.download()
        else:
            output_path = video.download(output_path)
            
        if format_choice.lower() in ['mp3', '3']:
            audio_path = os.path.splitext(output_path)[0] + '.mp3'
            os.rename(output_path, audio_path)
            output_path = audio_path

        print(f"\n\n{translate_file['8a']}\n\033[92m{output_path}\033[0m")
        
        convert_speed = lambda x: "{:.2f} Mb/s".format(x / 1024) if x >= 1024 else "{:.2f} kb/s".format(x)
        
        avg_speed = ((lambda x: x / 1024 if x >= 1024 else x)(sum(speed_list))) / len(speed_list)
        avg_speed_formatted = "{:.2f} Mb/s".format(avg_speed) if avg_speed >= 1 else "{:.2f} kb/s".format(avg_speed * 1024)

        max_speed = convert_speed(max(speed_list))
        min_speed = convert_speed(min(speed_list))
        
        file_size = os.path.getsize(output_path) / 1e6
        
        title = video.title
        weight = video.filesize / (1024 * 1024)

        print(f"\n{translate_file['9a']}\033[92m{avg_speed_formatted}\033[0m")
        print(f"{translate_file['9b']}\033[92m{max_speed}\033[0m")
        print(f"{translate_file['9c']}\033[92m{min_speed}\033[0m\n")
        
        save_data_to_file(title, file_size, avg_speed, output_path)


    except Exception as e:
        print(f"\n\033[91m{translate_file['10a']}{e}\033[0m\n")
        response = input(f"\033[96m{translate_file['6b']}\033[0m\n")
        if response.lower() not in ['tak', 't', 'yes', 'y']:
            exit()
            

if __name__ == "__main__":
    print("YT_Downloader ver.1.3")
    while True:
        format_choice, yt = user_choice()
        download_video(format_choice, yt, output_path=f"C:\\Users\\{current_user}\\Downloads")
        