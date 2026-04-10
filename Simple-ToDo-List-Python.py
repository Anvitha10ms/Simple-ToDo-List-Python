import tkinter as tk
from tkinter import messagebox

def add_task():
    """Add a new task to the listbox.
    
    Reads input from the entry field and inserts
    it into the listbox. Shows a warning if empty.
    """
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    """Remove the selected task from the listbox.
    
    Deletes the currently highlighted task.
    Shows a warning if no task is selected.
    """
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_list():
    """Clear all tasks from the listbox.
    
    Removes every task from the display.
    """
    listbox.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create and configure widgets
entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear List", command=clear_list)
listbox = tk.Listbox(root)

# Place widgets in the layout
entry.pack(pady=5)
add_button.pack(pady=5)
remove_button.pack(pady=5)
clear_button.pack(pady=5)
listbox.pack(pady=5)

root.mainloop()
