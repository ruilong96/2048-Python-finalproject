"""
Filename: interface.py
Author: zhuangr
date: 05/15/2017
"""
import tkinter
# import ttk

Color = {0: "#3a3a3a",2:"#ff694f",4:"#ff574f",8:"#fff34f",
		16: "#7fff8a",32: "#ffa65e",64: "#ffa65e",128: "#ffc15e",
        256: "#7277ff",512: "#e971ff",1024: "#ff4fd8",2048:"#ff4f4f",}

class Graphics():
    "Graphics interface of the game"
    def __init__(self):
        "Constructor of the Game"
        self.root = tkinter.Tk()
        
        self.frame = tkinter.Frame(self.root)

        self.frame.grid()
        self.frame.master.title("2048")
        self.keydown = 0
        self.frame.cells_grid = []
        self.matrix = None

        self.initial_grid()

    def initial_grid(self):
        "initialize a grid and window with cells"
        background = tkinter.Frame(self.frame, bg = "#211f1f", width = 500, height = 500)
        background.grid()

        for r in range(4):
            row_grid = []
            for c in range(4):
                cell = tkinter.Frame(background, bg = Color[0], width = 500//4, height= 500//4)
                cell.grid(row = r, column = c, padx = 10, pady = 10)

                text = tkinter.Label(master = cell, text = "", bg = Color[0], width = 4, height = 2,
                            justify = "center")
                text.grid()
                row_grid.append(text)

            self.frame.cells_grid.append(row_grid)

    def update_cells(self, matrix):
        "update the cell according to the matrix given"
        for r in range(4):
            for c in range(4):
                if matrix[r][c] == 0:
                    self.frame.cells_grid[r][c].configure(text = '', bg = Color[0])
                else:
                    self.frame.cells_grid[r][c].configure(text = str(matrix[r][c]), 
                        bg = Color[matrix[r][c]])


    def update_state(self, state):
        "update the state of game according to the state"
        if state == 1:
            self.frame.cells_grid[1][1].configure(text="You", bg = "white")
            self.frame.cells_grid[1][2].configure(text="Win!", bg= "white")
        elif state == -1: 
            self.frame.cells_grid[1][1].configure(text="You", bg = "white")
            self.frame.cells_grid[1][2].configure(text="lose!", bg= "white")

    def startmainloop(self, mat):
        "mainloop the interface and the function"
        self.matrix = mat
        
        def key(event):
            "capture the key and react according to the key stroke"
            choice = event.char

            matrix = self.matrix.mat
            if choice == "w":
                self.matrix.upward()
            elif choice == "s":
                self.matrix.downward()
            elif choice == "a":
                self.matrix.leftward()
            elif choice == "d":
                self.matrix.rightward()
            if self.matrix.checker() < 16 and matrix != self.matrix.mat:
                self.matrix.random_update()
            self.update_cells(self.matrix.mat)

            if self.matrix.game_state() == -1:
                self.update_state(self.matrix.game_state())
            elif self.matrix.game_state() == 1:
                self.update_state(self.matrix.game_state())

            self.frame.focus_set()
    
        self.frame.bind("<Key>", key)
        self.frame.focus_set()
        self.frame.pack()
        
        self.root.mainloop()
            




        
        
