#Task 1 Given by CodSoft - python program to creat a To-Do-List.
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import json
from datetime import datetime

# Load tasks from a file when the application starts
def load_tasks():
    """Load tasks from a JSON file into the listbox."""
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)  # Load tasks from the JSON file
            for task in tasks:
                task_listbox.insert(tk.END, task)  # Insert each task into the listbox
    except FileNotFoundError:
        pass  # If no tasks.json exists, skip loading

# Save tasks to a file
def save_tasks():
    """Save the current tasks in the listbox to a JSON file."""
    tasks = []  # List to hold all tasks
    for i in range(task_listbox.size()):  # Iterate over each task in the listbox
        tasks.append(task_listbox.get(i))  # Append task text
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)  # Save tasks as JSON

# Add a new task
def add_task():
    """Add a new task to the listbox and save it."""
    task = task_entry.get()  # Get the task text from the entry
    if task:
        task_listbox.insert(tk.END, task)  # Add task to the listbox
        task_entry.delete(0, tk.END)  # Clear the entry box
        save_tasks()  # Save tasks after adding
    else:
        messagebox.showwarning("Input Error", "Please enter a task to add.")

# Add a new task with a deadline
def add_task_with_deadline():
    """Add a new task with a deadline to the listbox and save it."""
    task = task_entry.get()  # Get the task text from the entry
    deadline_str = simpledialog.askstring("Deadline", "Enter deadline (YYYY-MM-DD):")  # Prompt for deadline
    if task and deadline_str:
        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()  # Parse the deadline
            task_with_deadline = f"{task} (Deadline: {deadline})"  # Format task with deadline
            task_listbox.insert(tk.END, task_with_deadline)  # Add task to the listbox
            task_entry.delete(0, tk.END)  # Clear the entry box
            save_tasks()  # Save tasks after adding
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid date in YYYY-MM-DD format.")
    else:
        messagebox.showwarning("Input Error", "Please enter a task and a deadline.")

# Remove the selected task
def remove_task():
    """Remove the selected task from the listbox and save changes."""
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        task_listbox.delete(selected_task_index)  # Remove the task from the listbox
        save_tasks()  # Save after removing a task
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Edit the selected task
def edit_task():
    """Edit the selected task in the listbox."""
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        existing_task = task_listbox.get(selected_task_index)  # Get the existing task text
        updated_task = simpledialog.askstring("Update Task", "Modify your task:", initialvalue=existing_task)  # Prompt for new task text
        if updated_task:  # Check if the updated task is not empty
            task_listbox.delete(selected_task_index)  # Remove the old task from the list
            task_listbox.insert(selected_task_index, updated_task)  # Insert the updated task
            save_tasks()  # Save after editing
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to modify.")

# Toggle task completion
def toggle_completion():
    """Toggle the completion status of the selected task."""
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        current_task = task_listbox.get(selected_task_index)  # Get the current task text
        
        # Toggle completion status by adding/removing strikethrough
        if current_task.startswith("✔ "):  # Check if the task is already marked as completed
            updated_task = current_task[2:]  # Remove the completion indicator
        else:
            updated_task = "✔ " + current_task  # Add the completion indicator
        
        task_listbox.delete(selected_task_index)  # Remove the old task
        task_listbox.insert(selected_task_index, updated_task)  # Insert the updated task
        save_tasks()  # Save after toggling
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to toggle.")

# Main function for setting up the GUI
def main_app():
    """Setup and run the main application."""
    global task_listbox, task_entry

    # Main window setup
    app_window = tk.Tk()
    app_window.title("Task-1 To-Do List")
    app_window.geometry("800x600")  # Set window size
    app_window.configure(bg='lightblue')  # Set background color

    # Frame to hold the task list and scrollbar
    frame_task_list = tk.Frame(app_window, bg='lightblue')
    frame_task_list.pack(pady=10)

    # Listbox to display tasks
    task_listbox = tk.Listbox(frame_task_list, width=80, height=20, selectbackground="lightgreen")
    task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Scrollbar for the listbox
    task_scrollbar = tk.Scrollbar(frame_task_list)
    task_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    task_listbox.config(yscrollcommand=task_scrollbar.set)  # Connect scrollbar to listbox
    task_scrollbar.config(command=task_listbox.yview)

    # Entry field for new tasks
    task_entry = tk.Entry(app_window, width=60)
    task_entry.pack(pady=10)

    # Frame to hold buttons for task actions
    button_frame = tk.Frame(app_window, bg='lightblue')
    button_frame.pack(pady=10)

    # Buttons for adding, removing, editing, and toggling tasks
    add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg='lightgreen')
    add_button.pack(side=tk.LEFT, padx=5)

    add_deadline_button = tk.Button(button_frame, text="Add Task with Deadline", command=add_task_with_deadline, bg='lightyellow')
    add_deadline_button.pack(side=tk.LEFT, padx=5)

    remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, bg='lightcoral')
    remove_button.pack(side=tk.LEFT, padx=5)

    edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task, bg='lightblue')
    edit_button.pack(side=tk.LEFT, padx=5)

    complete_button = tk.Button(button_frame, text="Toggle Completion", command=toggle_completion, bg='lightgreen')
    complete_button.pack(side=tk.LEFT, padx=5)

    # Load tasks when the application starts
    load_tasks()

    # Start the GUI event loop
    app_window.mainloop()

# Run the application
if __name__ == "__main__":
    main_app()
