from tkinter import ttk
from tkinter import *
import tkinter
#from Environment import Environment
#from Tile import Tile
#from Individual import Individual
#from Individual import Genome

class GUI(object):
    def __init__(self, enviro):
        self.master = Tk()
        self.canvas = Canvas(self.master, width=1920, height=1080)
        self.env = enviro
        self.tile_canvas = Canvas(self.master, width = 192, height=108)
        self.buttons = []
        self.separator = ttk.Separator(self.master, orient='vertical')
        self.separator.place(relx=0.5, rely=0, relwidth=0.2, relheight=1)
        #self.tile_position_label = tkinter.Label(self.separator, text="")
        #self.tile_position_label.pack()
        self.tile_description = tkinter.Label(self.separator, text="")
        self.tile_description.pack()
        self.last_used_button = 0
        self.pass_time_button = tkinter.Button(self.master, height=2, width=8,
                                        text="PASS TIME",
                                        highlightthickness = 0, bd=0, bg='white',
                                        command=lambda : self.pass_time())
        self.pass_time_button.place(x=20, y=1)


    def make_grid(self):
        self.canvas.delete('all')
        #self.canvas = Canvas(self.master, width=1920, height=1080)
        num_rows = len(self.env.grid)
        num_cols = len(self.env.grid[0])
        x_size = 33
        y_size = 36
        self.master.attributes('-fullscreen', True)
        self.canvas.pack()

        for col in range(1, num_cols + 1):
            for row in range(1, num_rows + 1):
                self.buttons.append(tkinter.Button(self.master, height=2, width=4,
                                        text=self.env.grid[row-1][col-1].get_num_individuals(),
                                        highlightthickness = 0, bd=0, bg='white',
                                        command=lambda row=row,col=col: self.examine_tile(row-1, col-1)))
                self.buttons[-1].pack()
                #self.buttons[row-1][col-1].pack(pady=10)
                rect = self.canvas.create_rectangle(row * x_size, col * y_size,
                                               (row+1) * x_size, (col+1) * y_size,
                                                fill = '#ccc')
                self.buttons[-1].place(x=row * x_size + 1, y=col * y_size + 1)

        self.master.update()

    def examine_tile(self, x, y):
        self.buttons[self.last_used_button].config(bg='white')
        self.last_used_button = y*len(self.env.grid)+x
        self.buttons[y*len(self.env.grid)+x].config(bg='green')
        self.master.update()
        self.tile_description.configure(text=f'{self.env.grid[x][y].get_description()}\n{self.env.last_wanted_position}\n{len(self.env.grid)}, {len(self.env.grid[0])}')

    def update_grid(self):
        self.buttons[self.last_used_button].config(bg='white')
        num_rows = len(self.env.grid)
        num_cols = len(self.env.grid[0])
        for col in range(num_cols):
            for row in range(num_rows):
                self.buttons[col * num_rows + row].config(text=self.env.grid[row][col].get_num_individuals())
                #self.buttons[row * len(self.env.grid) + col].config(text=self.env.grid[row][col].get_num_individuals())
        self.master.update()

    def pass_time(self):
        self.env.pass_time()
        self.update_grid()

    def mainloop(self):
        mainloop()

#if __name__ == '__main__':
#    gui = GUI()
#    gui.make_grid()
#    mainloop()