import time
import os
import platform

def load_frames(file_name):
    frames = []
    with open(file_name, 'r') as file:
        frame = ""
        for line in file:
            if line.startswith("Frame "):
                if frame:
                    frames.append(frame)
                frame = ""
            else:
                frame += line
        if frame:
            frames.append(frame)
    return frames

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def animate_ascii_art(frames, frame_delay, loop=True):
    try:
        while loop:
            for frame in frames:
                print(frame)
                time.sleep(frame_delay / 1000)
                clear_screen()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    frame_delay = 100  # Delay in milliseconds
    frames = load_frames("frames.txt")
    animate_ascii_art(frames, frame_delay)
