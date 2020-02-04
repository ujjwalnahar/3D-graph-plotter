from matplotlib.pyplot import *
import numpy as np
import numexpr as npx
from mpl_toolkits import mplot3d
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import tkinter.colorchooser as tkc

import tkinter.ttk as ttk







def plotll(e1,e2, x1, x2,t):

    if t=="2d function":
        try:


            x3 = int(x1)
            x4 = int(x2)
            x = np.linspace(x3, x4, 1000, endpoint=True)
            F = npx.evaluate(e1)
            fig = Figure(figsize=(6, 6))
            a = fig.add_subplot(111)
            a.plot(x, F)
        except SyntaxError:
            messagebox.showinfo("Error!", "Entered expression is not in specified format")
        except ValueError:
            messagebox.showinfo("Error!","Range for graph not entered")
        except Exception:
            messagebox.showinfo("Error", "Some error occured")

        else:
            canvas = FigureCanvasTkAgg(fig, master=root)


            canvas.get_tk_widget().configure(borderwidth="2")
            canvas.get_tk_widget().configure(highlightbackground="#d9d9d9")
            canvas.get_tk_widget().configure(highlightcolor="black")
            canvas.get_tk_widget().configure(insertbackground="#000000")
            canvas.get_tk_widget().configure(relief="ridge")
            canvas.get_tk_widget().configure(selectbackground="#c4c4c4")
            canvas.get_tk_widget().configure(selectforeground="black")
            canvas.get_tk_widget().place(relx=0.0, rely=0.505, relheight=0.457, relwidth=0.996)
            canvas.draw()
            toolbar = NavigationToolbar2Tk(canvas, root)
            toolbar.update()


    else:
        try:

            x = np.linspace(0, 4, 1000, endpoint=True)
            y = np.linspace(0, 4, 1000, endpoint=True)
            fig = Figure()
            a = fig.add_subplot(111, projection='3d')
            x, y = np.meshgrid(x, y)
            Z = eval(e2)




            a.plot_surface(x, y, Z, cmap='viridis', edgecolor='none')

            a.set_xlabel('X Label')
            a.set_ylabel('Y Label')

            a.set_zlabel('Z Label')
        except Exception:
            messagebox.showinfo(0,"Enter the expression in correct format")








        else:
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.get_tk_widget().configure(background="#ffffff")
            canvas.get_tk_widget().configure(borderwidth="2")
            canvas.get_tk_widget().configure(highlightbackground="#d9d9d9")
            canvas.get_tk_widget().configure(highlightcolor="black")
            canvas.get_tk_widget().configure(insertbackground="#000000")
            canvas.get_tk_widget().configure(relief="ridge")
            canvas.get_tk_widget().configure(selectbackground="#c4c4c4")
            canvas.get_tk_widget().configure(selectforeground="black")
            canvas.get_tk_widget().place(relx=0.0, rely=0.505, relheight=0.457, relwidth=0.996)
            canvas.draw()
            toolbar = NavigationToolbar2Tk(canvas, root)
            toolbar.update()

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import messagebox



