import tkinter as tk
from tkinter import messagebox
 
 
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
 
 
def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
 
 
# Create the main application window
root = tk.Tk()
root.title("To-Do List - The Pycodes")
root.geometry("400x600")
root.configure(bg="black")
tk.Label(root,text="Today's To Do List",font="arial 20 bold",bg="black",fg="red").place(x=70,y=20)
root.resizable(False,False)
 
 
# Create an entry widget for adding tasks
entry = tk.Entry(root, width=40,font="arial 12")
entry.pack(pady=100)
 
 
# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.place(x=175,y=150)
 
 
# Create a frame to contain the listbox and scrollbar
frame = tk.Frame(root,bd=3,width=100)
frame.pack()
 
 
# Create a listbox to display tasks
listbox = tk.Listbox(frame, width=40,height=15, selectmode=tk.SINGLE,bg="grey",fg="white",font="arial 11")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
 
 
# Create a Canvas widget to contain the listbox
canvas = tk.Canvas(frame, bg="grey")
canvas.pack(side=tk.RIGHT, fill=tk.BOTH)
 
 
# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(canvas,orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
 
 
# Configure the listbox to use the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
 
 
# Create a button to delete selected tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.place(x=170,y=530)
 
 
# Start the main event loop
root.mainloop()
