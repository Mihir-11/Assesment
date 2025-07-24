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
       

        #container for frames
        self.container = Frame(self.root)
        self.container.grid(sticky = "NSEW")

        
        #dictionary to hold frames
        self.frames = {}
        self.frames["homepage"] = self.home_frame()
        self.frames["helppage"] = self.help_frame()
        self.frames["gamepage"] = self.game_frame()
        

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def home_frame(self):
        frame = Frame(self.container)
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)


        banner = Label(frame, text = "Clicker Game", font = "arial 30 bold")
        banner.grid(column = 0, row = 0, sticky = "WE", ipadx=20)
        

        button_play = Button(frame, text = "Play", font = "arial 20 bold",
                             command = lambda: self.show_frame("gamepage"))
        button_play.grid(column = 0, row = 1, pady = 10)

        button_help = Button(frame, text = "Help", font = "arial 20 bold", 
                             command = lambda: self.show_frame("helppage"))
        button_help.grid(column = 0, row = 2, pady = 10)

        return frame


    def help_frame(self):
        frame = Frame(self.container)
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        banner_help = Label(frame, text = "Welcome to [Game name]!", font = "arial 30 bold")
        banner_help.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        return frame
    
    def game_frame(self):
        frame = Frame(self.container)
        frame.grid(row = 0,column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        banner_game = Label(frame, text = "Game", font = "arial 30 bold")
        banner_game.grid(row = 0, column = 0,sticky = "WE", ipadx=20)
        

        return frame

    def run(self):
        self.show_frame("homepage")
        self.root.mainloop()

app = Game()
app.run()
