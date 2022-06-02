from tkinter import *
from tkinterdnd2 import *

def DisplayText(event):
    # delete entire existing content
    textbox.delete("1.0","end")
    # check the file holds txt extension
    if event.data.endswith(".txt"):
        with open(event.data, "r") as f:
            # getting content in a variable
            for text_line in f:
                text_line=text_line.strip()
                textbox.insert("end",f"{text_line}\n")
win = TkinterDnD.Tk()
win.title('Delftstack')
win.geometry('500x400')
win.config(bg='gold')

frame = Frame(win)
frame.pack()

textbox = Text(frame, height=22, width=50)
textbox.pack(side=LEFT)
textbox.drop_target_register(DND_FILES)
textbox.dnd_bind('<<Drop>>', DisplayText)

scrolbar = Scrollbar(frame, orient=VERTICAL)
scrolbar.pack(side=RIGHT, fill=Y)

textbox.configure(yscrollcommand=scrolbar.set)
scrolbar.config(command=textbox.yview)

win.mainloop()