from tkinter import*
from tkinter import ttk
import ttkwidgets as tkk 


t = """
############################################
Microsoft window users                     
version 2021.1(OS built).
🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂

© Microsoft Corporation.

All rights and copyrights are reserved.    
The Windows 10 pro user use this software. 
It is simple text writing(must be inculude 
many other function)operating system.      
                                           
############################################
                                           
Crated by MOHIT SAINI.


Window User
############################################
"""
def window_for_help(window):
    top = Toplevel()
    top.lift()
    top.focus_force()
    top.transient(window)
    style = ttk.Style() 
    style.configure('TButton', font =
			('Arial', 8, 'bold'), 
					borderwidth = '4') 


    style.map('TButton',background = [('focus', 'light blue')]) 
    top.title("About Textpad")
    top.resizable(0,0)
    im = PhotoImage(file = "")
    l = ttk.Label(top,text = t)
    l.pack()
    
    li = tkk.LinkLabel(top,text = "MicroSoft")
    li.pack()
    b = ttk.Button(top,text = "Ok",command = top.destroy)
    b.pack(pady = 10)
    b.focus_force()
    
