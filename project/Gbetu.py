
import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=150, height=150)
canvas.pack()


canvas.create_line(30, 30, 30, 120, width=10)
canvas.create_line(30, 30, 100, 30, width=10)
canvas.create_line(100, 30, 100, 60, width=10)
canvas.create_line(70, 85, 100, 85, width=10)
canvas.create_line(100, 85, 100, 120, width=10)
canvas.create_line(100, 120, 30, 120, width=10)



root.mainloop()
