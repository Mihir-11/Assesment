'''
Assement v2
Upgrades and upgrade store in addition to a theme for the game
Tycoon clicker game
Written by Mihir Batra
'''
from tkinter import *

class Game:
    def __init__(self):
        #window
        self.root = Tk()
        self.root.title("Clicker Game")
        self.root.geometry("+500+300")

        #container for frames
        self.container = Frame(self.root)
        self.container.grid(sticky = "NSEW")

        
        #dictionary to hold frames
        self.frames = {}
        self.frames["homepage"] = self.home_frame()
        self.frames["helppage"] = self.help_frame()
        self.frames["gamepage"] = self.game_frame()
        
    def show_frame(self, name):
        '''Method to change which frames the user is seeing and using'''

        frame = self.frames[name]  #sets frame variable to chose frame
        frame.tkraise()  #raises chosen frame to the front

    def home_frame(self):
        '''This method is the design for the home page and returns "frame" which means when this method is called using the show_frame method, 
        this frame will be raised and displayed to the user'''

        #window 
        frame = Frame(self.container)
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)


        #window design
        banner = Label(frame, text = "Clicker Game", font = "arial 30 bold")
        banner.grid(column = 0, row = 0, sticky = "WE", ipadx=20)
        

        button_play = Button(frame, text = "Play", font = "arial 20 bold",
                             command = lambda: self.show_frame("gamepage"))  #gives "gamepage" as name to show_frame method which means when this button is clicked the game frame is raised 
        button_play.grid(column = 0, row = 1, pady = 10)


        button_help = Button(frame, text = "Help", font = "arial 20 bold", 
                             command = lambda: self.show_frame("helppage")) #gives "helppage" as name to show_frame method which means when this button is clicked the help frame is raised
        button_help.grid(column = 0, row = 2, pady = 10)

        return frame

    def help_frame(self):
        '''This method is the design for the help page and returns "frame" which means when this method is called using the show_frame method, 
        this frame will be raised and displayed to the user'''

        #window
        frame = Frame(self.container)
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        #window design
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
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        back_button.grid(column = 0, row = 2, pady=10)


        return frame
    
    def click(self):
            '''This method is used to increase the users currency each time a button is clicked'''
            self.count += 1 #increases count
            self.user_currency_amount.set(self.count) #sets labels textvariable to new count

    def game_frame(self):
        '''This method is the design for the game page and returns "frame" which means when this method is called using the show_frame method, 
        this frame will be raised and displayed to the user'''

        #window
        frame = Frame(self.container)
        frame.grid(row = 0,column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        #setting variables for the users currency count
        self.user_currency_amount = IntVar()
        self.user_currency_amount.set(0)
        self.count = 0
        
        #window design
        user_currency = Label(frame, 
                              textvariable = self.user_currency_amount, #user_currency_amount is set as a text variable so that when the count changes it can be updated in this label
                              font = "arial 30 bold")
        user_currency.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        clicker = Button(frame, text = "click me", font = "arial 40 bold", command = lambda : self.click()) #click method is called meaning that each time this button is clicked currency is added to the users count
        clicker.grid(column = 0, row = 1, pady = 30)

        home_button = Button(frame, text = "Home", font = "arial 20 bold",
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        home_button.grid(column = 0, row = 2,  pady = 20)

        #upgrade store button
        store_button = Button(frame, text = "Upgrade store", font = "arial 20 bold",
                              command = self.popup)
        store_button.grid(column = 1, row = 2,  pady = 20)


        
        return frame
    
    def popup(self):
        '''Method that makes a popup for the upgrade store'''

        #window
        popup = Toplevel(self.root, bg = "lightblue")
        popup.overrideredirect(True)
        popup.title("Upgrade Store")
        popup.geometry("300x200+800+300")


        #window design
        popup_label = Label(popup, text = "Upgrade Store", font = "arial 20 bold")
        popup_label.grid(column = 0, row = 0, sticky = "NSEW")

        upgrade_button = Button(popup, text = "increase currency earned per click", command = self.clickincrease_upgrade)
        upgrade_button.grid(column =0, row = 1)

        close_button = Button(popup, text = "close", command = popup.destroy)
        close_button.grid(column = 0 , row = 3, pady = 20)

    def clickincrease_upgrade(self):

        #window
        click_increase_popup = Toplevel(self.root)

        #window design
        increase_label = Label(click_increase_popup, text = "How much would you like to earn per click:", font = "arial 10 bold")
        increase_label.grid(column = 0, row = 0, sticky = "NSEW")

        entrybox_currencyperclick = Entry(click_increase_popup, borderwidth = 2, relief = "solid") 
        entrybox_currencyperclick.grid(column = 0, row = 1, sticky = "NSEW")

        increaseperclick = entrybox_currencyperclick.get()
        print(increaseperclick)


        

    def run(self):
        '''Method to run program'''
        self.show_frame("homepage")
        self.root.mainloop()

app = Game()
app.run()
