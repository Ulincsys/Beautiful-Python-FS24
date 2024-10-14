from tkinter import Tk, Label, Button, Text, Frame

from projects.dadjoke_lib import get_joke

def update_joke_textbox(textbox: Text):
    # Clear the existing text in the textbox
    textbox.delete("1.0", "end")
    
    joke = get_joke()
    
    # Insert joke text from the start of the textbox
    textbox.insert("1.0", joke["joke"])
    
window = Tk()
window.minsize(400, 200)
window.title("Get Dad Jokes!")

l1 = Label(window, text="Got Joke")
l1.pack(anchor="nw")

t = Text(window, height=5, wrap="word")
t.pack(fill="x")

# You can't pack two widgets "next to" each other on the same row easily
# So we use a Frame to contain the packing for us
button_bar = Frame(window)

b1 = Button(button_bar, text="Get Joke", command=lambda: update_joke_textbox(t))
b1.pack(side="left", anchor="s", padx=10, pady=10)

b2 = Button(window, text="Close", command=window.destroy)
b2.pack(side="right", anchor="s", padx=10, pady=10)

button_bar.pack(side="bottom", anchor="s", expand=True, fill="x")

window.mainloop()
