#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 18, 2020 12:47:51 PM IST  platform: Windows NT

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

import bio_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Bio (root)
    bio_support.init(root, top)
    root.mainloop()

w = None
def create_Bio(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Bio(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Bio (w)
    bio_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Bio():
    global w
    w.destroy()
    w = None

class Bio:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 18"
        font11 = "-family {Segoe UI Black} -size 12 -weight bold"
        font9 = "-family {Segoe UI Black} -size 18 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1007x751")
        top.minsize(120, 2)
        top.maxsize(1924, 1065)
        top.resizable(1, 1)
        top.title("VSA")
        top.configure(relief="raised")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.c1 = tk.Canvas(top)
        self.c1.place(relx=0.02, rely=0.08, relheight=0.881, relwidth=0.963)
        self.c1.configure(background="#ffffff")
        self.c1.configure(borderwidth="2")
        self.c1.configure(highlightbackground="#c0c0c0")
        self.c1.configure(highlightcolor="black")
        self.c1.configure(insertbackground="black")
        self.c1.configure(relief="ridge")
        self.c1.configure(selectbackground="blue")
        self.c1.configure(selectforeground="white")

        self.l2_11 = tk.Label(self.c1)
        self.l2_11.place(relx=0.155, rely=0.03, height=46, width=141)
        self.l2_11.configure(activebackground="#f9f9f9")
        self.l2_11.configure(activeforeground="black")
        self.l2_11.configure(background="#ffffff")
        self.l2_11.configure(disabledforeground="#a3a3a3")
        self.l2_11.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_11.configure(foreground="#000000")
        self.l2_11.configure(highlightbackground="#d9d9d9")
        self.l2_11.configure(highlightcolor="black")
        self.l2_11.configure(text='''Enter the Name''')

        self.name = tk.Entry(self.c1)
        self.name.place(relx=0.337, rely=0.029,height=40, relwidth=0.272)
        self.name.configure(background="white")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="TkFixedFont20")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="black")
        self.name.configure(insertbackground="black")
        self.name.configure(selectbackground="blue")
        self.name.configure(selectforeground="white")

        self.l2_2 = tk.Label(self.c1)
        self.l2_2.place(relx=0.165, rely=0.121, height=40, width=123)
        self.l2_2.configure(activebackground="#f9f9f9")
        self.l2_2.configure(activeforeground="black")
        self.l2_2.configure(background="#ffffff")
        self.l2_2.configure(disabledforeground="#a3a3a3")
        self.l2_2.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_2.configure(foreground="#000000")
        self.l2_2.configure(highlightbackground="#d9d9d9")
        self.l2_2.configure(highlightcolor="black")
        self.l2_2.configure(text='''Enter the Role''')

        self.role = tk.Entry(self.c1)
        self.role.place(relx=0.337, rely=0.116,height=40, relwidth=0.272)
        self.role.configure(background="white")
        self.role.configure(disabledforeground="#a3a3a3")
        self.role.configure(font="TkFixedFont20")
        self.role.configure(foreground="#000000")
        self.role.configure(highlightbackground="#d9d9d9")
        self.role.configure(highlightcolor="black")
        self.role.configure(insertbackground="black")
        self.role.configure(selectbackground="blue")
        self.role.configure(selectforeground="white")

        self.l2_6 = tk.Label(self.c1)
        self.l2_6.place(relx=0.144, rely=0.211, height=29, width=153)
        self.l2_6.configure(activebackground="#f9f9f9")
        self.l2_6.configure(activeforeground="black")
        self.l2_6.configure(background="#ffffff")
        self.l2_6.configure(disabledforeground="#a3a3a3")
        self.l2_6.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_6.configure(foreground="#000000")
        self.l2_6.configure(highlightbackground="#d9d9d9")
        self.l2_6.configure(highlightcolor="black")
        self.l2_6.configure(text='''Enter the Acc.No.''')

        self.acc_no = tk.Entry(self.c1)
        self.acc_no.place(relx=0.337, rely=0.205,height=40, relwidth=0.272)
        self.acc_no.configure(background="white")
        self.acc_no.configure(disabledforeground="#a3a3a3")
        self.acc_no.configure(font="TkFixedFont20")
        self.acc_no.configure(foreground="#000000")
        self.acc_no.configure(highlightbackground="#d9d9d9")
        self.acc_no.configure(highlightcolor="black")
        self.acc_no.configure(insertbackground="black")
        self.acc_no.configure(selectbackground="blue")
        self.acc_no.configure(selectforeground="white")

        self.l2_7 = tk.Label(self.c1)
        self.l2_7.place(relx=0.118, rely=0.292, height=30, width=185)
        self.l2_7.configure(activebackground="#f9f9f9")
        self.l2_7.configure(activeforeground="black")
        self.l2_7.configure(background="#ffffff")
        self.l2_7.configure(disabledforeground="#a3a3a3")
        self.l2_7.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_7.configure(foreground="#000000")
        self.l2_7.configure(highlightbackground="#d9d9d9")
        self.l2_7.configure(highlightcolor="black")
        self.l2_7.configure(text='''Enter the Acc.Name''')

        self.acc_name = tk.Entry(self.c1)
        self.acc_name.place(relx=0.337, rely=0.292,height=40, relwidth=0.272)
        self.acc_name.configure(background="white")
        self.acc_name.configure(disabledforeground="#a3a3a3")
        self.acc_name.configure(font="TkFixedFont20")
        self.acc_name.configure(foreground="#000000")
        self.acc_name.configure(highlightbackground="#d9d9d9")
        self.acc_name.configure(highlightcolor="black")
        self.acc_name.configure(insertbackground="black")
        self.acc_name.configure(selectbackground="blue")
        self.acc_name.configure(selectforeground="white")

        self.l2_8 = tk.Label(self.c1)
        self.l2_8.place(relx=0.107, rely=0.381, height=29, width=197)
        self.l2_8.configure(activebackground="#f9f9f9")
        self.l2_8.configure(activeforeground="black")
        self.l2_8.configure(background="#ffffff")
        self.l2_8.configure(disabledforeground="#a3a3a3")
        self.l2_8.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_8.configure(foreground="#000000")
        self.l2_8.configure(highlightbackground="#d9d9d9")
        self.l2_8.configure(highlightcolor="black")
        self.l2_8.configure(text='''Enter the Bank Name''')

        self.bank = tk.Entry(self.c1)
        self.bank.place(relx=0.337, rely=0.381,height=40, relwidth=0.272)
        self.bank.configure(background="white")
        self.bank.configure(disabledforeground="#a3a3a3")
        self.bank.configure(font="TkFixedFont20")
        self.bank.configure(foreground="#000000")
        self.bank.configure(highlightbackground="#d9d9d9")
        self.bank.configure(highlightcolor="black")
        self.bank.configure(insertbackground="black")
        self.bank.configure(selectbackground="blue")
        self.bank.configure(selectforeground="white")

        self.l2_1 = tk.Label(self.c1)
        self.l2_1.place(relx=0.124, rely=0.468, height=25, width=179)
        self.l2_1.configure(activebackground="#f9f9f9")
        self.l2_1.configure(activeforeground="black")
        self.l2_1.configure(background="#ffffff")
        self.l2_1.configure(disabledforeground="#a3a3a3")
        self.l2_1.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_1.configure(foreground="#000000")
        self.l2_1.configure(highlightbackground="#d9d9d9")
        self.l2_1.configure(highlightcolor="black")
        self.l2_1.configure(text='''Enter Branch Name''')

        self.branch = tk.Entry(self.c1)
        self.branch.place(relx=0.337, rely=0.468,height=40, relwidth=0.272)
        self.branch.configure(background="white")
        self.branch.configure(disabledforeground="#a3a3a3")
        self.branch.configure(font="TkFixedFont20")
        self.branch.configure(foreground="#000000")
        self.branch.configure(highlightbackground="#d9d9d9")
        self.branch.configure(highlightcolor="black")
        self.branch.configure(insertbackground="black")
        self.branch.configure(selectbackground="blue")
        self.branch.configure(selectforeground="white")

        self.l2_9 = tk.Label(self.c1)
        self.l2_9.place(relx=0.124, rely=0.559, height=23, width=173)
        self.l2_9.configure(activebackground="#f9f9f9")
        self.l2_9.configure(activeforeground="black")
        self.l2_9.configure(background="#ffffff")
        self.l2_9.configure(disabledforeground="#a3a3a3")
        self.l2_9.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_9.configure(foreground="#000000")
        self.l2_9.configure(highlightbackground="#d9d9d9")
        self.l2_9.configure(highlightcolor="black")
        self.l2_9.configure(text='''Enter the IFSC Code''')

        self.ifsc = tk.Entry(self.c1)
        self.ifsc.place(relx=0.337, rely=0.559,height=40, relwidth=0.272)
        self.ifsc.configure(background="white")
        self.ifsc.configure(disabledforeground="#a3a3a3")
        self.ifsc.configure(font="TkFixedFont20")
        self.ifsc.configure(foreground="#000000")
        self.ifsc.configure(highlightbackground="#d9d9d9")
        self.ifsc.configure(highlightcolor="black")
        self.ifsc.configure(insertbackground="black")
        self.ifsc.configure(selectbackground="blue")
        self.ifsc.configure(selectforeground="white")

        self.back = tk.Button(self.c1)
        self.back.place(relx=0.810, rely=0.68, height=54, width=167)
        self.back.configure(activebackground="#ececec")
        self.back.configure(activeforeground="#000000")
        self.back.configure(background="#d9d9d9")
        self.back.configure(disabledforeground="#a3a3a3")
        self.back.configure(foreground="#000000")
        self.back.configure(highlightbackground="#d9d9d9")
        self.back.configure(highlightcolor="black")
        self.back.configure(pady="0")
        self.back.configure(text='''Back''')
        self.back.bind('<Button-1>',lambda e:bio_support.menu(e))

        self.refresh = tk.Button(self.c1)
        self.refresh.place(relx=0.124, rely=0.68, height=34, width=87)
        self.refresh.configure(activebackground="#ececec")
        self.refresh.configure(activeforeground="#000000")
        self.refresh.configure(background="#d9d9d9")
        self.refresh.configure(disabledforeground="#a3a3a3")
        self.refresh.configure(foreground="#000000")
        self.refresh.configure(highlightbackground="#d9d9d9")
        self.refresh.configure(highlightcolor="black")
        self.refresh.configure(pady="0")
        self.refresh.configure(text='''Refresh''')
        self.refresh.bind('<Button-1>',lambda e:bio_support.refresh(e))

        self.submit = tk.Button(self.c1)
        self.submit.place(relx=0.701, rely=0.272, height=74, width=207)
        self.submit.configure(activebackground="#ececec")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#d9d9d9")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(font=font9)
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
        self.submit.configure(text='''Submit''')
        self.submit.bind('<ButtonPress-1>',lambda e:bio_support.submit(e))
        self.submit.bind('<ButtonRelease-1>',lambda e:bio_support.refresh(e))

        self.TSeparator1 = ttk.Separator(self.c1)
        self.TSeparator1.place(relx=0.041, rely=0.77, relwidth=0.567)

        self.Label1 = tk.Label(self.c1)
        self.Label1.place(relx=0.041, rely=0.785, height=31, width=284)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''To Edit Stored BioData''')

        self.l2_1 = tk.Label(self.c1)
        self.l2_1.place(relx=0.072, rely=0.861, height=46, width=140)
        self.l2_1.configure(activebackground="#f9f9f9")
        self.l2_1.configure(activeforeground="black")
        self.l2_1.configure(background="#ffffff")
        self.l2_1.configure(disabledforeground="#a3a3a3")
        self.l2_1.configure(font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.l2_1.configure(foreground="#000000")
        self.l2_1.configure(highlightbackground="#d9d9d9")
        self.l2_1.configure(highlightcolor="black")
        self.l2_1.configure(text='''Enter the Name''')

        self.name_2 = tk.Entry(self.c1)
        self.name_2.place(relx=0.268, rely=0.876,height=40, relwidth=0.272)
        self.name_2.configure(background="white")
        self.name_2.configure(disabledforeground="#a3a3a3")
        self.name_2.configure(font="TkFixedFont20")
        self.name_2.configure(foreground="#000000")
        self.name_2.configure(highlightbackground="#d9d9d9")
        self.name_2.configure(highlightcolor="black")
        self.name_2.configure(insertbackground="black")
        self.name_2.configure(selectbackground="blue")
        self.name_2.configure(selectforeground="white")

        self.edit = tk.Button(self.c1)
        self.edit.place(relx=0.608, rely=0.861, height=44, width=117)
        self.edit.configure(activebackground="#ececec")
        self.edit.configure(activeforeground="#000000")
        self.edit.configure(background="#d9d9d9")
        self.edit.configure(disabledforeground="#a3a3a3")
        self.edit.configure(font=font11)
        self.edit.configure(foreground="#000000")
        self.edit.configure(highlightbackground="#d9d9d9")
        self.edit.configure(highlightcolor="black")
        self.edit.configure(pady="0")
        self.edit.configure(text='''Edit''')
        self.edit.bind('<Button-1>',lambda e:bio_support.edit(e))

        self.l1 = tk.Label(top)
        self.l1.place(relx=0.437, rely=0.027, height=33, width=132)
        self.l1.configure(activebackground="#f9f9f9")
        self.l1.configure(activeforeground="black")
        self.l1.configure(background="#d9d9d9")
        self.l1.configure(disabledforeground="#a3a3a3")
        self.l1.configure(font="-family {Segoe UI} -size 20 -weight bold -slant roman -underline 0 -overstrike 0")
        self.l1.configure(foreground="#000000")
        self.l1.configure(highlightbackground="#d9d9d9")
        self.l1.configure(highlightcolor="black")
        self.l1.configure(text='''BioDate''')

if __name__ == '__main__':
    vp_start_gui()





