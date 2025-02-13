import tkinter as tk
import datetime

def on_submit(event=None):
    user_input = input_field.get()
    output_field.config(state='normal')
    output_field.insert('end', 'User: ' + user_input + '\n', 'black')
    if user_input in ['hi',"hey"]:
        output_field.insert('end', 'Hello, how can I help you?\n', 'blue')
        
    elif user_input == 'how are you':
        output_field.insert('end', 'I am Okay. How about you?\n', 'blue')

    elif user_input == 'how old are you':
        output_field.insert('end', 'My creator just brought me to life in front of you. I am not much older than 10 minutes.\n', 'blue')

    elif user_input == 'what time is it':
        now = datetime.datetime.now()
        output_field.insert('end', "It's "+ now.strftime("%H:%M:%S %p")+'\n', 'blue')

    elif user_input == 'bye':
        output_field.insert('end', 'Goodbye, have a nice day!\n', 'blue')

    elif user_input == 'who is hod and gui helper of this project':
        output_field.insert('end', 'Suriya thiru.T\n', 'blue')
    
    elif user_input == 'what do you mean by hod?':
        output_field.insert('end', 'Head Of Design \n', 'blue')

    elif user_input == 'who is your creator?':
        output_field.insert('end', 'Mugilan.M\n', 'blue')

    else:
        output_field.insert('end', 'I am sorry, I do not understand.\n', 'blue')
    input_field.delete(0, 'end')
    output_field.config(state='disabled')

root = tk.Tk()
root.title("Chatbot")

p1 = tk.PhotoImage(file = 'chat.png')
root.iconphoto(False, p1)


output_frame = tk.Frame(root)
output_frame.pack(side='top', fill='both', expand=True)

output_label = tk.Label(output_frame, text="Chatbot:")
output_label.pack(side='left', padx=5, pady=5)

output_field = tk.Text(output_frame)
output_field.pack(side='left', fill='both', expand=True, padx=5, pady=5)
output_field.config(state='disabled')
output_field.tag_config('blue', foreground='blue')
output_field.tag_config('red', foreground='red')
output_field.config(font=("Futura", 16))

input_frame = tk.Frame(root)
input_frame.pack(side='bottom', fill='x')

input_label = tk.Label(input_frame, text="User:")
input_label.pack(side='left', padx=5, pady=5)

input_field = tk.Entry(input_frame, width=150)
input_field.pack(side='left', padx=5, pady=5)
input_field.bind("<Return>", on_submit)

submit_button = tk.Button(input_frame, text="Submit", command=on_submit)
submit_button.pack(side='left')

root.mainloop()