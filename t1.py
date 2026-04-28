import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")

root.geometry("300x200")

label = tk.Label(root, text="Hello GUI")
label.pack()

root.mainloop()
