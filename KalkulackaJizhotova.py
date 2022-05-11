#!/usr/bin/env python3
# Soubor:  kalkulacka.py
# Datum:   28.03.2022 08:31
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
############################################################################

import math
from re import M
import tkinter as tk 

from tkinter import  CENTER,  E, LEFT, TOP,  N,W, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry, END, ACTIVE
from os.path import basename , splitext

# Operace s dvěma operandy 

dva_operandy = {}
dva_operandy["+"] = lambda a, b: a + b
dva_operandy["-"] = lambda a, b: a - b
dva_operandy["*"] = lambda a, b: a * b
dva_operandy["/"] = lambda a, b: a / b
dva_operandy["//"] = lambda a, b: a // b
dva_operandy["**"] = lambda a, b: a ** b

# Operace s jedním operandem 

jeden_operand = {}
jeden_operand["sin"] = math.sin
jeden_operand["cos"] = math.cos
jeden_operand["tg"] = math.tan
jeden_operand["tan"] = math.tan


# Okno 

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Superkalkulátor"

    def __init__(self):
        super().__init__(className=self.name)

        self.vyraz = ""
        
        self.zasobnik = []
        
        self.rovnice = StringVar()
        
        self.geometry("435x377")
        
        self.bind("<Escape>", self.quit)
        
        self.nadpis = tk.Label(self, text="Kalkulačka s posfixovou notací")
        self.nadpis.grid(row = 0,column=2,columnspan=6)
        
        self.EmptyLabel = tk.Label(self)
        self.EmptyLabel.grid(row = 1,column=4)
        
        self.labelframeCisla = tk.LabelFrame(self , text="Čísla")
        self.labelframeCisla.grid(row=2,column=2,sticky = W,rowspan=5)
        
        self.BtnCislo1 = Button(self.labelframeCisla, text=' 1 ', command=lambda: self.stisk(1), height=1, width=7)
        self.BtnCislo1.grid(row = 2, column = 2)
        
        self.BtnCislo2 = Button(self.labelframeCisla, text=' 2 ', command=lambda: self.stisk(2), height=1, width=7)
        self.BtnCislo2.grid(row= 2, column=3)
        
        self.BtnCislo3 = Button(self.labelframeCisla, text=' 3 ', command=lambda: self.stisk(3), height=1, width=7)
        self.BtnCislo3.grid(row= 2, column=4)
        
        self.BtnCislo4 = Button(self.labelframeCisla, text=' 4 ', command=lambda: self.stisk(4), height=1, width=7)
        self.BtnCislo4.grid(row=3, column=2)
        
        self.BtnCislo5 = Button(self.labelframeCisla, text=' 5 ', command=lambda: self.stisk(5), height=1, width=7)
        self.BtnCislo5.grid(row=3, column=3)
        
        self.BtnCislo6 = Button(self.labelframeCisla, text=' 6 ', command=lambda: self.stisk(6), height=1, width=7)
        self.BtnCislo6.grid(row=3, column=4)
        
        self.BtnCislo7 = Button(self.labelframeCisla, text=' 7 ', command=lambda: self.stisk(7), height=1, width=7)
        self.BtnCislo7.grid(row=4, column=2)
        
        self.BtnCislo8 = Button(self.labelframeCisla, text=' 8 ', command=lambda: self.stisk(8), height=1, width=7)
        self.BtnCislo8.grid(row=4, column=3)
        
        self.BtnCislo9 = Button(self.labelframeCisla, text=' 9 ', command=lambda: self.stisk(9), height=1, width=7)
        self.BtnCislo9.grid(row=4, column=4)
        
        self.BtnCislo0 = Button(self.labelframeCisla, text=' 0 ', command=lambda: self.stisk(0), height=1, width=7)
        self.BtnCislo0.grid(row=5, column=2)
        
        self.labelframeOperace = tk.LabelFrame(self , text="Operace",height= 25)
        self.labelframeOperace.grid(row=2,column=3)
        
        self.btnOperacePlus = Button(self.labelframeOperace, text=' + ', command=lambda: self.stisk("+"), height=1, width=7)
        self.btnOperacePlus.grid(row=3, column=5)
        
        self.btnOperaceMinus = Button(self.labelframeOperace, text=' - ', command=lambda: self.stisk("-"), height=1, width=7)
        self.btnOperaceMinus.grid(row=3, column=6)
        
        self.btnOperaceNasobeni = Button(self.labelframeOperace, text=' * ', command=lambda: self.stisk("*"), height=1, width=7)
        self.btnOperaceNasobeni.grid(row=3, column=6)
        
        self.btnOperaceDeleni = Button(self.labelframeOperace, text=' / ', command=lambda: self.stisk("/"), height=1, width=7)
        self.btnOperaceDeleni.grid(row=5, column=5)
        
        self.btnOperaceCeloscisloDeleni = Button(self.labelframeOperace, text=' //', command=lambda: self.stisk("//"), height=1, width=7)
        self.btnOperaceCeloscisloDeleni.grid(row=5, column=6)
        
        self.btnOperaceMocnina = Button(self.labelframeOperace, text=' **', command=lambda: self.stisk("**"), height=1, width=7)
        self.btnOperaceMocnina.grid(row=4, column=6)
        
        
        self.btnDesetinne = Button(self.labelframeCisla, text='.', command=lambda: self.stisk("."), height=1, width=7)
        self.btnDesetinne.grid(row=5, column=3)
        
        
        self.labelframeGF = tk.LabelFrame(self , text="G. Fce")
        self.labelframeGF.grid(row=2,column=4)
        
        self.Sinus = Button(self.labelframeGF, text='sin', command=lambda: self.stisk("sin"), height=1, width=7)
        self.Sinus.grid(row=2, column=5)
        
        self.Cosinus = Button(self.labelframeGF, text='cos', command=lambda: self.stisk("cos"), height=1, width=7)
        self.Cosinus.grid(row=3, column=5)
        
        self.Tangens = Button(self.labelframeGF, text='tan', command=lambda: self.stisk("tan"), height=1, width=7)
        self.Tangens.grid(row=4, column=5)
        
        self.pi = Button(self.labelframeOperace, text='π', command=lambda: self.stisk(3.14), height=1, width=7)
        self.pi.grid(row=4, column=5)
       
        self.labelframeNeworkuje = tk.LabelFrame(self , text="Tlacitka")
        self.labelframeNeworkuje.grid(row=2,column=5)
        
        
        self.BtnQuit = tk.Button(self.labelframeNeworkuje, text = "Quit", command = self.quit, height=1, width=7)
        self.BtnQuit.grid(row = 4, column = 6)
        
        self.BtnEnter = tk.Button(self.labelframeNeworkuje, text="Enter", command=self.fce, height=1, width=7)
        self.BtnEnter.grid(row=2, column=6)
        
        self.clear = Button(self.labelframeNeworkuje, text='Clear', command=self.vycistit, height=1, width=7)
        self.clear.grid(row=3, column=6)
        
        self.EmptyLabel = tk.Label(self)
        self.EmptyLabel.grid(row = 6,column=8)
        
        self.EmptyLabel = tk.Label(self)
        self.EmptyLabel.grid(row = 6,column=8)
        
        self.vstup = Frame(self)
        self.vstup.grid(row = 11, column =9)

        self.entry = Entry(self, textvariable=self.rovnice, width=40)
        self.entry.grid(rowspan = 10, columnspan = 8)
        
        self.listbox = tk.Listbox(self, width=40)
        self.listbox.grid(rowspan = 11, columnspan = 8)


