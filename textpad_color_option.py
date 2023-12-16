from tkinter import *
from tkinter import colorchooser
exit_app = False
def text_color(my_text,):
    global exit_app
    exit_app = False
    my_color=colorchooser.askcolor(title="Selected text colour")[1]
    if my_color:
        color_font = font.Font(my_text,my_text.cget("font"))

        my_text.tag_configure("colored",font=color_font,foreground = my_color)
        current_tag = my_text.tag_names("sel.first")
        if "colored" in current_tag:
            my_text.tag_remove("colored","sel.first","sel.last")

        else:
            my_text.tag_add("colored","sel.first","sel.last")

def bg_color(my_text):
    global exit_app
    exit_app = False
    my_color=colorchooser.askcolor(title="Background colour")[1]
    if my_color:
        my_text.config(bg=my_color)

def all_text_color(my_text):
    global exit_app
    exit_app = False
    my_color=colorchooser.askcolor(title="All text colour")[1]
    if my_color:
        my_text.config(fg=my_color)
