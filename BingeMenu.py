from tkinter import *
import sys
import time
from tkinter.messagebox import showinfo
import datetime

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



            
            

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
   
    root.mainloop()
    
    

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)

    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
noodles_qty = 0
burger_qty = 0
pasta_qty = 0
fries_qty = 0
pizza_qty = 0
wraps_qty = 0
honeychilli_qty = 0
coke_qty = 0
icescream_qty = 0
tea_qty = 0
class Toplevel1:
    
    def __init__(self, top=None):
        def reset():
                   global noodles_qty
                   global burger_qty
                   global pasta_qty
                   global fries_qty
                   global pizza_qty
                   global wraps_qty
                   global honeychilli_qty
                   honeychilli_qty = 0
                   wraps_qty = 0
                   noodles_qty = 0
                   burger_qty = 0
                   pasta_qty = 0
                   fries_qty = 0
                   pizza_qty = 0
                   coke_qty = 0
                   icescream_qty = 0
                   tea_qty = 0
                   showinfo("Reset all Items", "All Items Reset!!")
                   self.Label4.config(text="0")
                   self.Label3.config(text="0")
                   self.Label5.config(text="0")
                   self.Label6.config(text="0")
                   self.Label8.config(text="0")
                   self.Label10.config(text='0')
                   self.Label11.config(text='0')
                   self.Label12.config(text='0')
                   self.Label13.config(text='0')
                   self.Label14.config(text='0')
                   
                    
                
              
                
                
                
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1920x1080+606+270")
        top.minsize(120, 1)
        top.maxsize(2000,2000)
        top.resizable(1, 1)
        top.title("BINGE HOUSE")
        top.configure(background="#d9d9d9")
        noodles_qty = 0
        burger_qty = 0
        pasta_qty = 0

        def noodlespos():
            global noodles_qty # inform funtion to use external variable `noodles_qty`

            noodles_qty = noodles_qty + 1
            print(noodles_qty)
            self.Label3 = tk.Label(top)
            self.Label3.place(relx=0.001, rely=0.253, height=80, width=87)
            self.Label3.configure(background="#FFC0CB")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(text=f'{noodles_qty}')
        def noodlesneg():
            global noodles_qty # inform funtion to use external variable `noodles_qty`

            noodles_qty = noodles_qty - 1
            if noodles_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                noodles_qty=0
            print(noodles_qty)
            self.Label3 = tk.Label(top)
            self.Label3.place(relx=0.001, rely=0.253, height=80, width=87)
            self.Label3.configure(background="#FFC0CB")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(text=f'{noodles_qty}')
            
        def burgerpos():
            global burger_qty # inform funtion to use external variable `noodles_qty`

            burger_qty = burger_qty + 1
            print(noodles_qty)
            self.Label4 = tk.Label(top)
            self.Label4.place(relx=0.001, rely=0.363, height=80, width=87)
            self.Label4.configure(background="#FFC0CB")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(foreground="#000000")
            self.Label4.configure(text=burger_qty) 
        def burgerneg():
            global burger_qty # inform funtion to use external variable `noodles_qty`

            burger_qty = burger_qty - 1
            if burger_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                burger_qty=0
            print(noodles_qty)
            self.Label4 = tk.Label(top)
            self.Label4.place(relx=0.001, rely=0.363, height=80, width=87)
            self.Label4.configure(background="#FFC0CB")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(foreground="#000000")
            self.Label4.configure(text=burger_qty)

        def pastapos():
            global pasta_qty # inform funtion to use external variable `noodles_qty`
            
            pasta_qty = pasta_qty + 1
            print(pasta_qty)
            self.Label8 = tk.Label(top)
            self.Label8.place(relx=0.001, rely=0.473, height=80, width=87)
            self.Label8.configure(background="#FFC0CB")
            self.Label8.configure(disabledforeground="#a3a3a3")
            self.Label8.configure(foreground="#000000")
            self.Label8.configure(text=pasta_qty) 
            
        def pastaneg():
            global pasta_qty # inform funtion to use external variable `noodles_qty`

            pasta_qty = pasta_qty - 1
            if pasta_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                pasta_qty=0
            print(pasta_qty)
            self.Label8 = tk.Label(top)
            self.Label8.place(relx=0.001, rely=0.473, height=80, width=87)
            self.Label8.configure(background="#FFC0CB")
            self.Label8.configure(disabledforeground="#a3a3a3")
            self.Label8.configure(foreground="#000000")
            self.Label8.configure(text=pasta_qty)
        def friespos():
            global fries_qty # inform funtion to use external variable `noodles_qty`

            fries_qty = fries_qty + 1
            if fries_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                fries_qty=0
            print(fries_qty)
            self.Label5 = tk.Label(top)
            self.Label5.place(relx=0.001, rely=0.583, height=80, width=87)
            self.Label5.configure(background="#FFC0CB")
            self.Label5.configure(disabledforeground="#a3a3a3")
            self.Label5.configure(foreground="#000000")
            self.Label5.configure(text=fries_qty)
        def friesneg():
            global fries_qty # inform funtion to use external variable `noodles_qty`

            fries_qty = fries_qty - 1
            if fries_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                fries_qty=0
            print(pasta_qty)
            self.Label5 = tk.Label(top)
            self.Label5.place(relx=0.001, rely=0.583, height=80, width=87)
            self.Label5.configure(background="#FFC0CB")
            self.Label5.configure(disabledforeground="#a3a3a3")
            self.Label5.configure(foreground="#000000")
            self.Label5.configure(text=fries_qty)
            
        def pizzapos():
            global pizza_qty # inform funtion to use external variable `noodles_qty`

            pizza_qty = pizza_qty + 1
            if pizza_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                pizza_qty=0
            print(pizza_qty)
            self.Label6 = tk.Label(top)
            self.Label6.place(relx=0.001, rely=0.693, height=80, width=87)
            self.Label6.configure(background="#FFC0CB")
            self.Label6.configure(disabledforeground="#a3a3a3")
            self.Label6.configure(foreground="#000000")
            self.Label6.configure(text=pizza_qty)
            
        def pizzaneg():
            global pizza_qty # inform funtion to use external variable `noodles_qty`

            pizza_qty = pizza_qty - 1
            if pizza_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                pizza_qty=0
            print(pizza_qty)
            self.Label6 = tk.Label(top)
            self.Label6.place(relx=0.001, rely=0.693, height=80, width=87)
            self.Label6.configure(background="#FFC0CB")
            self.Label6.configure(disabledforeground="#a3a3a3")
            self.Label6.configure(foreground="#000000")
            self.Label6.configure(text=pizza_qty)
            
        def wrapspos():
            global wraps_qty # inform funtion to use external variable `noodles_qty`

            wraps_qty = wraps_qty + 1
            if wraps_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                wraps_qty=0
            print(wraps_qty)
            self.Label10 = tk.Label(top)
            self.Label10.place(relx=0.2, rely=0.253, height=80, width=87)
            self.Label10.configure(background="#FFC0CB")
            self.Label10.configure(disabledforeground="#a3a3a3")
            self.Label10.configure(foreground="#000000")
            self.Label10.configure(text=wraps_qty)
            
        def wrapsneg():
            global wraps_qty # inform funtion to use external variable `noodles_qty`

            wraps_qty = wraps_qty - 1
            if wraps_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                wraps_qty=0
            print(wraps_qty)
            self.Label10 = tk.Label(top)
            self.Label10.place(relx=0.2, rely=0.253, height=80, width=87)
            self.Label10.configure(background="#FFC0CB")
            self.Label10.configure(disabledforeground="#a3a3a3")
            self.Label10.configure(foreground="#000000")
            self.Label10.configure(text=wraps_qty)
            
        def honeychillipos():
            global honeychilli_qty # inform funtion to use external variable `noodles_qty`

            honeychilli_qty = honeychilli_qty + 1
            if honeychilli_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                honeychilli_qty=0
            print(honeychilli_qty)
            self.Label11 = tk.Label(top)
            self.Label11.place(relx=0.2, rely=0.363, height=80, width=87)
            self.Label11.configure(background="#FFC0CB")
            self.Label11.configure(disabledforeground="#a3a3a3")
            self.Label11.configure(foreground="#000000")
            self.Label11.configure(text=honeychilli_qty)
            
        def honeychillineg():
            global honeychilli_qty # inform funtion to use external variable `noodles_qty`

            honeychilli_qty = honeychilli_qty - 1
            if honeychilli_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                honeychilli_qty=0
            print(honeychilli_qty)
            self.Label11 = tk.Label(top)
            self.Label11.place(relx=0.2, rely=0.363, height=80, width=87)
            self.Label11.configure(background="#FFC0CB")
            self.Label11.configure(disabledforeground="#a3a3a3")
            self.Label11.configure(foreground="#000000")
            self.Label11.configure(text=honeychilli_qty)
            
        def cokepos():
            global coke_qty # inform funtion to use external variable `noodles_qty`

            coke_qty = coke_qty + 1
            if coke_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                coke_qty=0
            print(honeychilli_qty)
            self.Label12 = tk.Label(top)
            self.Label12.place(relx=0.2, rely=0.473, height=80, width=87)
            self.Label12.configure(background="#FFC0CB")
            self.Label12.configure(disabledforeground="#a3a3a3")
            self.Label12.configure(foreground="#000000")
            self.Label12.configure(text=coke_qty)
        
        def cokeneg():
            global coke_qty # inform funtion to use external variable `noodles_qty`

            coke_qty = coke_qty - 1
            if coke_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                coke_qty=0
            print(honeychilli_qty)
            self.Label12 = tk.Label(top)
            self.Label12.place(relx=0.2, rely=0.473, height=80, width=87)
            self.Label12.configure(background="#FFC0CB")
            self.Label12.configure(disabledforeground="#a3a3a3")
            self.Label12.configure(foreground="#000000")
            self.Label12.configure(text=coke_qty)
        def icecreampos():
            global icescream_qty # inform funtion to use external variable `noodles_qty`

            icescream_qty = icescream_qty + 1
            if icescream_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                icescream_qty=0
            print(icescream_qty)
            self.Label13 = tk.Label(top)
            self.Label13.place(relx=0.2, rely=0.583, height=80, width=87)
            self.Label13.configure(background="#FFC0CB")
            self.Label13.configure(disabledforeground="#a3a3a3")
            self.Label13.configure(foreground="#000000")
            self.Label13.configure(text=icescream_qty)
            
        def icecreamneg():
            global icescream_qty # inform funtion to use external variable `noodles_qty`

            icescream_qty = icescream_qty - 1
            if icescream_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                icescream_qty=0
            print(icescream_qty)
            self.Label13 = tk.Label(top)
            self.Label13.place(relx=0.2, rely=0.583, height=80, width=87)
            self.Label13.configure(background="#FFC0CB")
            self.Label13.configure(disabledforeground="#a3a3a3")
            self.Label13.configure(foreground="#000000")
            self.Label13.configure(text=icescream_qty)
            
        def teapos():
            global tea_qty # inform funtion to use external variable `noodles_qty`

            tea_qty = tea_qty + 1
            if tea_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                tea_qty=0
            print(tea_qty)
            self.Label14 = tk.Label(top)
            self.Label14.place(relx=0.2, rely=0.693, height=80, width=87)
            self.Label14.configure(background="#FFC0CB")
            self.Label14.configure(disabledforeground="#a3a3a3")
            self.Label14.configure(foreground="#000000")
            self.Label14.configure(text=tea_qty)
            
        def teaneg():
            global tea_qty # inform funtion to use external variable `noodles_qty`

            tea_qty = tea_qty - 1
            if tea_qty<0:
                showinfo("Error","Item cant be less than 0!!",icon='error')
                tea_qty=0
            print(tea_qty)
            self.Label14 = tk.Label(top)
            self.Label14.place(relx=0.2, rely=0.693, height=80, width=87)
            self.Label14.configure(background="#FFC0CB")
            self.Label14.configure(disabledforeground="#a3a3a3")
            self.Label14.configure(foreground="#000000")
            self.Label14.configure(text=tea_qty)
            
            
            
            
            
            
        
        
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.1, rely=0.253, height=30, width=80)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Noodle +''', command=noodlespos)
        
        self.Button11 = tk.Button(top)
        self.Button11.place(relx=0.1, rely=0.300, height=30, width=80)
        self.Button11.configure(activebackground="#ececec")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''Noodle -''', command=noodlesneg)  

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.363, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Burger+''',command=burgerpos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.410, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Burger-''',command=burgerneg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.473, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Pasta+''',command=pastapos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.520, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Pasta-''',command=pastaneg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.583, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Fries+''',command=friespos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.630, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Fries-''',command=friesneg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.693, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Pizza+''',command=pizzapos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.1, rely=0.740, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Pizza-''',command=pizzaneg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.253, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Wraps+''',command=wrapspos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.300, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Wraps-''',command=wrapsneg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.363, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''HoneyChilli+''',command=honeychillipos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.410, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''HoneyChilli-''',command=honeychillineg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.473, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Coke+''',command=cokepos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.520, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Coke-''',command=cokeneg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.583, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''IceCream+''',command=icecreampos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.630, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''IceCream-''',command=icecreamneg)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.693, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Tea+''',command=teapos)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.25, rely=0.740, height=30, width=80)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Tea-''',command=teaneg)
        
        
       
       
       
       
       
       
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.01, rely=0.800, height=80, width=87)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Reset''', command=reset)
        

       
        
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.35, rely=0.032, height=71, width=650)
        self.Label1.configure(background="#FFC0CB")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''FOOD MENU''',font=("Times new roman", "50", "bold"), relief="groove")
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.45, rely=0.10, height=65, width=293,)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        localtime = time.asctime()
        self.Label2.configure(text=localtime,font=("arial", "15"))
       
        
        
       
        
        
        
        

if __name__ == '__main__':
    vp_start_gui()





