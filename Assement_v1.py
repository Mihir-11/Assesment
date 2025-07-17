'''
Assement v1
Tycoon clicker game
Written by Mihir Batra
'''
from tkinter import *
from tkinter import ttk

class Game:
    def __init__(self):
        #window
        self.root = Tk()
        self.root.title("Clicker Game")

        #window design
        banner = Label(self.root, text = "Clicker Game", font = "arial 30 bold")
        banner.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        button_play = Button(self.root, text = "Play", font = "arial 20 bold")
        button_play.grid(column = 0, row = 1, pady = 20)





    
    def run(self):
        self.root.mainloop()

app = Game()
app.run()