# import mtplb as mp
# import mtplb3d as mp3



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()

    top = Toplevel1(root)

    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, top
    rt = root
    w = tk.Toplevel(root)
    gui_support.set_Tk_var()
    top = Toplevel1(w)
    gui_support.init(w, top, *args, **kwargs)
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
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("800x700+468+139")
        top.title("3D Graph plot")
        top.configure(background="#011d4a")
        top.configure(cursor="arrow")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.com = ttk.Combobox(master=root,values=['2d function', '3d fuction'])
        self.com.place(relx=0.301, rely=0.048, relheight=0.031, relwidth=0.512)
        self.com.set('select')
        self.com.configure(takefocus="")
        self.com.current(0)

        self.entfx = tk.Entry(top)
        self.entfx.place(relx=0.215, rely=0.167, height=24, relwidth=0.52)
        self.entfx.configure(background="white")
        self.entfx.configure(disabledforeground="#a3a3a3")
        self.entfx.configure(font="TkFixedFont")
        self.entfx.configure(foreground="#000000")
        self.entfx.insert(0,"eg.x**2")
        self.entfx.configure(highlightbackground="#d9d9d9")
        self.entfx.configure(highlightcolor="black")
        self.entfx.configure(insertbackground="black")
        self.entfx.configure(selectbackground="#c4c4c4")
        self.entfx.configure(selectforeground="black")

        self.functype = tk.Label(top)
        self.functype.place(relx=0.064, rely=0.048, height=26, width=95)
        self.functype.configure(activebackground="#efa91d")
        self.functype.configure(activeforeground="black")
        self.functype.configure(background="#d9d9d9")
        self.functype.configure(disabledforeground="#a3a3a3")
        self.functype.configure(foreground="#000000")
        self.functype.configure(highlightbackground="#d9d9d9")
        self.functype.configure(highlightcolor="black")
        self.functype.configure(text='''Function type''')

        self.funceq = tk.Label(top)
        self.funceq.place(relx=0.064, rely=0.108, height=26, width=129)
        self.funceq.configure(activebackground="#fff81f")
        self.funceq.configure(activeforeground="black")
        self.funceq.configure(background="#d9d9d9")
        self.funceq.configure(disabledforeground="#a3a3a3")
        self.funceq.configure(foreground="#000000")
        self.funceq.configure(highlightbackground="#d9d9d9")
        self.funceq.configure(highlightcolor="black")
        self.funceq.configure(text='''Function equation''')

        self.fx = tk.Label(top)
        self.fx.place(relx=0.075, rely=0.167, height=26, width=28)
        self.fx.configure(activebackground="#f9f9f9")
        self.fx.configure(activeforeground="black")
        self.fx.configure(background="#d9d9d9")
        self.fx.configure(disabledforeground="#a3a3a3")
        self.fx.configure(foreground="#000000")
        self.fx.configure(highlightbackground="#d9d9d9")
        self.fx.configure(highlightcolor="black")
        self.fx.configure(text='''f(x)''')
        self.fx.configure()

        self.z = tk.Label(top)
        self.z.place(relx=0.075, rely=0.251, height=26, width=15)
        self.z.configure(activebackground="#f9f9f9")
        self.z.configure(activeforeground="black")
        self.z.configure(background="#d9d9d9")
        self.z.configure(disabledforeground="#a3a3a3")
        self.z.configure(foreground="#000000")
        self.z.configure(highlightbackground="#d9d9d9")
        self.z.configure(highlightcolor="black")
        self.z.configure(text='''Z''')

        self.entz = tk.Entry(top)
        self.entz.place(relx=0.204, rely=0.251, height=24, relwidth=0.531)
        self.entz.configure(background="white")
        self.entz.configure(disabledforeground="#a3a3a3")
        self.entz.configure(font="TkFixedFont")
        self.entz.configure(foreground="#000000")
        self.entz.configure(highlightbackground="#d9d9d9")
        self.entz.configure(highlightcolor="black")
        self.entz.configure(insertbackground="black")
        self.entz.configure(selectbackground="#c4c4c4")
        self.entz.configure(selectforeground="black")
        self.entz.insert(0, "eg.(x**2)+(y**2)")

        self.startp = tk.Label(top)
        self.startp.place(relx=0.064, rely=0.323, height=26, width=76)
        self.startp.configure(activebackground="#f9f9f9")
        self.startp.configure(activeforeground="black")
        self.startp.configure(background="#d9d9d9")
        self.startp.configure(disabledforeground="#a3a3a3")
        self.startp.configure(foreground="#000000")
        self.startp.configure(highlightbackground="#d9d9d9")
        self.startp.configure(highlightcolor="black")
        self.startp.configure(text='''Start point''')

        self.entstartp = tk.Entry(top)
        self.entstartp.place(relx=0.193, rely=0.323, height=24, relwidth=0.208)
        self.entstartp.configure(background="white")
        self.entstartp.configure(disabledforeground="#a3a3a3")
        self.entstartp.configure(font="TkFixedFont")
        self.entstartp.configure(foreground="#000000")
        self.entstartp.configure(highlightbackground="#d9d9d9")
        self.entstartp.configure(highlightcolor="black")
        self.entstartp.configure(insertbackground="black")
        self.entstartp.configure(selectbackground="#c4c4c4")
        self.entstartp.configure(selectforeground="black")
        self.entstartp.insert(0, "eg.0")

        self.endp = tk.Label(top)
        self.endp.place(relx=0.548, rely=0.323, height=26, width=70)
        self.endp.configure(activebackground="#f9f9f9")
        self.endp.configure(activeforeground="black")
        self.endp.configure(background="#d9d9d9")
        self.endp.configure(disabledforeground="#a3a3a3")
        self.endp.configure(foreground="#000000")
        self.endp.configure(highlightbackground="#d9d9d9")
        self.endp.configure(highlightcolor="black")
        self.endp.configure(text='''End point''')



        self.entendp = tk.Entry(top)
        self.entendp.place(relx=0.698, rely=0.323, height=24, relwidth=0.208)
        self.entendp.configure(background="white")
        self.entendp.configure(disabledforeground="#a3a3a3")
        self.entendp.configure(font="TkFixedFont")
        self.entendp.configure(foreground="#000000")
        self.entendp.configure(highlightbackground="#d9d9d9")
        self.entendp.configure(highlightcolor="black")
        self.entendp.configure(insertbackground="black")
        self.entendp.configure(selectbackground="#c4c4c4")
        self.entendp.configure(selectforeground="black")
        self.entendp.insert(0, "eg.100")

        self.com = ttk.Combobox(top)
        self.com.place(relx=0.301, rely=0.048, relheight=0.031, relwidth=0.512)
        self.value_list = ['2d function', '3d fuction']
        self.com.configure(values=self.value_list)
        self.com.configure(takefocus="")
        self.com.current(0)

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)


        self.run = tk.Button(top)
        self.run.place(relx=0.380, rely=0.419, height=33, width=37)
        self.run.configure(activebackground="#ececec")
        self.run.configure(activeforeground="#000000")
        self.run.configure(background="#d9d9d9")
        self.run.configure(disabledforeground="#a3a3a3")
        self.run.configure(foreground="#000000")
        self.run.configure(highlightbackground="#d9d9d9")
        self.run.configure(highlightcolor="black")
        self.run.configure(pady="0")
        self.run.configure(text='''Run''')
        self.run.configure(command=lambda: plotll(self.entfx.get(),self.entz.get(), self.entstartp.get(), self.entendp.get(),self.com.get()))





if __name__ == '__main__':
    vp_start_gui()