# Funkce 

    def stisk(self, num):   
            self.vyraz = self.vyraz + str(num)
            self.rovnice.set(self.vyraz)

    def equalpress(self):
        try:
            total = str(eval(self.vyraz))
            self.rovnice.set(total)
            self.vyraz = ""
    
        except:
            self.rovnice.set(" error ")
            self.vyraz = ""

    def vycistit(self):
        self.listbox.delete(0,tk.END)
        self.vyraz = ""
        self.rovnice.set("")

    def fce(self):
        self.schroustej(self.entry.get())
        self.vyraz = ""
        self.rovnice.set("")
    
    def Znovu_nacist_listbox(self):
        self.listbox.delete(0, END)
        for item in self.zasobnik:
            self.listbox.insert(END, item)

                
    
    def quit(self, event = None):
        super().quit()


    def operace(self, token, event= None):
            
            token = str(self.entry.get())
            
            if token.upper() == "Q":
                exit()
            if token.upper() == "PI":
                self.zasobnik.append(math.pi)
            if token.upper() == "SW":
                b = self.listbox.pop(tk.END-1)
                a = self.listbox.pop(tk.END)
                self.zasobnik.append(b)
                self.zasobnik.append(a)
            if token in dva_operandy.keys():
                if len(self.zasobnik) >= 2:
                    b = self.zasobnik.pop()
                    a = self.zasobnik.pop()
                    self.zasobnik.append(dva_operandy[token](a, b))
                else:
                    print("Nemám dost operandů!!!")
            if token in jeden_operand.keys():
                if len(self.zasobnik) >= 1:
                    a = self.zasobnik.pop()
                    self.zasobnik.append(jeden_operand[token](a))
                else:
                    print("Nemám dost operandů!!!")

            self.listbox.delete(0,tk.END)
            for token in self.zasobnik:
                self.listbox.insert(tk.END,token)


    def schroustej(self, token, event =None ):
        try:
            self.zasobnik.append(float(token))
            self.listbox.insert(tk.END,token)
        except ValueError:
            self.operace(token)

# Mainloop 

app = Application()
app.mainloop()
