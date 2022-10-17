from gtts import gTTS
from tkinter import *  # For GUI
import os
import random


# Converts Text audio Function
def convert_audio(event):
    text_info = text.get()
    audio = gTTS(text=text_info, lang="en", tld='co.uk', slow=False)
    no = random.randint(4, 9999)
    file = "{number}audio.mp3".format(number=no)
    audio.save(file)
    os.system(file)
    text_entry.delete(0, END)


# Making of a Window
app = Tk()
app.geometry('500x500')
app.configure(bg='black')
app.title("Text to Audio App")
heading = Label(text="Python Text to Audio App", bg="black", font=("Arial", "15"), fg="white", width="500", height="3")
heading.pack()

# Text Box
text_box = Label(text="Text :", font=("Arial", 12, "bold"), fg="white", bg="black")
text_box.place(x=25, y=80)

text = StringVar()

# Text entry Box
text_entry = Entry(textvariable=text, width=65)
text_entry.place(x=73, y=83)

# convert Audio Button
button = Button(text="Convert to Audio", command=convert_audio, width="55", height="1", bg="black", fg="white",
                font=("Arial", 10, "bold"))
button.place(x=25, y=120)

# Binding Enter Key with the Window
app.bind('<Return>', convert_audio)
mainloop()
