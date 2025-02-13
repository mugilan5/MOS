import tkinter as tk
from tkinter import messagebox
import time
import winsound

# Initialize alarm_time and timer_duration as global variables
alarm_time = ""
timer_duration = 0

# Function to update the clock
def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    check_alarm()
    root.after(1000, update_clock)  # Update every second

# Function to set an alarm
def set_alarm():
    global alarm_time
    alarm_time = entry_alarm.get()
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

# Function to start the timer
# Function to start the timer
def start_timer():
    global timer_duration
    timer_input = entry_timer.get()
    if timer_input.isdigit():
        timer_duration = int(timer_input)
        messagebox.showinfo("Timer Started", f"Timer set for {timer_duration} seconds")
        root.after(timer_duration * 1000, lambda: show_message("Timer Finished", "Timer finished"))
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the timer.")


# Function to check the alarm
def check_alarm():
    current_time = time.strftime('%H:%M:%S')
    if current_time == alarm_time:
        play_sound()
        show_message("Alarm", "Alarm time reached")

# Function to play a sound
def play_sound():
    winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second

# Function to show a message box
def show_message(title, message):
    messagebox.showinfo(title, message)

# Create the main application window
root = tk.Tk()
root.title('Clock, Alarm, and Timer App')

p1 = tk.PhotoImage(file = 'clock.png')
root.iconphoto(False, p1)

# Clock label
clock_label = tk.Label(root, font=('Arial', 24), bg='white', fg='black')
clock_label.pack(pady=10)

# Alarm section
tk.Label(root, text="Set Alarm (HH:MM:SS):").pack(pady=5)
entry_alarm = tk.Entry(root)
entry_alarm.pack(pady=5)
tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=5)

# Timer section
tk.Label(root, text="Set Timer (seconds):").pack(pady=5)
entry_timer = tk.Entry(root)
entry_timer.pack(pady=5)
tk.Button(root, text="Start Timer", command=start_timer).pack(pady=5)

# Run the clock update function
update_clock()

# Start the main event loop
root.mainloop()
