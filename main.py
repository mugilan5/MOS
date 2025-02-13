import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import csv
import os

app = tk.Tk()
app.title("Welcome")
img = Image.open("black.png")
bg = ImageTk.PhotoImage(img)

app.geometry("1500x999")

# Add image
label = Label(app, image=bg)
label.place(x=0, y=0)


def on_username_entry_click(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, "end")
        username_entry.config(fg='white')


def on_username_focus_out(event):
    if username_entry.get() == "":
        username_entry.insert(0, "Username")
        username_entry.config(fg='white')


def on_username_entry_click_1(event):
    if username_entry1.get() == "Username":
        username_entry1.delete(0, "end")
        username_entry1.config(fg='white')


def on_username_focus_out_1(event):
    if username_entry1.get() == "":
        username_entry1.insert(0, "Username")
        username_entry1.config(fg='white')


def on_password_entry_click(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, "end")
        password_entry.config(fg='white')
        password_entry.config(show='●')


def on_password_focus_out(event):
    if password_entry.get() == "":
        password_entry.insert(0, "Password")
        password_entry.config(fg='white')
        password_entry.config(show='')


def on_password_entry_click_1(event):
    if password_entry1.get() == "Password":
        password_entry1.delete(0, "end")
        password_entry1.config(fg='white')
        password_entry1.config(show='')


def on_password_focus_out_1(event):
    if password_entry1.get() == "":
        password_entry1.insert(0, "Password")
        password_entry1.config(fg='white')
        password_entry1.config(show='')


def on_email_entry_click(event):
    if email.get() == "Email":
        email.delete(0, "end")
        email.config(fg='white')


def on_email_focus_out(event):
    if email.get() == "":
        email.insert(0, "Email")
        email.config(fg='white')


def chess():
    os.system("python Chess.py")

def notepad():
    os.system("python notepad.py")

def calculator():
    os.system("python calculator.py")

def paint():
    os.system("python paint.py")

def clock():
    os.system("python clock.py")

def chatbot():
    os.system("python chatbot.py")

def weather():
    os.system("python weather.py")

def music():
    os.system("python music_player.py")

def dict_app():
    os.system("python dict_1.py")

def calander_app():
    os.system("python calander.py")

def write_to_csv():
    data = {
        'username': username_entry1.get(),
        "email": email.get(),
        'password': password_entry1.get()}
    with open('storage.csv', newline='', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['username'], data['password'], data['email']])
        messagebox.showinfo("sign up Successful", "You have signed up in Successfully")


def sign__up():
    global username_entry1, password_entry1, email

    signup_window = Toplevel(app)
    signup_window.title("Sign Up")
    signup_window.geometry("1250x833")
    signup_window.resizable(False, False)

    # Load an image for the sign-up window
    img_signup = Image.open("acc.png")
    bg_signup = ImageTk.PhotoImage(img_signup)

    # Create and place the Label widget with the image
    label_signup = Label(signup_window, image=bg_signup)
    label_signup.image = bg_signup  # Keep a reference to the image to prevent it from being garbage collected
    label_signup.pack()

    username_entry1 = Entry(signup_window, bg="black", fg='white', font=('Arial 21'), bd=0)
    username_entry1.insert(0, "Username")
    username_entry1.bind("<FocusIn>", on_username_entry_click_1)
    username_entry1.bind("<FocusOut>", on_username_focus_out_1)
    username_entry1.place(x=490, y=310, height=50)

    email = Entry(signup_window, bg="black", fg='white', font=('Arial 21'), bd=0)
    email.insert(0, "Email")
    email.bind("<FocusIn>", on_email_entry_click)
    email.bind("<FocusOut>", on_email_focus_out)
    email.place(x=490, y=380, height=50)

    password_entry1 = Entry(signup_window, bg="black", fg='white', font=('Arial 21'), bd=0)
    password_entry1.insert(0, "Password")
    password_entry1.bind("<FocusIn>", on_password_entry_click_1)
    password_entry1.bind("<FocusOut>", on_password_focus_out_1)
    password_entry1.place(x=490, y=450, height=50)

    click_btn1 = PhotoImage(file='button.png')

    button1 = Button(signup_window, image=click_btn1, bd=0, command=write_to_csv)
    button1.place(y=540, x=500)

    signup_window.mainloop() 


