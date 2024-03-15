import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Frame Example")

# Create a frame
frame = tk.Frame(root, bg="lightblue", padx=100, pady=100)
frame.pack()

# Create labels and buttons within the frame
label = tk.Label(frame, text="This is a frame!", font=("Helvetica", 16))
label.pack()

button = tk.Button(frame, text="Click Me", padx=10, pady=5)
button.pack()

# Run the main event loop
root.mainloop()
