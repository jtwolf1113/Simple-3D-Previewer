# Simple 3D previewer

## Features

This is a simple GUI for file selection and 3D object viewing using Python. This program supports .f3d, .stl and .obj file extensions. 
Files can be drag and dropped into the program, or they can be selected using the choose file button. 
The Program renders the object by reading the file data and creating a 3D projection using pygame. 
A preview will be shown in the picture below the choose file button. The default scene will be shown on launch.
When display button is clicked, a pygame window displaying the object will open.
The object can be moved using wasdqe keys and rotated about x and y axes using the arrow keys. 
#### **To get a better understanding of the keyboard controls, use the default scene which depicts the world axes as well as the object axes.** 

## Features to be Added

* Automatic Default Camera Positioning to display the full extent of the object in frame. 
* More thorough error handling during file selection and display. 
* Performance improvements using cython and/or numba (tbd) to improve FPS for highly detailed files. 
* Additional Pygame environment customizability - default motion, axes display, controls, and rates of motion.
* Aesthetic improvements to UI. 

## **More to Come Soon!**
