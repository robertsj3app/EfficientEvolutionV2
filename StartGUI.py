from tkinter import ttk
from tkinter import *
import tkinter
from GUI import GUI
from Environment import Environment
from Individual import Individual
from Individual import TraitGenome

class StartGUI(object):
    def __init__(self):
        self.master = Tk()
        self.canvas = Canvas(self.master, width=1920, height=1080)
        self.gui = None
        self.env = None
        self.intro_label = tkinter.Label(self.master, text='Welcome to Efficient Evolution!')
        self.intro_label.place(x=450, y=150)
        self.constraint_label = tkinter.Label(self.master, text='Please do not make grid larger than 18x18')
        self.constraint_label.place(x=450, y=200)
        self.x_label = tkinter.Label(self.master, text="x size:")
        self.x_label.place(x=450, y=300)
        self.y_label = tkinter.Label(self.master, text="y size:")
        self.y_label.place(x=550, y=300)
        self.x_entry = tkinter.Entry(self.master, width=4)
        self.x_entry.place(x=500, y=300)
        self.y_entry = tkinter.Entry(self.master, width=4)
        self.y_entry.place(x=600, y=300)
        self.size_label = tkinter.Label(self.master, text='Size of each generation:')
        self.size_label.place(x=450, y=350)
        self.size_entry = tkinter.Entry(self.master, width=4)
        self.size_entry.place(x=590, y=350)
        self.start_button = tkinter.Button(self.master, height=2, width=4,
                                           text='Start', bd=0, bg='white',
                                           command=lambda: self.start_simulation())
        self.start_button.place(x=450, y=400)
        self.size = (-1,-1)
        self.master.attributes('-fullscreen', True)
        self.canvas.pack()

    def start_simulation(self):
        #self.canvas.delete()
        self.x = int(self.x_entry.get())
        self.y = int(self.y_entry.get())
        self.num_pop = int(self.size_entry.get())
        self.master.destroy()
        self.env = Environment(self.x, self.y, self.num_pop)
        self.env.insert_generation()
        self.gui = GUI(self.env)
        self.gui.make_grid()
        self.gui.examine_tile(0, 0)
        #self.gui.mainloop()

    def mainloop(self):
        mainloop()

#if __name__ == '__main__':
#    gui = GUI()
#    gui.make_grid()
#    mainloop()