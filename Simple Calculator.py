import tkinter as tk

# Function to handle arithmetic operations
def calculate_expression():
    """
    Evaluates the current expression entered by the user and updates the display with the result.
    If there's an error in the expression (like division by zero), 'Error' is displayed.
    """
    try:
        # Get the current expression from the entry field and evaluate it
        result = eval(entry.get())
        # Clear the entry field and display the result
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        # Update the history with the completed calculation
        update_history(f"{entry_history.get()} = {result}")
    except Exception as e:
        # If an error occurs (e.g., invalid syntax), display 'Error'
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def on_button_click(event):
    """
    Handles the click event for all buttons on the calculator.
    Performs different actions based on which button is clicked.
    """
    text = event.widget.cget("text")  # Get the text of the clicked button
    
    if text == "=":
        # If '=' button is clicked, evaluate the expression
        calculate_expression()
    elif text == "C":
        # If 'C' button is clicked, clear the entry field
        entry.delete(0, tk.END)
    else:
        # For other buttons, insert the corresponding text into the entry field
        entry.insert(tk.END, text)

# Function to update the calculation history
def update_history(recent_entry):
    """
    Updates the history display with the most recent calculation.
    The history is shown above the main entry field.
    """
    entry_history.delete(0, tk.END)
    entry_history.insert(tk.END, recent_entry)

# Function to create a calculator button
def create_button(text, row, col, col_span=1):
    """
    Dynamically creates a button for the calculator, places it in the specified row and column,
    and binds the button click event to the on_button_click function.
    """
    # Create a button with specific text, font, and style
    button = tk.Button(root, text=text, font=("Helvetica", 18), bd=5, bg='lightblue', fg='black')
    # Place the button in the grid layout at the specified row, column, and column span
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, sticky="nsew")
    # Bind the button click event to on_button_click function
    button.bind("<Button-1>", on_button_click)

# Setting up the main calculator window
root = tk.Tk()
root.title("Unique Calculator")  # Set the window title
root.geometry("320x450")  # Set the window size
root.configure(bg='lightgrey')  # Set background color

# Configure the grid layout to make it responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Entry field for displaying the current arithmetic expression
entry = tk.Entry(root, font=("Helvetica", 24), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Entry field for displaying recent calculation history
entry_history = tk.Entry(root, font=("Helvetica", 14), bd=3, justify=tk.RIGHT)
entry_history.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
# Initialize history with 'None' since there's no calculation yet
entry_history.insert(tk.END, "History: None")

# Create calculator buttons and arrange them in the grid
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),  # Row 2: Digits 7-9 and Divide button
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),  # Row 3: Digits 4-6 and Multiply button
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),  # Row 4: Digits 1-3 and Subtract button
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),  # Row 5: Digit 0, Decimal, Equals, and Add button
    ("C", 6, 0, 4)  # Row 6: Clear button spanning all columns
]

# Loop through the buttons list to create each button dynamically
for (text, row, col, *col_span) in buttons:
    create_button(text, row, col, *col_span)

# Start the main event loop to keep the application running
root.mainloop()
