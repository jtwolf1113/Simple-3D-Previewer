import tkinter as tk
from tkinter import messagebox

from pygame import FULLSCREEN
from render import *
from easygui import fileopenbox

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.file = None
        self.geometry('770x600')
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.title('Wolf\'s 3D engine')
        self.iconbitmap('icon.ico')
        self.create_UI()
    
    def create_UI(self):
        self.file_selector = tk.Button(self, text="Choose File", command=self.file_select)
        self.file_selector.pack(pady=5)

        self.selected_file = tk.Label(self, text = f'Selected File: {self.file}')
        self.selected_file.pack(pady=2.5)



        self.fullscreen = False
        self.fullscreen_check = tk.Checkbutton(text='Fullscreen', command=self.fullscreen_select)
        self.fullscreen_check.pack()

        self.vertices = True
        self.vertices_check_var = tk.BooleanVar(value = True)
        self.vertices_check = tk.Checkbutton(text='Render Vertices', var = self.vertices_check_var, command=self.vertices_select)
        self.vertices_check.pack()

        self.launch_button = tk.Button(self, text="Display!", command=self.display)
        self.launch_button.pack(pady=2.5)

    def file_select(self): 
        filetypes = [['*.stl', '*.obj', '*.3mf', 'Compatible 3D Files']]
        self.file = fileopenbox(filetypes=filetypes, multiple=False)
        self.selected_file['text'] = f'Selected File: {self.file}'
    
    def fullscreen_select(self):
        if self.fullscreen:
            self.fullscreen = False
        elif not self.fullscreen:
            self.fullscreen = True
    def vertices_select(self):
        if self.vertices:
            self.vertices = False
        elif not self.vertices:
            self.vertices = True
    '''   
    def display_preview(self, event):
        if event.data.endswith('.3mf'):
            object_3d = Render.read_3mf(file = event.data)
    '''

    def display(self):
        self.subwindow = Render(file = self.file, fullscreen = self.fullscreen, draw_vertices=self.vertices)
        self.subwindow.run_program()
    
    def on_close(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.destroy()

if __name__ == '__main__':
    Program = App()
    Program.mainloop()
