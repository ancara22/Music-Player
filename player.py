import pygame										#Game interface
import tkinter as tkr								#Interface module
from tkinter.filedialog import askdirectory         #Ask of directory module
import os											#OS possibility to choose directory

#Main window
window = tkr.Tk()    				#Create main window
window.title("Player")				#Window title
window.geometry("200x250")			#Window sizes

#Player choose directory and create list
directory = askdirectory()			#Ask for directory
os.chdir(directory)					#Chose directory
songlist = os.listdir()				#List of files from directory
playlist = tkr.Listbox(window, 		#Interface list label, with selected option
					   font="Helvetica 12 bold",
					   bg="gray",
					   selectmode=tkr.SINGLE)

for item in songlist:               #Insertation items from choose directory, one by one
	pos = 0							#start position
	playlist.insert(pos, item)		#insert on position 0, item
	pos += 1						#incr

pygame.init()						#Init player actions
pygame.mixer.init()

var = tkr.StringVar()
songtitle = tkr.Label(window, font="Helvetica 12 bold", textvariable=var)


#Functions for buttons
def play():							#Functionto play file
	pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
	var.set(playlist.get(tkr.ACTIVE))
	pygame.mixer.music.play()


def stopP():						#Functionto stop
	pygame.mixer.music.stop()


def pause():						#Functionto pause
	pygame.mixer.music.pause()


def unpause():						#Functionto unpause
	pygame.mixer.music.unpause()


#Buttons
b1 = tkr.Button(window, font="Helvetica 12 bold", bg="red", text="Play", fg="white", command=play)
b2 = tkr.Button(window, font="Helvetica 12 bold", bg="black", text="Stop", fg="white", command=stopP)
b3 = tkr.Button(window, font="Helvetica 12 bold", bg="white", text="Pause", fg="black", command=pause)
b4 = tkr.Button(window, font="Helvetica 12 bold", bg="gray", text="Unpause", fg="black", command=unpause)

#Positioning on the window
songtitle.pack()
b1.pack(fill="x")
b2.pack(fill="x")
b3.pack(fill="x")
b4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

window.mainloop()
