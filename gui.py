from tkinter import *
import tkinter as tk


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Regions', width = 25, command = self.new_window)
        self.button2 = tk.Button(self.frame, text = 'Items', width = 25, command = self.new_window2)

        self.button1.pack()
        self.button2.pack()

        self.button1.pack()
        self.frame.pack()

   
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    
    def new_window2(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo3(self.newWindow)


class Demo2:

    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)

        regions = ['Light World',
                   'Hyrule Castle',
                   'Eastern Palace' ,
                   'Desert Palace' ,
                   'Death Mountain' ,
                   'Tower Of Hera' ,
                   'Castle Tower' ,
                   'Dark World',
                   'Dark Palace' ,
               'Swamp Palace' ,
                   'Skull Woods' ,
                   'Thieves Town',
                   'Ice Palace' ,
                   'Misery Mire' ,
               'Turtle Rock' ,
                   'Ganons Tower' ,
                   'Special']

        self.select = StringVar()

        self.drop = tk.OptionMenu(self.frame,self.select,*regions)
        self.reg = tk.Button(self.frame, text = 'select', command = self.show_value )

        self.drop.pack()
        self.reg.pack()
    
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
    def show_value(self):
        i = self.select.get()
        print(i)


    

    


class Demo3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        itemlist = [
            "TwentyRupees:18383",
            "Lamp:18383",
             "OneHundredRupees:18383",        
         "FiftyRupees:18383",
         "TenArrows:18383",       
         "ProgressiveSword:18383",
            "PendantOfWisdom:18383",
            "MoonPearl:18383"

        ]
        self.select = StringVar()

        self.drop = tk.OptionMenu(self.frame , self.select,*itemlist)

        self.itemButton = tk.Button(self.frame, text = 'select', width = 25, command = self.show_value)
        self.drop.pack()
        self.itemButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def show_value(self):
        i = self.select.get()
        print(i)


def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
