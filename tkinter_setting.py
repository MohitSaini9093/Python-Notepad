"""
install tkinter and ttk lastest version.


"""
from tkinter import *
from tkinter import ttk



def window1(window,text_f):
    top = Toplevel()
    top.lift()
    top.focus_force()
    top.transient(window)
    top.title('SETTING')
    note = ttk.Notebook(top)
    fr = ttk.Frame(top)
    fr.pack()
    note.add(fr,text = 'BordarType')
    note.pack(fill = 'both',expand = 1)
    L = ttk.Label(fr,text = 'BORDAR SETTING',font = ('Arial',15,'bold'))
    L.pack(padx = 10,pady = 10)

    L1 = ttk.Label(fr,text = 'BORDAR TYPE',)
    L1.pack(padx = 10,pady = 10)
    f = ttk.Combobox(fr,value = ['sunken','raised','flat','groove','ridge','solid'])
    f.current(0)
    f.pack(padx = 10,pady = 10)

    L2 = ttk.Label(fr,text = 'BORDAR WIDTH',)
    L2.pack(padx = 10,pady = 10)
    s = ttk.Spinbox(fr,value = [1,2,3,4,5,6])
    #s.current(0)
    s.pack()
    
    
    def bordar():
        try:
            text_f.config(relief = f.get(),bd = s.get())
        except:
            pass
    b = ttk.Button(fr,text = 'ok',command = bordar)
    b.pack()



    
    
    
