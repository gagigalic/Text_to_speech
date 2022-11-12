import os
from tkinter import *
from gtts import gTTS

BACKGROUND_COLOR = "#0E5E6F"
TITLE_FONT = "Arial"
TITLE_COLOR = "#00ADB5"
WORD_FONT = "Times New Roman"
WORD_COLOR = "#EEEEEE"
BTN_BACKGROUND_COLOR = "#0E5E6F"

def play_audio():
    word = text_entry.get()
    tts= gTTS(text = word, lang = "en")
    tts.save("text-audio.mp3")
    play_btn.config(fg =TITLE_COLOR)
    os.startfile("text-audio.mp3")


window = Tk()
window.title("Text to Speech")
window.config(padx= 25, pady= 25, bg = BACKGROUND_COLOR)


title_label = Label(text = "Text to Speech", font=(TITLE_FONT, 54, "bold"), fg=TITLE_COLOR, bg=BACKGROUND_COLOR )
title_label.grid(column = 0, row= 0, pady=40, columnspan = 2)

text_label = Label(text = "Insert text:", font=(TITLE_FONT, 25, "bold"), fg=TITLE_COLOR, bg=BACKGROUND_COLOR )
text_label.grid(column = 0, row= 1, pady=40)

text_entry = Entry(width = 50)
text_entry.grid(column = 1, row = 1, pady = 40)

play_btn= Button(text="Play Audio", font = (WORD_FONT, 35), width = 15, fg = WORD_COLOR, bg =BTN_BACKGROUND_COLOR, command = play_audio )
play_btn.grid(column = 0, row = 2, pady = 5, columnspan = 2)


window.mainloop()
