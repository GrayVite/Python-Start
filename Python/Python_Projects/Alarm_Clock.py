import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "D:\\Ayan\\Music\\relaxing-guitar-loop-v5-245859.mp3"

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😠")
            is_running = False

            pygame.mixer.init() # initialize the mixer with default settings
            pygame.mixer.music.load(sound_file) # Load our sound file
            pygame.mixer.music.play() # Play our sound file

            # Continue playing our sound file until it finishes playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)