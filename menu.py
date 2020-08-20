#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 13, 2020 10:46:41 AM IST  platform: Windows NT

import sys

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

import menu_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Menu (root)
    menu_support.init(root, top)
    root.mainloop()

w = None
def create_Menu(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Menu(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Menu (w)
    menu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Menu():
    global w
    w.destroy()
    w = None

class Menu:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("817x789")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("VSA")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.c1 = tk.Canvas(top)
        self.c1.place(relx=0.012, rely=0.203, relheight=0.787, relwidth=0.973)
        self.c1.configure(background="#ffffff")
        self.c1.configure(borderwidth="2")
        self.c1.configure(cursor="arrow")
        self.c1.configure(highlightbackground="#d9d9d9")
        self.c1.configure(highlightcolor="black")
        self.c1.configure(insertbackground="black")
        self.c1.configure(relief="ridge")
        self.c1.configure(selectbackground="blue")
        self.c1.configure(selectforeground="white")

        self.l2 = tk.Label(self.c1)
        self.l2.place(relx=0.075, rely=0.193, height=61, width=183)
        self.l2.configure(activebackground="#f9f9f9")
        self.l2.configure(activeforeground="#000000")
        self.l2.configure(background="#ffffff")
        self.l2.configure(disabledforeground="#a3a3a3")
        self.l2.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l2.configure(foreground="#000000")
        self.l2.configure(highlightbackground="#d9d9d9")
        self.l2.configure(highlightcolor="black")
        self.l2.configure(text='''Add BioDate''')

        self.l3 = tk.Label(self.c1)
        self.l3.place(relx=0.088, rely=0.403, height=61, width=184)
        self.l3.configure(activebackground="#f9f9f9")
        self.l3.configure(activeforeground="#000000")
        self.l3.configure(background="#ffffff")
        self.l3.configure(disabledforeground="#a3a3a3")
        self.l3.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l3.configure(foreground="#000000")
        self.l3.configure(highlightbackground="#d9d9d9")
        self.l3.configure(highlightcolor="black")
        self.l3.configure(text='''Add Advance''')

        self.l3_2 = tk.Label(self.c1)
        self.l3_2.place(relx=0.667, rely=0.064, height=71, width=224)
        self.l3_2.configure(activebackground="#f9f9f9")
        self.l3_2.configure(activeforeground="#000000")
        self.l3_2.configure(background="#ffffff")
        self.l3_2.configure(disabledforeground="#a3a3a3")
        self.l3_2.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l3_2.configure(foreground="#000000")
        self.l3_2.configure(highlightbackground="#d9d9d9")
        self.l3_2.configure(highlightcolor="black")
        self.l3_2.configure(text='''Print''')

        self.l3_3 = tk.Label(self.c1)
        self.l3_3.place(relx=0.101, rely=0.709, height=61, width=244)
        self.l3_3.configure(activebackground="#f9f9f9")
        self.l3_3.configure(activeforeground="#000000")
        self.l3_3.configure(background="#ffffff")
        self.l3_3.configure(disabledforeground="#a3a3a3")
        self.l3_3.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l3_3.configure(foreground="#000000")
        self.l3_3.configure(highlightbackground="#d9d9d9")
        self.l3_3.configure(highlightcolor="black")
        self.l3_3.configure(text='''View Stored Datas''')

        self.l3_4 = tk.Label(self.c1)
        self.l3_4.place(relx=0.616, rely=0.717, height=62, width=244)
        self.l3_4.configure(activebackground="#f9f9f9")
        self.l3_4.configure(activeforeground="#000000")
        self.l3_4.configure(background="#ffffff")
        self.l3_4.configure(disabledforeground="#a3a3a3")
        self.l3_4.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l3_4.configure(foreground="#000000")
        self.l3_4.configure(highlightbackground="#d9d9d9")
        self.l3_4.configure(highlightcolor="black")
        self.l3_4.configure(text='''Delete Stored Datas''')

        self.TSeparator1 = ttk.Separator(self.c1)
        self.TSeparator1.place(relx=0.628, rely=0.129, relheight=0.435)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(self.c1)
        self.TSeparator2.place(relx=0.013, rely=0.66, relwidth=0.97)

        self.bio = tk.Button(self.c1)
        self.bio.place(relx=0.352, rely=0.193, height=64, width=167)
        self.bio.configure(activebackground="#ececec")
        self.bio.configure(activeforeground="#000000")
        self.bio.configure(background="#d9d9d9")
        self.bio.configure(command=menu_support.bio)
        self.bio.configure(disabledforeground="#a3a3a3")
        self.bio.configure(foreground="#000000")
        self.bio.configure(highlightbackground="#d9d9d9")
        self.bio.configure(highlightcolor="black")
        self.bio.configure(pady="0")
        self.bio.configure(text='''Bio''')
        self.bio.bind('<Button-1>',lambda e:menu_support.bio(e))

        self.advance = tk.Button(self.c1)
        self.advance.place(relx=0.352, rely=0.403, height=64, width=167)
        self.advance.configure(activebackground="#ececec")
        self.advance.configure(activeforeground="#000000")
        self.advance.configure(background="#d9d9d9")
        self.advance.configure(disabledforeground="#a3a3a3")
        self.advance.configure(foreground="#000000")
        self.advance.configure(highlightbackground="#d9d9d9")
        self.advance.configure(highlightcolor="black")
        self.advance.configure(pady="0")
        self.advance.configure(text='''Advance''')
        self.advance.bind('<Button-1>',lambda e:menu_support.advance(e))

        self.print = tk.Button(self.c1)
        self.print.place(relx=0.704, rely=0.177, height=64, width=167)
        self.print.configure(activebackground="#ececec")
        self.print.configure(activeforeground="#000000")
        self.print.configure(background="#d9d9d9")
        self.print.configure(disabledforeground="#a3a3a3")
        self.print.configure(foreground="#000000")
        self.print.configure(highlightbackground="#d9d9d9")
        self.print.configure(highlightcolor="black")
        self.print.configure(pady="0")
        self.print.configure(text='''Print''')
        self.print.bind('<Button-1>',lambda e:menu_support.print(e))

        self.details = tk.Button(self.c1)
        self.details.place(relx=0.151, rely=0.821, height=64, width=167)
        self.details.configure(activebackground="#ececec")
        self.details.configure(activeforeground="#000000")
        self.details.configure(background="#d9d9d9")
        self.details.configure(disabledforeground="#a3a3a3")
        self.details.configure(foreground="#000000")
        self.details.configure(highlightbackground="#d9d9d9")
        self.details.configure(highlightcolor="black")
        self.details.configure(pady="0")
        self.details.configure(text='''Details''')
        self.details.bind('<Button-1>',lambda e:menu_support.details(e))

        self.delete = tk.Button(self.c1)
        self.delete.place(relx=0.667, rely=0.821, height=64, width=167)
        self.delete.configure(activebackground="#ececec")
        self.delete.configure(activeforeground="#000000")
        self.delete.configure(background="#d9d9d9")
        self.delete.configure(disabledforeground="#a3a3a3")
        self.delete.configure(foreground="#000000")
        self.delete.configure(highlightbackground="#d9d9d9")
        self.delete.configure(highlightcolor="black")
        self.delete.configure(pady="0")
        self.delete.configure(text='''Delete''')
        self.delete.bind('<Button-1>',lambda e:menu_support.delete(e))

        self.l3_1 = tk.Label(self.c1)
        self.l3_1.place(relx=0.667, rely=0.338, height=71, width=224)
        self.l3_1.configure(activebackground="#f9f9f9")
        self.l3_1.configure(activeforeground="#000000")
        self.l3_1.configure(background="#ffffff")
        self.l3_1.configure(disabledforeground="#a3a3a3")
        self.l3_1.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l3_1.configure(foreground="#000000")
        self.l3_1.configure(highlightbackground="#d9d9d9")
        self.l3_1.configure(highlightcolor="black")
        self.l3_1.configure(text='''Week Report''')

        self.report = tk.Button(self.c1)
        self.report.place(relx=0.704, rely=0.483, height=64, width=167)
        self.report.configure(activebackground="#ececec")
        self.report.configure(activeforeground="#000000")
        self.report.configure(background="#d9d9d9")
        self.report.configure(disabledforeground="#a3a3a3")
        self.report.configure(foreground="#000000")
        self.report.configure(highlightbackground="#d9d9d9")
        self.report.configure(highlightcolor="black")
        self.report.configure(pady="0")
        self.report.configure(text='''Report''')
        self.report.bind('<Button-1>',lambda e:menu_support.report(e))

        self.l1 = tk.Label(top)
        self.l1.place(relx=0.122, rely=0.038, height=92, width=625)
        self.l1.configure(activebackground="#f9f9f9")
        self.l1.configure(activeforeground="black")
        self.l1.configure(background="#d9d9d9")
        self.l1.configure(disabledforeground="#a3a3a3")
        self.l1.configure(font="-family {Albertus Medium} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l1.configure(foreground="#000000")
        self.l1.configure(highlightbackground="#d9d9d9")
        self.l1.configure(highlightcolor="black")
        self.l1.configure(text='''V S Associates Engineering contractors''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





