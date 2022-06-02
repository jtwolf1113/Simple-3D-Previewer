import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import *

from pygame import FULLSCREEN
from render import *
from customfileopenbox import *

class App(TkinterDnD.Tk):
    def __init__(self):
        TkinterDnD.Tk.__init__(self)
        self.file = None
        self.file_shorthand = None
        self.geometry('770x600')
        self.primary_blue = '#045594'
        self.primary_gray = '#424549'
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.title('Wolf\'s 3D engine')
        self.iconbitmap('icon.ico')
        self.font = 'Times 12'
        self.warning_font = 'Times 12 bold'
        self.warning_label = None
        self.warning_text = None

        self.geometry('770x600')
        self.protocol('WM_DELETE_WINDOW', self.on_close)
        
        self.title('Wolf\'s 3D Engine')
        self.iconbitmap('icon.ico')

        self.configure(background = self.primary_blue)
        self.create_UI()
    
    def create_UI(self):

        self.file_selector = tk.Button(self, text="Choose File", command=self.file_select, font =self.font, bg = self.primary_blue,relief = 'solid')
        self.file_selector.pack(pady=5)

        self.selected_file = tk.Label(self, text = f'Selected File: {self.file}', font =self.font,bg = self.primary_blue,relief = 'solid')
        self.selected_file.pack(pady=2.5)

        self.preview_frame = tk.Canvas(self, height=22, width=50)
        self.preview_frame.pack()
        self.preview_frame_text = tk.Label(self.preview_frame, text = 'Drag and Drop Files Here', font = self.font+' bold', fg = self.primary_blue, bg = 'white', borderwidth=1, relief = 'solid', highlightcolor='black')
        self.preview_frame_text.pack()
        self.preview_frame.drop_target_register(DND_FILES)
        self.preview_frame.dnd_bind('<<Drop>>', self.drag_and_drop_file_select)

        self.fullscreen = False
        self.fullscreen_check = tk.Checkbutton(self, text='Fullscreen', command=self.fullscreen_select, font =self.font, bg = self.primary_blue, relief = 'solid')
        self.fullscreen_check.pack()

        self.vertices = False
        self.vertices_check_var = False
        self.vertices_check = tk.Checkbutton(self, text='Render Vertices', var = self.vertices_check_var, command=self.vertices_select, font =self.font, bg = self.primary_blue, relief = 'solid')
        self.vertices_check.pack()

        self.launch_button = tk.Button(self, text="Display!", command=self.display, font =self.font, bg = self.primary_blue, relief = 'solid')
        self.launch_button.pack(pady=2.5)

        

    def file_select(self): 
        filetypes = [['*.stl', '*.obj', '*.3mf', 'Compatible 3D Files']]
        self.file = custom_fileopenbox(filetypes=filetypes, multiple=False, title='Select a single 3D Compatible File for Wolf\'s 3D Engine', icon = self.iconbitmap)
        self.file_shorthand = self.file.split('\\')[-1]
        self.selected_file['text'] = f'Selected File: {self.file_shorthand}'

        if '.obj' in self.file or '.stl' in self.file or '.3mf' in self.file:
            if self.warning_label is not None:
                self.warning_label.destroy()
                self.warning_label = None
                self.warning_text = None
        else:
            self.warning_text = 'Warning: Incompatible Filetype'
            self.raise_warning()
    
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

    def drag_and_drop_file_select(self, event):
        self.preview_frame.delete()

        self.file = event.data
        if '{' in self.file:
            self.file = self.file[1:-1]
        print(type(self.file), self.file)
        self.file_shorthand = self.file.split('/')[-1]
        self.selected_file['text'] = f'Selected File: {self.file_shorthand}'

        if '.obj' in self.file or '.stl' in self.file or '.3mf' in self.file:
            if self.warning_label is not None:
                self.warning_label.destroy()
                self.warning_label = None
                self.warning_text = None
        else:
            self.warning_text = 'Warning: Incompatible Filetype'
            self.raise_warning()
        

    def raise_warning(self):
        if self.warning_label is not None:
            self.warning_label['text'] = self.warning_text
        else:
            self.warning_label = tk.Label(self, text= self.warning_text, fg = 'red', bg = self.primary_gray)
            self.warning_label.pack()


    def display(self):
        self.subwindow = Render(file = self.file, fullscreen = self.fullscreen, draw_vertices=self.vertices)
        self.subwindow.run_program()
    
    def on_close(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.destroy()

if __name__ == '__main__':
    Program = App()
    Program.mainloop()
