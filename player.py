#impoertign necessary modules
import pygame
import tkinter as tkr 
from tkinter.filedialog import askdirectory #to seect 
import os
#creating app. window
musicplayer = tkr.Tk() 
#setting the title
musicplayer.title("VISION Players")

#setting dimensions
musicplayer.geometry("750x650")
#choosing the folder of the playlist
directory = askdirectory();
#setting dirctor y to current
os.chdir(directory)
#creating songlist   os.dir return a list containing the anmes and etheentries of the directory
#given by the user
songlist = os.listdir()
#creating playlist
playlist = tkr.Listbox(musicplayer, font = "Arial 14 bold", bg = "lightblue", selectmode = tkr.SINGLE)
#adding songs to the playlist
for item in songlist:
     pos = 0
     playlist.insert(pos,item)
     pos = pos+1
#initialising the modules
pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def Exit():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()
def resume():
    pygame.mixer.music.unpause()

text = tkr.Label(musicplayer, text = "VISION MUSIC PLAYERS !!" ,font = "Arial 15 bold")
text.place(x = 250)
Button1 = tkr.Button(musicplayer, width=5,
height=3, font="Arial 16 bold", text="PlayMusic", command=play, bg="red",
fg="black")
Button2 = tkr.Button(musicplayer, width=5,
height=3, font="Arial 16 bold", text="Stop Music", command=Exit,  bg="black", fg="white")
Button3 = tkr.Button(musicplayer, width=5,
height=3, font="Arial 16 bold", text="Pause Music", command=pause, bg="red", fg="black")
Button4 = tkr.Button(musicplayer, width=5,
height=3, font="Arial 16 bold", text="Resume Music", command=resume, bg="black", fg="white")
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,
font="Helvetica 12 bold", textvariable=var)
songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")
musicplayer.mainloop()