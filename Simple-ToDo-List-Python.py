import tkinter as tk
from tkinter import messagebox
def add_task():
    """Add a new task to the listbox."""
    task = entry.get()
    if task:
        # Validate task length
        if len(task) > 100:
            messagebox.showwarning("Warning", "Task too long.")
            return
        if task.strip() == "":
            messagebox.showwarning("Warning", "Task cannot be blank.")
            return
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    """Remove the selected task from the listbox."""
    selected_task_index = listbox.curselection()
    if selected_task_index:
        # Validate task length
        if len(entry.get()) > 100:
            messagebox.showwarning("Warning", "Task too long.")
            return
        if entry.get().strip() == "":
            messagebox.showwarning("Warning", "Task cannot be blank.")
            return
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
