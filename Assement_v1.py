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

        what_label = Label(frame, text = '''This game is a basic clicker game that works by you the user clicking on the[object] to earn[currency].
        The aim of the game is to try and have more [currency] than other players and be top of the leaderboard!
                           
        To start off you can earn 1 [currency] per click on [object], however once you save up enough [currency] you can go to the store to purchase upgrades.
        From the upgrade store you will be able to purchase upgrades that increase your amount of [currency] earned per click or you could purchase workers 
        that provide you with passive income ''',
                           font = "arial 12")
        what_label.grid(column = 0, row = 1, sticky = "WE", ipadx=20)

        back_button = Button(frame, text = "Back", font = "arial 20 bold",
                             command = lambda: self.show_frame("homepage"))
        back_button.grid(column = 0, row = 2, pady=10)


        return frame
    
    def game_frame(self):
        frame = Frame(self.container)
        frame.grid(row = 0,column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        banner_game = Label(frame, text = "Game", font = "arial 30 bold")
        banner_game.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        clicker = Button(frame, text = "click me", font = "arial 40 bold")
        clicker.grid(column = 0, row = 1, pady = 30)
        

        return frame

    def run(self):
        self.show_frame("homepage")
        self.root.mainloop()

app = Game()
app.run()
