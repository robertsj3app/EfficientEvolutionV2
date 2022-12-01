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
        self.map_mode = True
        self.tile_canvas = Canvas(self.master, width = 192, height=108)
        self.buttons = []
        self.separator = ttk.Separator(self.master, orient='vertical')
        self.separator.place(relx=0.5, rely=0, relwidth=0.2, relheight=1)
        #self.tile_position_label = tkinter.Label(self.separator, text="")
        #self.tile_position_label.pack()
        self.tile_description = tkinter.Label(self.separator, text="")
        self.tile_description.pack()
        self.last_used_button = -1
        self.last_used_position = (-1,-1)
        self.current_position = (-1,-1)
        self.generation_num = 1
        self.pass_time_button = tkinter.Button(self.master, height=2, width=8,
                                        text="PASS TIME",
                                        highlightthickness = 0, bd=0, bg='white',
                                        command=lambda : self.pass_time())
        self.pass_time_button.place(x=112, y=1)
        self.back_time_button = tkinter.Button(self.master, height=2, width=8,
                                        text="BACK TIME",
                                        highlightthickness = 0, bd=0, bg='white',
                                        command=lambda : self.back_time())
        self.back_time_button.place(x=32, y=1)
        self.turn_label = tkinter.Label(self.master, height=2,
                                         text=f"TURN: {self.env.turn}")
        self.turn_label.place(x=192, y=0)
        self.block_label = tkinter.Label(self.master, height=2, width=20, text='Map Editor Mode')
        self.block_label.place(x=32,y=0)
        self.block_label.destroy()
        self.update_tile_button = tkinter.Button(self.separator, height=2, width=8,
                                                 text='Update', bg='white',
                                                 command=lambda : self.update_tile())
        self.update_tile_button.place(x=150, y=450)
        self.copy_button = tkinter.Button(self.separator, height=2, width=8,
                                          text='Copy', bg='white',
                                          command=lambda : self.copy_tile())
        self.copy_button.place(x=100, y=250)
        self.paste_button = tkinter.Button(self.separator, height=2, width=8,
                                          text='Paste', bg='white',
                                          command=lambda: self.paste_tile())
        self.generation_num_label = tkinter.Label(self.master, text=f'GENERATION # {self.generation_num}', height=2, width=14)
        self.generation_num_label.place(x=272, y=0)
        self.start_button = tkinter.Button(self.master, height=2, width=14,
                                               text="START SIM",
                                               highlightthickness=0, bd=0, bg='white',
                                               command=lambda: self.start_sim())
        self.start_button.place(x=272, y=1)
        self.next_generation_button = None
        self.edit_label = tkinter.Label(self.master, height=2, width=20, text='EDITOR MODE')
        self.edit_label.place(x=32, y=0)
        self.paste_button.place(x=190, y=250)
        self.food_entry = tkinter.Entry(self.separator, width=4)
        self.food_entry.place(x=150, y=300)
        self.hazard_entry = tkinter.Entry(self.separator, width=4)
        self.hazard_entry.place(x=150, y=350)
        self.water_entry = tkinter.Entry(self.separator, width=4)
        self.water_entry.place(x=150, y=400)
        self.food_label = tkinter.Label(self.separator, text='Food:')
        self.food_label.place(x=100,y=300)
        self.hazard_label = tkinter.Label(self.separator, text='Hazard:')
        self.hazard_label.place(x=100, y=350)
        self.water_label = tkinter.Label(self.separator, text='Water:')
        self.water_label.place(x=100, y=400)
        self.food_copy = -1
        self.hazard_copy = -1
        self.water = -1

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
        self.update_grid()

    def start_sim(self):
        self.edit_label.destroy()
        self.copy_button.destroy()
        self.paste_button.destroy()
        self.update_tile_button.destroy()
        self.start_button.destroy()

    def examine_tile(self, x, y):
        self.current_position = (x, y)
        self.food_entry.delete(0, END)
        self.hazard_entry.delete(0, END)
        self.water_entry.delete(0, END)
        self.food_entry.insert(0, str(self.env.grid[x][y].attributes['Food']))
        self.hazard_entry.insert(0, str(self.env.grid[x][y].attributes['Hazard']))
        self.water_entry.insert(0, str(self.env.grid[x][y].attributes['Water']))
        first_examine = False
        if self.last_used_button != -1:
            self.buttons[self.last_used_button].config(bg='white')
            if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Food"] > 0:
                self.buttons[self.last_used_button].config(bg='green')
            if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Water"] > 0:
                if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Food"] > 0:
                    self.buttons[self.last_used_button].config(bg='turquoise')
                else:
                    self.buttons[self.last_used_button].config(bg='blue')
            if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Hazard"] > 0:
                self.buttons[self.last_used_button].config(bg='red')
        self.last_used_button = y*len(self.env.grid)+x
        self.last_used_position = (x, y)
        self.buttons[y*len(self.env.grid)+x].config(bg='orange')
        self.master.update()
        self.tile_description.configure(text=f'{self.env.grid[x][y].get_description()}')
        #\n{self.env.last_wanted_position}\n{len(self.env.grid)}, {len(self.env.grid[0])}')

    def update_grid(self):
        self.buttons[self.last_used_button].config(bg='white')
        if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Food"] > 0:
            self.buttons[self.last_used_button].config(bg='green')
        if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Water"] > 0:
            if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Food"] > 0:
                self.buttons[self.last_used_button].config(bg='turquoise')
            else:
                self.buttons[self.last_used_button].config(bg='blue')
        if self.env.grid[self.last_used_position[0]][self.last_used_position[1]].attributes["Hazard"] > 0:
            self.buttons[self.last_used_button].config(bg='red')
        num_rows = len(self.env.grid)
        num_cols = len(self.env.grid[0])
        for col in range(num_cols):
            for row in range(num_rows):
                self.buttons[col * num_rows + row].config(text=self.env.grid[row][col].get_num_individuals())
                self.buttons[col * num_rows + row].config(bg='white')
                if self.env.grid[row][col].attributes["Food"] > 0:
                    self.buttons[col * num_rows + row].config(bg='green')
                if self.env.grid[row][col].attributes["Water"] > 0:
                    if self.env.grid[row][col].attributes["Food"] > 0:
                        self.buttons[col * num_rows + row].config(bg='turquoise')
                    else:
                        self.buttons[col * num_rows + row].config(bg='blue')
                if self.env.grid[row][col].attributes["Hazard"] > 0:
                    self.buttons[col * num_rows + row].config(bg='red')
                #self.buttons[row * len(self.env.grid) + col].config(text=self.env.grid[row][col].get_num_individuals())
        self.turn_label.config(text=f"TURN: {self.env.turn}")
        self.master.update()

    def update_tile(self):
        self.env.grid[self.current_position[0]][self.current_position[1]].attributes['Food'] = int(self.food_entry.get())
        self.env.grid[self.current_position[0]][self.current_position[1]].attributes['Hazard'] = int(self.hazard_entry.get())
        self.env.grid[self.current_position[0]][self.current_position[1]].attributes['Water'] = int(self.water_entry.get())
        #self.update_grid()
        self.examine_tile(self.current_position[0], self.current_position[1])

    def next_generation(self):
        self.generation_num += 1
        self.generation_num_label.config(text=f'GENERATION #: {self.generation_num}')
        self.next_generation_button.destroy()
        self.next_generation_button = None
        self.env.next_generation()
        self.update_grid()

    def copy_tile(self):
        self.food_copy = self.food_entry.get()
        self.hazard_copy = self.hazard_entry.get()
        self.water_copy = self.water_entry.get()

    def paste_tile(self):
        self.food_entry.delete(0, END)
        self.hazard_entry.delete(0, END)
        self.water_entry.delete(0, END)
        self.food_entry.insert(0, self.food_copy)
        self.hazard_entry.insert(0, self.hazard_copy)
        self.water_entry.insert(0, self.water_copy)

    def pass_time(self):
        self.env.pass_time()
        if self.next_generation_button is None:
            if len(self.env.generation.living_individuals) == 0:
                self.next_generation_button = tkinter.Button(self.master, height=2, width=16,
                                               text="NEXT GENERATION",
                                               highlightthickness=0, bd=0, bg='white',
                                               command=lambda: self.next_generation())
                self.next_generation_button.place(x=412, y=1)
        self.update_grid()

    def back_time(self):
        self.env.back_time()
        self.update_grid()

    def mainloop(self):
        mainloop()

#if __name__ == '__main__':
#    gui = GUI()
#    gui.make_grid()
#    mainloop()