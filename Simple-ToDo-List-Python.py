import tkinter as tk
from tkinter import messagebox
def validate_task(task):
    """Validate task input. Returns True if valid, False otherwise.
    
    Checks that task is not empty, not blank, and under 100 chars.
    """
    if not task:
        messagebox.showwarning("Warning", "Please enter a task.")
        return False
    if len(task) > 100:
        messagebox.showwarning("Warning", "Task too long.")
        return False
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be blank.")
        return False
    return True

def add_task():
    """Add a new task to the listbox."""
    task = entry.get()
    if validate_task(task):  # single call
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    """Remove the selected task from the listbox."""
    selected_task_index = listbox.curselection()
    if selected_task_index:
        if validate_task(entry.get()):  # single call
            listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_list():
    """Clear all tasks from the listbox."""
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
