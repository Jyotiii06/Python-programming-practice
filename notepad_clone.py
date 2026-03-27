import tkinter as tk
from tkinter import filedialog, messagebox

# Functions
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(file_path)

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(file_path)

def exit_app():
    if messagebox.askokcancel("Quit", "Do you really want to exit?"):
        root.destroy()

# Main window
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Text area
text_area = tk.Text(root, wrap="word", font="Arial 12")
text_area.pack(expand=True, fill="both")

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

# Attach menu
root.config(menu=menu_bar)

# Run app
root.mainloop()
