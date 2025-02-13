import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox

# Create Object
root = tk.Tk()
root.title("Calendar")

p1 = tk.PhotoImage(file = 'calander_app.png')
root.iconphoto(False, p1)

# Global variables
current_date = datetime.now()
selected_date = current_date

# Function to update the calendar display
def update_calendar():
    global current_date
    first_day = current_date.replace(day=1)
    last_day = (current_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Update the label to display the current month
    month_label.config(text=current_date.strftime('%B %Y'))

    # Remove any existing widgets in the calendar frame
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    # Create buttons for each day in the month
    for day in range((last_day - first_day).days + 1):
        date = first_day + timedelta(days=day)
        day_button = tk.Button(calendar_frame, text=str(date.day), command=lambda d=date: on_date_click(d))
        day_button.grid(row=(day // 7) + 1, column=day % 7, padx=5, pady=5)

# Function to handle date button click
def on_date_click(date):
    global selected_date
    selected_date = date
    date_label.config(text="Selected Date is: " + selected_date.strftime('%Y-%m-%d'))

# Function to show the next month
def next_month():
    global current_date
    current_date = current_date.replace(day=1) + timedelta(days=32)
    update_calendar()

# Function to show the previous month
def prev_month():
    global current_date
    current_date = current_date.replace(day=1) - timedelta(days=1)
    update_calendar()

# Create a frame to hold the calendar
calendar_frame = tk.Frame(root)
calendar_frame.pack(pady=20)

# Create buttons to navigate between months
prev_button = tk.Button(root, text="Previous Month", command=prev_month)
prev_button.pack(side=tk.LEFT, padx=10)
next_button = tk.Button(root, text="Next Month", command=next_month)
next_button.pack(side=tk.RIGHT, padx=10)

# Create a label to display the current month
month_label = tk.Label(root, text="", font=("Helvetica", 16))
month_label.pack()

# Create a label to display the selected date
date_label = tk.Label(root, text="")
date_label.pack(pady=10)

# Update the calendar display
update_calendar()

# Execute Tkinter
root.mainloop()
