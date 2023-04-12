# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300,bg="green")
canvas.pack(fill = BOTH, expand = 1)

#canvas2=Canvas(win, width=500, height=300,bg="red")
#canvas2.pack(fill = BOTH, expand = 1)

# Add a line in canvas widget
canvas.create_line(30, 30, 30, 120, width=10)
canvas.create_line(30, 30, 100, 30, width=10)
canvas.create_line(100, 30, 100, 60, width=10)
canvas.create_line(70, 85, 100, 85, width=10)
canvas.create_line(100, 85, 100, 120, width=10)
canvas.create_line(100, 120, 30, 120, width=10)



win.mainloop()
