import tkinter as tk
from tkinter import filedialog
import pygame
from PIL import Image, ImageTk

playlist = []
current_track_index = 0

def add_song():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        playlist.append(file_path)

def play_music():
    global current_track_index
    if playlist:
        pygame.mixer.music.load(playlist[current_track_index])
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

def play_next():
    global current_track_index
    if playlist:
        current_track_index = (current_track_index + 1) % len(playlist)
        play_music()

def play_previous():
    global current_track_index
    if playlist:
        current_track_index = (current_track_index - 1) % len(playlist)
        play_music()

# Initialize Pygame mixer
pygame.init()
pygame.mixer.init()

root = tk.Tk()
root.title("Music Player")

p1 = tk.PhotoImage(file = 'music_app.png')
root.iconphoto(False, p1)

root.configure(bg="#2E2E2E")
img = Image.open("music_player.png")
bg = ImageTk.PhotoImage(img)

root.geometry("640x360")

root.resizable(False,False)

# Add image
label = tk.Label(root, image=bg)
label.place(x=0, y=0)

# Text styles
label_style = {"font": ("Arial", 12), "fg": "#FFFFFF", "bg": "#2E2E2E"}

# Buttons with images
play_button_img = Image.open("play.png")
play_photo = ImageTk.PhotoImage(play_button_img)

pause_button_img = Image.open("pause.png")
pause_button_img = pause_button_img.resize((50, 50))
pause_photo = ImageTk.PhotoImage(pause_button_img)

stop_button_img = Image.open("stop.png")
stop_button_img = stop_button_img.resize((50, 50))
stop_photo = ImageTk.PhotoImage(stop_button_img)

next_button_img = Image.open("next.png")
next_photo = ImageTk.PhotoImage(next_button_img)

prev_button_img = Image.open("prev.png")
prev_photo = ImageTk.PhotoImage(prev_button_img)

add_button_img = Image.open("add.png")
add_button_img = add_button_img.resize((50, 50))
add_photo = ImageTk.PhotoImage(add_button_img)

# Buttons with images
play_button = tk.Button(root, image=play_photo, command=play_music, bd=0)
play_button.place(x=260,y=240)

next_button = tk.Button(root, image=next_photo, command=play_next, borderwidth=0)
next_button.place(x=430,y=260)

prev_button = tk.Button(root, image=prev_photo, command=play_previous, borderwidth=0)
prev_button.place(x=140,y=260)

add_button = tk.Button(root, image=add_photo, command=add_song,borderwidth=0)
add_button.place(x= 550,y=25)



root.mainloop()