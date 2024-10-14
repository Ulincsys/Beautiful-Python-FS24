from tkinter import Tk, Label, Button

# Create a new window
window = Tk()

# Give it a title and size
window.title("Hello Python!")
window.geometry("400x400")

# Set a minimum size of 150x100
window.minsize(150, 100)
# Otherwise you can squeeze the window invisible!

# Create our Hello world label
l1 = Label(window, text="Hello, world!")
# Tell the label to fill all empty space, and center itself
l1.pack(expand=True, fill="both", anchor="center")

# Create a close button
b1 = Button(window, text="close", command=window.destroy)
# Stick the button to the "se" (READ: bottom-right) corner
b1.pack(side="bottom", anchor="se", padx=10, pady=10)

# Pause for the window to close
window.mainloop()
