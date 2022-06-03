#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x250")

#Create a canvas
canvas= Canvas(win, width= 1000, height= 800)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open(r"C:\Users\jaket\Documents\GitHub\Simple-3D-engine\default-preview.png"))

#Add image to the Canvas Items
canvas.create_image(500,400,anchor=CENTER,image=img)

win.mainloop()