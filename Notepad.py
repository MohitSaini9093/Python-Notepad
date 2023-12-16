#my_text
import Notepad as no
from tkinter import*

from tkinter import font
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk
import wikipedia
from tkinter import messagebox
import sys
#import win32print
#import win32api
from datetime import date,datetime
import os
from time import strftime 
import time
import Pmw
import tkinter_setting
import textpad_color_option as tco

import textpad_about as ab
def main(root):
    #root = Toplevel(root)
    now = datetime.now()
    today = date.today()
    root.state('zoomed')
    meaa = Pmw.Balloon(root)
    #--icon
    help_img = PhotoImage(file ="icon_of_textpad/info.png")
    repl_img = PhotoImage(file="icon_of_textpad/loop.png")
    settingtr = PhotoImage(file="icon_of_textpad/settings.png")
    new_wg = PhotoImage(file="icon_of_textpad/new_w.png")
    new_img = PhotoImage(file="icon_of_textpad/009-add.png")
    copy_img = PhotoImage(file="icon_of_textpad/010-copy.png")
    paste_img = PhotoImage(file="icon_of_textpad/001-paste.png")
    clear_img = PhotoImage(file="icon_of_textpad/001-clear.png")
    undo_img = PhotoImage(file="icon_of_textpad/002-undo.png")
    redo_img = PhotoImage(file="icon_of_textpad/003-redo.png")
    open_img = PhotoImage(file="icon_of_textpad/004-folder.png")
    folder1_img = PhotoImage(file="icon_of_textpad/005-folder-1.png")
    save_img = PhotoImage(file="icon_of_textpad/006-save-file.png")
    print_img = PhotoImage(file="icon_of_textpad/007-printer.png")
    exit_img = PhotoImage(file="icon_of_textpad/008-exit.png")
    cut_img = PhotoImage(file="icon_of_textpad/cut.png")
    search_img = PhotoImage(file="icon_of_textpad/search.png")
    clock_img = PhotoImage(file="icon_of_textpad/clock.png")
    calendar_img = PhotoImage(file="icon_of_textpad/calendar.png")
    selection_img = PhotoImage(file="icon_of_textpad/selection.png")
    night_img = PhotoImage(file="icon_of_textpad/001-night.png")
    light_img = PhotoImage(file="icon_of_textpad/002-brightness.png")
    person_img = PhotoImage(file="icon_of_textpad/person.png")
    text_img = PhotoImage(file="icon_of_textpad/text.png")
    bold_img = PhotoImage(file="icon_of_textpad/bold.png")
    italic_img = PhotoImage(file="icon_of_textpad/italic.png")
    back_img = PhotoImage(file="icon_of_textpad/003-theme.png")
    font_img=PhotoImage(file="icon_of_textpad/typography.png")

    center_text=PhotoImage(file="icon_of_textpad/center-alignment-button.png")
    left_center=PhotoImage(file="icon_of_textpad/left-align.png")
    right_text=PhotoImage(file="icon_of_textpad/right-align.png")

    underline_img=PhotoImage(file="icon_of_textpad/001-underline.png")
    strick_img=PhotoImage(file="icon_of_textpad/002-strikethrough-text-interface-sign.png")

    wikiicon = PhotoImage(file="icon_of_textpad/011-wikipedia.png")
    icon = PhotoImage(file="icon_of_textpad/001-notes.png")
    wiki = PhotoImage(file="icon_of_textpad/001-wikipedia.png")



    #--global variable
    global open_file_name 
    open_file_name = None#variable for save file
    global font_f

    global selected
    selected = False#variable for selected text
    global highlight_color
    highlight_color ='ivory2'#variable for highloght colour
    global exit_app
    exit_app = True#for exit window
    root.iconphoto(False,icon)
    root.title("New File - Textpad!")
    style = ttk.Style(root)
    #font format
    my_family = "System"
    size = "8"
    style = "normal"

    def new_w(event = False):
        ro = Toplevel(root)
        no.main(ro)
    def new_file(event = False):
        global exit_app
        exit_app = True
        my_text.delete(1.0,END)
        root.title('New File - Notepad')
    def open_file(event = False):
        global font_f
        
        text_file = filedialog.askopenfilename(initialdir=".txt",title="Open File",filetypes=(("text files","*.txt"),("HTML files","*.html"),("Python files","*.py"),("All files","*.*")))
        if text_file:
            global open_file_name
            open_file_name = text_file
            name = text_file
            root.title(os.path.basename(name))#change title to open file name
            text_file = open(text_file,'r')#create filevariable
            Intext = text_file.read()
            my_text.delete(1.0,END)
            my_text.insert(END,Intext)
            my_text.tag_add('linespace','1.0',END)
            my_text.tag_configure('linespace',font = font_f)
            #my_text.tag_remove('OPEN','1.0',END)
            global exit_app
            exit_app = True   
            text_file.close()
            
        else:
            open_file_name = None

    def save_as_file(event=False):
        text_file = filedialog.asksaveasfilename(defaultextension="*.txt",initialdir=".txt",title="Save as file",filetypes=(("text files","*.txt"),("HTML files","*.html"),("Python files","*.py"),("All files","*.*")))
        if text_file:
            name = text_file
            root.title(f'{os.path.basename(name)} - textpad!')
            text_file = open(text_file,'w')
            text_file.write(my_text.get(1.0,END))
            global open_file_name
            open_status_name = text_file
            global exit_app
            exit_app = True
            text_file.close()
    def save_file(event = False):
        global open_file_name
        if open_file_name is not None:
            text_file = open(open_file_name,'w')
            text_file.write(my_text.get(1.0,END))
            global exit_app
            exit_app = True
            text_file.close()
            status_bar.config(text=f'{os.path.basename(open_file_name)}   ')
        else:
            save_as_file()

    def cut_text(e):
        try:
            global selected
            global exit_app
            exit_app = False
            if e:
                selected = root.clipboard_get()
                
            else:
                if my_text.selection_get():
                    selected = my_text.selection_get()
                    my_text.delete("sel.first","sel.last")
                    
                    my_text.tag_add('linespace','1.0',END)
                    my_text.tag_configure('linespace',font = font_f)
                    root.clipboard_clear()
                    root.clipboard_append(selected)
        except:
            pass
    def copy_text(e):
        try:
            global selected
            if e:
                selected = root.clipboard_get()
                
            if my_text.selection_get():
                selected = my_text.selection_get()
                
                root.clipboard_clear()
                root.clipboard_append(selected)
        except:
            pass

    def paste_text(e):
        try:
            global selected
            global exit_app
            exit_app = False
            if e:
                selected = root.clipboard_get()
                
            else:
                if selected:
                    position = my_text.index(INSERT)

                    my_text.insert(position,selected)
                    my_text.tag_add('linespace','1.0',END)
                    my_text.tag_configure('linespace',font = font_f)
                    
        except:
            pass

    def nowdate():
        nowd = today.strftime("%m/%d/%y")
        position = my_text.index(INSERT)
        my_text.insert(position,nowd)
        my_text.tag_add('linespace','1.0',END)
        my_text.tag_configure('linespace',font = font_f)
        global exit_app
        exit_app = False

    def time1():
        string = strftime('%H:%M:%S %p')     
        position = my_text.index(INSERT)
        my_text.insert(position,string)
        my_text.tag_add('linespace','1.0',END)
        my_text.tag_configure('linespace',font = font_f)
        global exit_app
        exit_app = False
    def bold_it():
        global exit_app
        exit_app = False
        global font_f
        global t_bold
        t_bold=bold_button.cget("bg")
        if t_bold == "light blue":
            try:
                bold_font1 = font.Font(my_text,my_text.cget("font"))
                bold_font1.configure(weight="bold")
                my_text.tag_configure("bold",font=bold_font1)
                current_tag = my_text.tag_names("sel.first")
                
                if "bold" in current_tag:
                    my_text.tag_remove("bold","sel.first","sel.last")

                else:
                    my_text.tag_add("bold","sel.first","sel.last")
            except:
                font_f.configure(weight="normal")
                my_text.tag_configure('linespace',font = font_f)
                bold_button.config(bg = "SystemButtonFace")
        elif t_bold!= "light blue":
            
            
            try:
                bold_font = font.Font(my_text,my_text.cget("font"))
                bold_font.configure(weight="bold")
                my_text.tag_configure("bold",font=bold_font)
                current_tag = my_text.tag_names("sel.first")
                
                if "bold" in current_tag:
                    my_text.tag_remove("bold","sel.first","sel.last")

                else:
                    my_text.tag_add("bold","sel.first","sel.last")
            except:
                font_f.configure(weight="bold")
                my_text.tag_configure('linespace',font = font_f)
                bold_button.config(bg = "light blue")
    def ita_it():
        global exit_app
        exit_app = False
        global ita_font1
        global t_ita
        global font_f
        t_ita=ita_button.cget("bg")
        if t_ita == "light blue":
            try:
                ita_font = font.Font(my_text,my_text.cget("font"))
                ita_font.configure(slant="italic")
                my_text.tag_configure("italic",font=ita_font)
                current_tag = my_text.tag_names("sel.first")
                if "italic" in current_tag:
                    my_text.tag_remove("italic","sel.first","sel.last")

                else:
                    my_text.tag_add("italic","sel.first","sel.last")
            except:
                font_f.configure(slant="roman")
                my_text.tag_configure('linespace',font = font_f)
                ita_button.config(bg = "SystemButtonFace")
        elif t_ita!= "light blue":
            
            
            try:
                bold_font = font.Font(my_text,my_text.cget("font"))
                bold_font.configure(slant="italic")
                my_text.tag_configure("italic",font=ita_font)
                current_tag = my_text.tag_names("sel.first")
                if "italic" in current_tag:
                    my_text.tag_remove("italic","sel.first","sel.last")

                else:
                    my_text.tag_add("italic","sel.first","sel.last")
            except:
                font_f.configure(slant="italic")
                my_text.tag_configure('linespace',font = font_f)
                ita_button.config(bg = "light blue")
    #underline            
    def underline_it():
        global exit_app
        exit_app = False
        global under_line
        global font_f
        global t_und
        t_und=under_button.cget("bg")
        if t_und == "light blue":
            
            
            try:
                under_line = font.Font(my_text,my_text.cget("font"))
                under_line.configure(underline="false")
                my_text.tag_configure("underline",font=under_line)
                current_tag = my_text.tag_names("sel.first")
                if "underline" in current_tag:
                    my_text.tag_remove("underline","sel.first","sel.last")

                else:
                    my_text.tag_add("underline","sel.first","sel.last")
            except:
                font_f.configure(underline="false")
                my_text.tag_configure('linespace',font = font_f)
                under_button.config(bg = "SystemButtonFace")
        elif t_und!= "light blue":
            
            
            try:
                under_line = font.Font(my_text,my_text.cget("font"))
                under_line.configure(underline="true")
                my_text.tag_configure("underline",font=under_line)
                current_tag = my_text.tag_names("sel.first")
                if "underline" in current_tag:
                    my_text.tag_remove("underline","sel.first","sel.last")

                else:
                    my_text.tag_add("underline","sel.first","sel.last")
            except:
                font_f.configure(underline="true")
                my_text.tag_configure('linespace',font = font_f)
                under_button.config(bg = "light blue")
    #overstrik
    def overstrike_it():
        global exit_app
        exit_app = False
        global font_f
        global under_line
        global t_overstrike
        t_overstrike=overstrike_button.cget("bg")
        if t_overstrike == "light blue":
            
            try:
                overstrike_line = font.Font(my_text,my_text.cget("font"))
                overstrike_line.configure(overstrike="false")
                my_text.tag_configure("overstrike",font=overstrike_line)
                current_tag = my_text.tag_names("sel.first")
                if "overstrike" in current_tag:
                    my_text.tag_remove("overstrike","sel.first","sel.last")

                else:
                    my_text.tag_add("overstrike","sel.first","sel.last")
            except:
                font_f.configure(overstrike="false")
                my_text.tag_configure('linespace',font = font_f)
                overstrike_button.config(bg = "SystemButtonFace")
        elif t_overstrike!= "light blue":
            try:
                overstrike_line = font.Font(my_text,my_text.cget("font"))
                overstrike_line.configure(overstrike="true")
                my_text.tag_configure("overstrike",font=overstrike_line)
                current_tag = my_text.tag_names("sel.first")
                if "overstrike" in current_tag:
                    my_text.tag_remove("overstrike","sel.first","sel.last")

                else:
                    my_text.tag_add("overstrike","sel.first","sel.last")
            except:
                font_f.configure(overstrike="true")
                my_text.tag_configure('linespace',font = font_f)
                overstrike_button.config(bg = "light blue")            
    def text_color():
        tco.text_color(my_text)

    def bg_color():
        tco.bg_color(my_text)

    def all_text_color():
        tco.all_text_color(my_text)

    def print_file():
        #printer_name = win32print.GetDefaultPrinter()

        file_t_print = filedialog.askopenfilename(initialdir=".txt",title="Open File",filetypes=(("text files","*.txt"),("HTML files","*.html"),("Python files","*.py"),("All files","*.*")))
        if file_t_print:
            win32api.ShellExecute(0,"print",file_t_print,None,".",0)
    def select_all():
        my_text.tag_add('sel','1.0','end')

    def clear_all(e =False):
        global exit_app
        exit_app = False
        my_text.delete(1.0,END)

    def night_on():
        main_color = "#000000"
        second_color = "#373737"
        text_color = "white"
        root.config(bg= main_color)
        status_bar.config(bg=main_color,fg = text_color)
        my_text.config(bg=second_color)
        toolbar_frame.config(bg=main_color)
        bold_button.config(bg=second_color)
        ita_button.config(bg=second_color)
        undo_button.config(bg=second_color)
        redo_button.config(bg=second_color)
        #color_text_button.config(bg=second_color)
        file_menu.config(bg=main_color,fg=text_color)
        edit_menu.config(bg=main_color,fg=text_color)
        color_menu.config(bg=main_color,fg=text_color)
        option_menu.config(bg=main_color,fg=text_color)
        format_menu.config(bg=main_color,fg=text_color)
        view_menu.config(bg=main_color,fg=text_color)
        search_menu.config(bg=main_color,fg=text_color)
        my_eM.config(bg=main_color,fg=text_color)
        center.config(bg=second_color)
        left.config(bg=second_color)
        right.config(bg=second_color)
        under_button.config(bg = second_color)
        overstrike_button.config(bg = second_color)
        setting.config(bg=main_color,fg=text_color)
        my_text.config(fg = "white")
    def night_off():
        main_color = "SystemButtonFace"
        second_color = "SystemButtonFace"
        text_color = "black"
        root.config(bg= main_color)
        status_bar.config(bg=main_color,fg = text_color)
        my_text.config(bg="white")
        toolbar_frame.config(bg=main_color)
        bold_button.config(bg=second_color)
        ita_button.config(bg=second_color)
        undo_button.config(bg=second_color)
        redo_button.config(bg=second_color)
        
        #color_text_button.config(bg=second_color)
        file_menu.config(bg=main_color,fg=text_color)
        edit_menu.config(bg=main_color,fg=text_color)
        color_menu.config(bg=main_color,fg=text_color)
        option_menu.config(bg=main_color,fg=text_color)
        format_menu.config(bg=main_color,fg=text_color)
        view_menu.config(bg=main_color,fg=text_color)
        search_menu.config(bg=main_color,fg=text_color)
        my_eM.config(bg=main_color,fg=text_color)
        center.config(bg=second_color)
        left.config(bg=second_color)
        right.config(bg=second_color)
        overstrike_button.config(bg = second_color)
        under_button.config(bg = second_color)
        setting.config(bg=main_color,fg=text_color)
        my_text.config(fg = "black")
    def sea():
        top = Toplevel()
        top.lift()
        top.focus_force()
        top.iconphoto(False,wiki)
        top.title("Wikipedia search")
        top.transient(root)
        #top.attributes('-toolwindow',True)
        top.geometry("350x100")
        
        l = ttk.Label(top,image = wikiicon,text="Type Here:",compound = "top")
        l.pack()
        e = ttk.Entry(top,width=50)
        e.pack()
        e.focus_set()
        def sea1():
            try:
                global exit_app
                exit_app = False
                se = wikipedia.summary(str(e.get()))
                my_text.delete(1.0,END)
                my_text.insert(END,se)
                top.destroy()

            except:
                
                exit_app = False
                messagebox.showwarning("Texpad","Check your internet connection")

            
        b = ttk.Button(top,text="OK",command=sea1)
        b.pack()

    def font_text():
        global font_f
        font_text_window = Toplevel()
        font_text_window.title("Font")
        font_text_window.transient(root)
        font_text_window.lift()
        font_text_window.focus_force()
        font_text_window.iconphoto(False,font_img)
        font_text_windowlabel = ttk.Label(font_text_window,text ="Font:" )
        font_text_windowlabel.grid(row = 0,column = 1,pady = 10,padx = 10 )
        fonts=list(font.families())
        fonts.sort()
        font_text_window_cfo = ttk.Combobox(font_text_window,values = fonts)
        font_text_window_cfo.current(0)
        font_text_window_cfo.grid(row = 1,column = 1)
        
        font_text_windowlabel = ttk.Label(font_text_window,text ="Font Size:" )
        font_text_windowlabel.grid(row = 0,column = 3,pady = 10,padx = 10 )
        sizefonts= ["8","9","10","11","12","14","16","18","20","22","24","26","28","36","48","72"]
        font_text_window_csi = ttk.Combobox(font_text_window,values = sizefonts)
        font_text_window_csi.grid(row = 1,column = 3)
        font_text_window_csi.current(0)
        

        def samplefont_text_window_frame(e = False):
            font_text_window_frame_label.config(font = (font_text_window_cfo.get(),font_text_window_csi.get()))
            font_text_window_cfo.config(font = (font_text_window_cfo.get(),"8"))
            
        font_text_window_frame = LabelFrame(font_text_window,text = "Sample",padx = 50,pady = 50)
        font_text_window_frame.grid(row=5,column = 1,pady = 10,columnspan =3)
        font_text_window_frame_label = ttk.Label(font_text_window_frame,text = "abcdef")
        font_text_window_frame_label.pack(padx = 25,pady=25)
        font_text_window_cfo.bind('<<ComboboxSelected>>',samplefont_text_window_frame )
        font_text_window_csi.bind('<<ComboboxSelected>>',samplefont_text_window_frame )
        my_text.tag_add('linespace1',"current")
        def font_select():
            
            global font_f
            font_f.configure(family=font_text_window_cfo.get(),size =font_text_window_csi.get() )
            my_text.tag_configure('linespace1',font = font_f)
            my_text.tag_configure('linespace',font = font_f)
            my_family = font_text_window_cfo.get()
            size = font_text_window_csi.get()
                
            global exit_app
            exit_app = False
            update_cursor_info_bar()
            show_cursor_info_bar()
            font_text_window.destroy()
        b_font_text_window =ttk.Button(font_text_window,text = "Ok",command = font_select)
        b_font_text_window.grid(row = 5,column = 5)



    def wrap_text():
        if var.get() == True:
            my_text.config(wrap = "word")
            hor_scroll.pack_forget()
            
            
        elif var.get() == False:
            my_text.config(wrap = "none")
        
            hor_scroll.pack(side=BOTTOM,fill=X)
            my_text.config(xscrollcommand = hor_scroll.set)
        else:
            pass
                   


    #--fint
    def find_text(event=None):
        search_toplevel = Toplevel()
        search_toplevel.title('Find Text')
        search_toplevel.transient(root)
        search_toplevel.iconphoto(False,search_img)
        search_toplevel.lift()
        search_toplevel.focus_force()
        ttk.Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')

        search_entry_widget = ttk.Entry(search_toplevel, width=25)
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        search_entry_widget.focus_set()
        ignore_case_value = IntVar()
        ttk.Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(
            row=1, column=1, sticky='e', padx=2, pady=2)
        ttk.Button(search_toplevel, text="Find All", underline=0,
               command=lambda: search_output(
                   search_entry_widget.get(), ignore_case_value.get(),
                   my_text, search_toplevel, search_entry_widget)
               ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

        def close_search_window():
            my_text.tag_remove('match', '1.0', END)
            search_toplevel.destroy()
            
        search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
        return "break"


    def search_output(needle, if_ignore_case, my_text,
                      search_toplevel, search_box):
        
        my_text.tag_remove('match', '1.0', END)
        matches_found = 0
        
        if needle:
            start_pos = '1.0'
            while True:
                start_pos = my_text.search(needle, start_pos,
                                                nocase=if_ignore_case, stopindex=END)
                
                if not start_pos:
                    break
                end_pos = '{}+{}c'.format(start_pos, len(needle))
                
                
                my_text.tag_add('match', start_pos, end_pos)
                matches_found += 1
                start_pos = end_pos
            my_text.tag_config(
                'match', foreground='red', background='yellow')
        search_box.focus_set()
        search_toplevel.title('{} matches found'.format(matches_found))
    #stauts
    def show_cursor_info_bar():
        show_cursor_info_checked = show_cursor_info.get()
        if show_cursor_info_checked:
            status_bar.pack(fill=X,side=BOTTOM)
        else:
            status_bar.pack_forget()


    def update_cursor_info_bar():
        row, col = my_text.index(INSERT).split('.')
        line_num, col_num = str(int(row)), str(int(col)+1)
        infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
        status_bar.config(text=infotext)
        root.after(100,update_cursor_info_bar)

    def highlight_line():
        my_text.tag_remove("active_line", 1.0, "end")
        my_text.tag_add(
            "active_line", "insert linestart", "insert lineend+1c")
        root.after(100, toggle_highlight)
    def undo_highlight():
        my_text.tag_remove("active_line", 1.0, "end")
    def toggle_highlight():

        if to_highlight_line.get():
            highlight_line()
        else:
            undo_highlight()
    def exitt(e = False):
        global exit_app
        if exit_app is not True:
            response = messagebox.askyesnocancel("Texpad","Do you want to save?",icon = "warning",default = "yes")
            if response==1:
                save_file()
            if response==0:
                root.destroy()
        if exit_app == True:
            response = messagebox.askquestion("Texpad","Do you want to exit")
            if response =="yes":
                root.destroy()
    def align(align):
        align1 = align
        if align == "left":
            my_text.tag_configure("center", justify=align)
            my_text.tag_add("center", 1.0, "end")
            center.config(bg = "SystemButtonFace")
            right.config(bg = "SystemButtonFace")
            left.config(bg = "light blue")
        if align == "right":
            my_text.tag_configure("center", justify=align)
            my_text.tag_add("center", 1.0, "end")
            center.config(bg = "SystemButtonFace")
            right.config(bg = "light blue")
            left.config(bg = "SystemButtonFace")
        if align == "center":
            my_text.tag_configure("center", justify=align)
            my_text.tag_add("center", 1.0, "end")
            center.config(bg = "light blue")
            right.config(bg = "SystemButtonFace")
            left.config(bg = "SystemButtonFace")
    def sett():
        tkinter_setting.window1(root,my_text)
    def ab_h():
        ab.window_for_help(root)
    def replace_text():
        replace_window = Toplevel(root)
        replace_window.title('Replace Text')
        replace_window.transient(root)
        replace_window.iconphoto(False,search_img)
        l_h = Label(replace_window,text = "Find:")
        l_h.grid(row=0,column=0,sticky="w")
        e_h = ttk.Entry(replace_window)
        e_h.grid(row = 0,column=1,padx = 10,pady=10)
        
        l_h1 = Label(replace_window,text = "Find:")
        l_h1.grid(row=1,column=0,sticky="w")
        e_h1 = ttk.Entry(replace_window)
        e_h1.grid(row = 1,column=1,padx = 10)
        def repl():
            replace_text=my_text.get(1.0,END)
            replace_text = replace_text.replace(e_h.get(),e_h1.get())
            my_text.delete(1.0,END)
            my_text.insert(1.0,replace_text)
            
        b_h = ttk.Button(replace_window,text = "Replace all",command = repl)
        b_h.grid(row = 2,column=1,columnspan=2)
        
        
        
    toolbar_frame = Frame(root,width = 600,height=400,relief = 'sunken',bd = 2)
    toolbar_frame.pack(fill=X)
    my_frame = Frame(root)
    my_frame.pack(pady=5,fill =BOTH,expand = 2)


    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT,fill=Y)



    hor_scroll = Scrollbar(my_frame,orient=HORIZONTAL)
    hor_scroll.pack(side=BOTTOM,fill=X)
    my_text = Text(my_frame,insertbackground = "blue",selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set,wrap=WORD,cursor = "xterm")
    my_text.pack(fill = BOTH,expand =2)
    my_text.tag_add("linespace","1.0","end")
    text_scroll.config(command = my_text.yview)
    hor_scroll.config(command = my_text.xview)
    my_menu = Menu(root)
    my_text.focus_set()
    root.config(menu=my_menu)
    file_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="New Window",command=new_w,accelerator = "Ctrl+Shift+N",image = new_wg,compound = "left")
    file_menu.add_command(label="New",command=new_file,accelerator = "Ctrl+N",image = new_img,compound = "left")
    file_menu.add_command(label="Open",command=open_file,accelerator = "Ctrl+O",image = open_img,compound = "left")
    file_menu.add_command(label="Save",command=save_file,accelerator = "Ctrl+S",image = save_img,compound = "left")
    file_menu.add_command(label="Save as",command=save_as_file,accelerator = "Shift+Ctrl+S",image = folder1_img,compound = "left")
    file_menu.add_separator()
    file_menu.add_command(label="Print file",command=print_file,accelerator = "Ctrl+P",image = print_img,compound = "left")

    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=exitt,accelerator = "Ctrl+E",image = exit_img,compound = "left")
    edit_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Cut",command=lambda:cut_text(False),accelerator = "Ctrl+X",image = cut_img,compound = "left")
    edit_menu.add_command(label="Copy",command=lambda:copy_text(False),accelerator = "Ctrl+C",image = copy_img,compound = "left")
    edit_menu.add_command(label="Paste",command=lambda:paste_text(False),accelerator = "Ctrl+V",image = paste_img,compound = "left")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo",command = my_text.edit_undo,accelerator = "Ctrl+Z",image = undo_img,compound = "left")
    edit_menu.add_command(label="Redo",command = my_text.edit_redo,accelerator = "Shief+Ctrl+Z",image = redo_img,compound = "left")
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All",command = select_all,accelerator = "Ctrl+A",image = selection_img,compound = "left")
    edit_menu.add_command(label="Clear",command = clear_all,image = clear_img,compound = "left")
    edit_menu.add_command(label="Date",command=nowdate,image = calendar_img,compound = "left")
    edit_menu.add_command(label="Time",command=time1,image = clock_img,compound = "left")
    edit_menu.add_command(label="Find",command = find_text,image = search_img,compound = "left",accelerator = "Ctrl+F")
    edit_menu.add_command(label="Replace",command = replace_text,image = repl_img,compound = "left")#accelerator = "Ctrl+F")
    
    view_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="View",menu=view_menu)

    var = BooleanVar()
    var.set(0)
    format_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="Format",menu=format_menu)
    format_menu.add_checkbutton(label="Word Wrap",variable = var,command=wrap_text)
    format_menu.add_command(label="Font",command=font_text,image = font_img,compound="left")
    
    color_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="Colors",menu=color_menu)
    color_menu.add_command(label="Slected text",command=text_color,image = text_img,compound="left")
    color_menu.add_command(label="All text color",command=all_text_color,image = text_img,compound="left")
    color_menu.add_command(label="Background ",command=bg_color,image = back_img,compound="left")

    option_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="Option",menu=option_menu)

    option_menu.add_command(label="Night mode on",command=night_on,image = night_img,compound = "left")
    option_menu.add_command(label="Night mode off",command=night_off,image = light_img,compound = "left")


    search_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="Search",menu=search_menu)
    search_menu.add_command(image  = wiki,compound = LEFT,label="Wikipedia",command=sea)
    setting = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="Setting",menu=setting)
    setting.add_command(label = "Setting",image = settingtr,command = sett,compound = "left")


    helpt = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="Help",menu=helpt)
    helpt.add_command(label = "About Textpad",image = help_img,command = ab_h,compound = 'left')

        

    my_text.tag_add('linespace',"current")
    font_f = font.Font(my_text,my_text.cget("font"))
    def my_text_staus():
        lenth = len(my_text.get(1.0,END))-1
        line = int(my_text.index('end').split('.')[0]) - 1
        status_bar.config(text="line: " + str(line)+ " "+"col:  " + str(lenth))
        root.after(100,my_text_staus)

    status_bar = Label(root,anchor=E,relief = 'groove')

    show_cursor_info = IntVar()
    show_cursor_info.set(1)
    view_menu.add_checkbutton(
        label='Show Cursor Location at Bottom', variable=show_cursor_info, command=show_cursor_info_bar)
    wrap_text()
    to_highlight_line = BooleanVar()

    view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1,
                              offvalue=0, variable=to_highlight_line, command=toggle_highlight)
    update_cursor_info_bar()
    show_cursor_info_bar()

    toggle_highlight()
    my_text.tag_add("linespace","1.0","end")
    def config_text():
        global font_f
        
        my_text.tag_configure('edf',font = font_f)
        #my_text.tag_add("linetry","current")
        root.after(100,config_text)
    config_text()    
    def t_p(e = False):
        global font_f
        global exit_app
        exit_app = False
        my_text.tag_add("edf","1.0","end")
        my_text.tag_configure('linespace',font = font_f)
        
    def pop_menu(e):
        if selected ==False:
            my_eM.entryconfig("Paste",state = "disabled")
        if selected is not False:
            my_eM.entryconfig("Paste",state = "normal")
        my_eM.tk_popup(e.x_root,e.y_root)    
                          
            
        
              
    my_eM = Menu(root,tearoff = False)
    my_eM.add_command(label = "Cut",command = lambda:cut_text(False),accelerator = "Ctrl+X",image = cut_img,compound = "left")
    my_eM.add_command(label = "Copy",command = lambda:copy_text(False),accelerator = "Ctrl+C",image = copy_img,compound = "left")
    my_eM.add_command(label = "Paste",command = lambda:paste_text(False),accelerator = "Ctrl+V",image = paste_img,compound = "left")
    my_eM.add_command(label = "Select All",command = select_all,accelerator = "Ctrl+A",image = selection_img,compound = "left")
    
    my_eM.add_command(label = "Time",command = time1,image = clock_img,compound = "left")
    my_eM.add_command(label = "Date",command = nowdate,image = calendar_img,compound = "left")
    root.bind("<Button-3>",pop_menu)     
    root.bind("<Control-x>",cut_text)
    root.bind("<Control-c>",copy_text)
    root.bind("<Control-v>",paste_text)
    root.bind("<Control-s>",save_file)
    root.bind("<Control-Shift-n>",new_w)
    root.bind("<Control-Shift-N>",new_w)
    root.bind("<Control-X>",cut_text)
    root.bind("<Control-C>",copy_text)
    root.bind("<Control-V>",paste_text)
    root.bind("<Control-S>",save_file)
    root.bind("<Shift-Control-S>",save_as_file)
    root.bind("<Control-p>",print_file)
    root.bind("<Control-P>",print_file)
    root.bind("<Control-O>",open_file)
    root.bind("<Control-o>",open_file)
    root.bind("<Control-N>",new_file)
    root.bind("<Control-n>",new_file)
    root.bind("<Control-z>",lambda e:my_text.edit_undo)
    root.bind("<Control-Z>",lambda e:my_text.edit_undo)
    root.bind("<Shift-Control-Z>",lambda e:my_text.edit_redo)
    root.bind("<Shift-Control-z>",lambda e:my_text.edit_redo)
    root.bind("<Control-f>",find_text)
    root.bind("<Control-F>",find_text)
    root.bind("<Control-e>",exitt)
    root.bind("<Control-E>",exitt)
    root.bind("<Any-KeyPress>",t_p)
    root.bind("<Delete>",clear_all)

    my_text.tag_configure('active_line', background=highlight_color)


        

    bold_button= Button(toolbar_frame,image = bold_img,command =bold_it,bd=0)
    bold_button.grid(row=0,column=0,sticky=W)
    meaa.bind(bold_button,"Bold")
    ita_button= Button(toolbar_frame,image = italic_img,command =ita_it,bd=0)
    ita_button.grid(row=0,column=1)
    meaa.bind(ita_button,"Italic")
    under_button= Button(toolbar_frame,image = underline_img,command =underline_it,bd=0)
    under_button.grid(row=0,column=2)
    meaa.bind(under_button,"Underline")
    overstrike_button =Button(toolbar_frame,image = strick_img,command =overstrike_it,bd=0)
    overstrike_button.grid(row=0,column=3)
    meaa.bind(overstrike_button,"Overstrike")
    undo_button= Button(toolbar_frame,image = undo_img,command =my_text.edit_undo,bd=0)
    undo_button.grid(row=0,column=4)
    meaa.bind(undo_button,"Undo")
    redo_button= Button(toolbar_frame,image = redo_img,command =my_text.edit_redo,bd = 0)
    redo_button.grid(row=0,column=5)
    meaa.bind(redo_button,"Redo")#
    center= Button(toolbar_frame,image = center_text,command =lambda:align("center"),bd = 0)
    center.grid(row=0,column=8)
    meaa.bind(center,"Center")
    left= Button(toolbar_frame,image = left_center,command =lambda:align("left"),bd=0,bg = "lightblue")
    left.grid(row=0,column=7)
    meaa.bind(left,"Left")
    right= Button(toolbar_frame,image = right_text,command =lambda:align("right"),bd=0)
    right.grid(row=0,column=9)
    meaa.bind(right,"Right")          
    root.protocol('WM_DELETE_WINDOW',exitt)
    root.mainloop()
