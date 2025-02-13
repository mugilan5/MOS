import tkinter as tk
from tkinter import messagebox

# Dictionary data
dictionary = {
    "apple": ["A fruit with a sweet or tart taste.", "A technology company."],
    "banana": ["A long, curved fruit that grows in clusters.", "A term for a yellow color."],
    "cherry": ["A small, round fruit that is typically red or black.", "A decorative wood with a reddish-brown color."],
    # Add more words and their meanings as needed
}

def lookup_word():
    word = entry.get().lower()
    meanings = dictionary.get(word, ["Word not found in the dictionary."])
    meanings_text = "\n".join(meanings)
    messagebox.showinfo("Meanings", meanings_text)

def add_word():
    word = entry.get().lower()
    definition = entry_definition.get()
    if word in dictionary:
        dictionary[word].append(definition)
    else:
        dictionary[word] = [definition]
    messagebox.showinfo("Success", "Meaning added to the dictionary.")

def delete_word():
    word = entry.get().lower()
    if word in dictionary:
        del dictionary[word]
        messagebox.showinfo("Success", "Word deleted from the dictionary.")
    else:
        messagebox.showerror("Error", "Word not found in the dictionary.")

# Create the main application window
root = tk.Tk()
root.title("Dictionary App")

p1 = tk.PhotoImage(file = 'dict.png')
root.iconphoto(False, p1)

# Create UI elements
label = tk.Label(root, text="Enter a word:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

lookup_button = tk.Button(root, text="Lookup", command=lookup_word)
lookup_button.pack(pady=5, padx=10)

# Additional UI elements for adding and deleting words
add_label = tk.Label(root, text="Enter a new meaning:")
add_label.pack(pady=10)

entry_definition = tk.Entry(root)
entry_definition.pack(pady=5)

add_button = tk.Button(root, text="Add Meaning", command=add_word)
add_button.pack(pady=5, padx=10)

delete_button = tk.Button(root, text="Delete Word", command=delete_word)
delete_button.pack(pady=5, padx=10)

# Run the application
root.mainloop()