def update_image(new_image):
    label_new_window.config(image=new_image)
    label_new_window.image = new_image

    # chess_label = Button(new_window, bd=0, image=chess_bg, command=chess)
    # chess_label.image = chess_bg
    # chess_label.place(x=250, y=277)

    note_label = Button(new_window, bd=0, image=note_bg, command=notepad)
    note_label.image = note_bg
    note_label.place(x=423, y=277)

    calculator_label = Button(new_window, bd=0, image=calculator_bg, command=calculator)
    calculator_label.image = calculator_bg
    calculator_label.place(x=780, y=277)

    paint_label = Button(new_window, bd=0, image=paint_bg, command=paint)
    paint_label.image = paint_bg
    paint_label.place(x=949, y=455)

    chatbot_label = Button(new_window, bd=0, image=chatbot_bg, command=chatbot)
    chatbot_label.image = chatbot_bg
    chatbot_label.place(x=600, y=282)

    weather_label = Button(new_window, bd=0, image=weather_bg, command=weather)
    weather_label.image = weather_bg
    weather_label.place(x=423, y=455)

    music_label = Button(new_window, bd=0, image=music_bg, command=music)
    music_label.image = music_bg
    music_label.place(x=249, y=455)

    dict_label = Button(new_window, bd=0, image=dict_bg, command=dict_app)
    dict_label.image = dict_bg
    dict_label.place(x=609, y=455)

    calander_label = Button(new_window, bd=0, image=calander_bg, command=calander_app)
    calander_label.image = calander_bg
    calander_label.place(x=782, y=452)

    calander_label = Button(new_window, bd=0, image=calander_bg, command=calander_app)
    calander_label.image = calander_bg
    calander_label.place(x=782, y=452)

    clock_label = Button(new_window, bd=0, image=clock_bg, command=clock)
    clock_label.image = clock_bg
    clock_label.place(x=952, y=282)


def login():
    global bg_new_window_app, app_button, label_new_window, new_window, chess_bg, bg_new_window1,username_entry,password_entry
    global chatbot_bg,note_bg,calculator_bg,paint_bg,weather_bg,music_bg,dict_bg,calander_bg,clock_bg

    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    with open('storage.csv', newline='') as database:
        csv_reader = csv.reader(database)
        for row in csv_reader:
            username = row[0]
            password = row[1]
            if entered_username == username and entered_password  == password :
                messagebox.showinfo("Login Successful", "You have logged in successfully")
                app.destroy()
                global new_window, bg_new_window1
                new_window = tk.Tk()
                new_window.title("Welcome, User!")
                new_window.geometry("1250x833")
                new_window.resizable(False, False)


                # Add widgets and content to the new window here
                img_new_window = Image.open("window_final.png")
                bg_new_window = ImageTk.PhotoImage(img_new_window)

                img_new_window1 = Image.open("window_final1.png")
                bg_new_window1 = ImageTk.PhotoImage(img_new_window1)

                # chess_img = Image.open("chess.png")
                # chess_bg = ImageTk.PhotoImage(chess_img)

                note_img = Image.open("note.png")
                note_bg = ImageTk.PhotoImage(note_img)

                calculator_img = Image.open("calculator.png")
                calculator_bg = ImageTk.PhotoImage(calculator_img)

                paint_img = Image.open("paint.png")
                paint_bg = ImageTk.PhotoImage(paint_img)

                chatbot_img = Image.open("chatbot.png")
                chatbot_bg = ImageTk.PhotoImage(chatbot_img)

                weather_img = Image.open("weather.png")
                weather_bg = ImageTk.PhotoImage(weather_img)

                music_img = Image.open("music_app.png")
                music_bg = ImageTk.PhotoImage(music_img)

                dict_img = Image.open("dict.png")
                dict_bg = ImageTk.PhotoImage(dict_img)

                calander_img = Image.open("calander_app.png")
                calander_bg = ImageTk.PhotoImage(calander_img)

                clock_img = Image.open("clock.png")
                clock_bg = ImageTk.PhotoImage(clock_img)

                # Create and place the Label widget with the background image
                global label_new_window
                label_new_window = Label(new_window, image=bg_new_window)
                label_new_window.image = bg_new_window  # Keep a reference to the image
                label_new_window.place(x=0, y=0, relwidth=1, relheight=1)

                app_button = Image.open("app_button.png")
                bg_new_window_app = ImageTk.PhotoImage(app_button)
                button = tk.Button(new_window, bd=0, image=bg_new_window_app, command=lambda: update_image(bg_new_window1))
                button.place(y=735, x=580)

                new_window.mainloop()
                return  # Exit the loop once a match is found

    messagebox.showerror("Login Failed", "Invalid Username and Password")

    


username_entry = tk.Entry(bg="black", fg='white', font=('Arial 17'), bd=0)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", on_username_entry_click)
username_entry.bind("<FocusOut>", on_username_focus_out)
username_entry.place(y=315, x=611, width=300, height=40)

password_entry = tk.Entry(bg="black", fg='white', font=('Arial 17'), bd=0)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", on_password_entry_click)
password_entry.bind("<FocusOut>", on_password_focus_out)
password_entry.place(y=385, x=610, width=300, height=40)

click_btn = PhotoImage(file='button.png')
click_btn2 = PhotoImage(file='create_acc.png')

button = tk.Button(image=click_btn, bd=0, command=login)
button.place(y=477, x=607)

signup = tk.Button(image=click_btn2, command=sign__up, bd=0)
signup.place(y=582, x=850)

app.mainloop()