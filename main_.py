from tkinter import *
import nltk
from nltk.corpus import wordnet

# Download NLTK WordNet data (run this once to download the data)
nltk.download('wordnet')

def fetch_word_details():
    word = entry_word.get().lower()

    # Get word synsets (sets of synonyms)
    synsets = wordnet.synsets(word)

    if synsets:
        # Display the first synset's definition
        meaning.config(text='Meaning: ' + synsets[0].definition())

        # Display synonyms and antonyms
        synonyms = []
        antonyms = []
        for syn in synsets:
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())

        synonym.config(text='Synonyms: ' + ', '.join(synonyms))
        antonym.config(text='Antonyms: ' + ', '.join(antonyms))
    else:
        meaning.config(text='Word not found.')
        synonym.config(text='')
        antonym.config(text='')

root = Tk()
root.geometry("400x400")

Label(root, text="Dictionary", font=("Helvetica 20 bold"), fg="Green").pack(pady=10)

frame = Frame(root)
Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
entry_word = Entry(frame, font=("Helvetica 15 bold"))
entry_word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

frame2 = Frame(root)
Label(frame2, text="Synonym:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)

frame3 = Frame(root)
Label(frame3, text="Antonym:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(root, text="Submit", font=("Helvetica 15 bold"), command=fetch_word_details).pack()

root.mainloop()
