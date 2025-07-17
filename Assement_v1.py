'''
Assement v1
Tycoon clicker game
Written by Mihir Batra
'''
from tkinter import *

class Game:
    def __init__(self):
        #window
        self.root = Tk()
        self.root.title("Clicker Game")

        #window design
        banner = Label(self.root, text = "Clicker Game", font = "arial 30 bold")
        banner.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        button_play = Button(self.root, text = "Play", font = "arial 20 bold")
        button_play.grid(column = 0, row = 1, pady = 10)
        button_help = Button(self.root, text = "Help", font = "arial 20 bold")
        button_help.grid(column = 0, row = 2, pady = 10)

        #container for frames
        self.container = Frame(self.root)
        self.container.grid(sticky = "NSEW")

        #dictionary to hold frames
        #self.frames = {}
        #self.frames["homepage"] = self.home_frame()
        #self.frames["gamepage"] = self.game_frame()
        #self.frames["helppage"] = self.help_frame()





    
    def run(self):
        self.root.mainloop()

app = Game()
app.run()
