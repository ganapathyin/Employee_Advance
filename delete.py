#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 12, 2020 05:19:56 PM IST  platform: Windows NT

import sys
from tkcalendar import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import delete_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    delete_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    delete_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 13 -weight bold"
        font14 = "-family {Segoe UI} -size 12"
        font15 = "-family {Arial} -size 14"
        font16 = "-family {Segoe UI Semibold} -size 12 -weight bold"
        font9 = "-family {Segoe UI Black} -size 20 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("986x642")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("VSA")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.304, rely=0.016, height=61, width=363)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Delete Stored Data''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.041, rely=0.125, relheight=0.366
                , relwidth=0.919)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.011, rely=0.043, height=31, width=224)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Delete BioData By Name''')

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.488, rely=0.077, relheight=0.847)
        self.TSeparator1.configure(orient="vertical")

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.497, rely=0.043, height=31, width=224)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Segoe UI} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Delete Advance By Name''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.011, rely=0.213, height=31, width=134)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Enter The Name''')

        self.Label3_3 = tk.Label(self.Frame1)
        self.Label3_3.place(relx=0.519, rely=0.213, height=31, width=134)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#d9d9d9")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(font="-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Enter The Name''')

        self.name_1 = tk.Entry(self.Frame1)
        self.name_1.place(relx=0.099, rely=0.383,height=40, relwidth=0.302)
        self.name_1.configure(background="white")
        self.name_1.configure(disabledforeground="#a3a3a3")
        self.name_1.configure(font=font15)
        self.name_1.configure(foreground="#000000")
        self.name_1.configure(insertbackground="black")

        self.name_2 = tk.Entry(self.Frame1)
        self.name_2.place(relx=0.618, rely=0.383,height=40, relwidth=0.302)
        self.name_2.configure(background="white")
        self.name_2.configure(disabledforeground="#a3a3a3")
        self.name_2.configure(font="-family Arial -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.name_2.configure(foreground="#000000")
        self.name_2.configure(highlightbackground="#d9d9d9")
        self.name_2.configure(highlightcolor="black")
        self.name_2.configure(insertbackground="black")
        self.name_2.configure(selectbackground="blue")
        self.name_2.configure(selectforeground="white")

        self.Delete_1 = tk.Button(self.Frame1)
        self.Delete_1.place(relx=0.155, rely=0.681, height=44, width=97)
        self.Delete_1.configure(activebackground="#ececec")
        self.Delete_1.configure(activeforeground="#000000")
        self.Delete_1.configure(background="#d9d9d9")
        self.Delete_1.configure(disabledforeground="#a3a3a3")
        self.Delete_1.configure(foreground="#000000")
        self.Delete_1.configure(highlightbackground="#d9d9d9")
        self.Delete_1.configure(highlightcolor="black")
        self.Delete_1.configure(pady="0")
        self.Delete_1.configure(text='''Delete''')
        self.Delete_1.bind('<Button-1>',lambda e:delete_support.delete1(e))

        self.Delete_2 = tk.Button(self.Frame1)
        self.Delete_2.place(relx=0.717, rely=0.638, height=44, width=97)
        self.Delete_2.configure(activebackground="#ececec")
        self.Delete_2.configure(activeforeground="#000000")
        self.Delete_2.configure(background="#d9d9d9")
        self.Delete_2.configure(disabledforeground="#a3a3a3")
        self.Delete_2.configure(foreground="#000000")
        self.Delete_2.configure(highlightbackground="#d9d9d9")
        self.Delete_2.configure(highlightcolor="black")
        self.Delete_2.configure(pady="0")
        self.Delete_2.configure(text='''Delete''')
        self.Delete_2.bind('<Button-1>',lambda e:delete_support.delete2(e))

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.041, rely=0.514, relheight=0.428
                , relwidth=0.922)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")

        self.Label2_2 = tk.Label(self.Frame2)
        self.Label2_2.place(relx=0.011, rely=0.036, height=31, width=305)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font="-family {Segoe UI} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Delete Advance By Name with Date''')

        self.Label3_4 = tk.Label(self.Frame2)
        self.Label3_4.place(relx=0.033, rely=0.182, height=31, width=134)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label3_4.configure(foreground="#000000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Enter The Name''')

        self.name_3 = tk.Entry(self.Frame2)
        self.name_3.place(relx=0.099, rely=0.327,height=40, relwidth=0.301)
        self.name_3.configure(background="white")
        self.name_3.configure(disabledforeground="#a3a3a3")
        self.name_3.configure(font="-family Arial -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.name_3.configure(foreground="#000000")
        self.name_3.configure(highlightbackground="#d9d9d9")
        self.name_3.configure(highlightcolor="black")
        self.name_3.configure(insertbackground="black")
        self.name_3.configure(selectbackground="blue")
        self.name_3.configure(selectforeground="white")

        self.Cal = Calendar(self.Frame2, selectmode = "day",date_pattern ="y-mm-dd")
        self.Cal.place(relx=0.517, rely=0.109, relheight=0.818, relwidth=0.314)

        self.select = tk.Button(self.Frame2)
        self.select.place(relx=0.88, rely=0.436, height=34, width=67)
        self.select.configure(activebackground="#ececec")
        self.select.configure(activeforeground="#000000")
        self.select.configure(background="#d9d9d9")
        self.select.configure(disabledforeground="#a3a3a3")
        self.select.configure(foreground="#000000")
        self.select.configure(highlightbackground="#d9d9d9")
        self.select.configure(highlightcolor="black")
        self.select.configure(pady="0")
        self.select.configure(text='''Select''')
        self.select.bind('<Button-1>',lambda e:delete_support.select(e))

        self.Delete_3 = tk.Button(self.Frame2)
        self.Delete_3.place(relx=0.308, rely=0.727, height=44, width=97)
        self.Delete_3.configure(activebackground="#ececec")
        self.Delete_3.configure(activeforeground="#000000")
        self.Delete_3.configure(background="#d9d9d9")
        self.Delete_3.configure(disabledforeground="#a3a3a3")
        self.Delete_3.configure(foreground="#000000")
        self.Delete_3.configure(highlightbackground="#d9d9d9")
        self.Delete_3.configure(highlightcolor="black")
        self.Delete_3.configure(pady="0")
        self.Delete_3.configure(text='''Delete''')
        self.Delete_3.bind('<Button-1>',lambda e:delete_support.delete3(e))
        

        self.menu = tk.Button(self.Frame2)
        self.menu.place(relx=0.913, rely=0.8, height=34, width=56)
        self.menu.configure(activebackground="#ececec")
        self.menu.configure(activeforeground="#000000")
        self.menu.configure(background="#d9d9d9")
        self.menu.configure(disabledforeground="#a3a3a3")
        self.menu.configure(foreground="#000000")
        self.menu.configure(highlightbackground="#d9d9d9")
        self.menu.configure(highlightcolor="black")
        self.menu.configure(pady="0")
        self.menu.configure(text='''back''')
        self.menu.bind('<Button-1>',lambda e:delete_support.menu(e))

        self.date = tk.Label(self.Frame2)
        self.date.place(relx=0.858, rely=0.182, height=41, width=114)
        self.date.configure(background="#ffffff")
        self.date.configure(disabledforeground="#a3a3a3")
        self.date.configure(font=font16)
        self.date.configure(foreground="#000000")
        self.date.configure(relief="raised")

if __name__ == '__main__':
    vp_start_gui()





