import tkinter as tk
from tkinter import messagebox
from render import *
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Display!", command=self.display)
        self.button.pack()
        self.entry.pack()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        

    def display(self):
        self.run()
    def run(self):
        self.subwindow = Render()
        self.subwindow.run_program()
    def on_close(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.destroy()

if __name__ == '__main__':
    Program = App()
    Program.mainloop()
