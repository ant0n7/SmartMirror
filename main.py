# Frameworks
import tkinter as tk


print("Hello World\n")

# Create window
root = tk.Tk()

# Create a new widget
myLabel = tk.Label(root, text="Hello World")
myLabel.pack()  # pack it to the screen

root.mainloop()
