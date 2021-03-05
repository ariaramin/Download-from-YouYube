from tkinter.font import Font
from PIL import ImageTk, Image
from pytube import *
from tkinter import Label, Button, Entry, StringVar, Tk

master = Tk()
master.geometry('420x300')
master.title('Download from YT')


def Download():
    global url, str_btn
    str_btn.set('Waiting...')
    try:
        link = url.get()
        YouTube(link).streams.get_highest_resolution().download()
    except:
        Label(master, text='Error', font=font).grid(row=2, column=0)
        str_btn.set('Error!')
    finally:
        str_btn.set('Done')


font = Font(family='Verdana', size=25)
Label(master, text='Download from YouTube', font=font).grid(row=0, column=0)

load = Image.open('youtube.png')
youtube_img = ImageTk.PhotoImage(load)
Label(master, image=youtube_img).grid(row=1, column=0)

url = StringVar()
Entry(master, textvariable=url, width=30).grid(row=3, column=0)

str_btn = StringVar()
str_btn.set('Download')
Button(master, textvariable=str_btn, command=Download).grid(row=4, column=0)

master.mainloop()
