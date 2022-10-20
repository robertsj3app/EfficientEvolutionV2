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


    def make_grid(self):
        self.canvas.delete('all')
        #self.canvas = Canvas(self.master, width=1920, height=1080)
        num_rows = len(self.env.grid)
        num_cols = len(self.env.grid[0])
        x_size = 33
        y_size = 37
        self.master.attributes('-fullscreen', True)
        self.canvas.pack()

        for row in range(1, num_rows + 1):
            for col in range(1, num_cols + 1):
                self.buttons.append(tkinter.Button(self.master, height=2, width=4,
                                        text=self.env.grid[row-1][col-1].get_num_individuals(),
                                        highlightthickness = 0, bd=0, bg='green',
                                        command=lambda row=row,col=col: self.examine_tile(row-1, col-1)))
                self.buttons[-1].pack()
                #self.buttons[row-1][col-1].pack(pady=10)
                rect = self.canvas.create_rectangle(col * x_size, row * y_size,
                                               (col+1) * x_size, (row+1) * y_size,
                                                fill = '#ccc')
                self.buttons[-1].place(x=col * x_size + 1, y=row * y_size + 1)

        self.master.update()

    def examine_tile(self, x, y):
        #self.buttons[x*len(self.env.grid)+y].flash()

        self.buttons[x*len(self.env.grid)+y].config(text='hi')
        self.buttons[x*len(self.env.grid)+y].config(bg='black')
        #self.buttons[x*len(self.env.grid)+y].config(bg='dark green', fg='white')

        self.buttons[x * len(self.env.grid) + y]['text'] = 'hi'
        self.master.update()

        #self.buttons[x][y].pack()
        #self.buttons[x][y].config(text="hi")
        #self.buttons[x][y].flash()
        #self.tile_position_label.configure(text=f'Position: {x}, {y}')
        self.tile_description.configure(text=self.env.grid[x][y].get_description())
        print(self.env.grid[x][y].get_description())


    def mainloop(self):
        mainloop()

#if __name__ == '__main__':
#    gui = GUI()
#    gui.make_grid()
#    mainloop()