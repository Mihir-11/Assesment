'''
Assement v3
Fully Validated and saves users information
Tycoon clicker game
Written by Mihir Batra
'''

from tkinter import *
from PIL import Image, ImageTk
import json

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
        self.frames["loginpage"] = self.login_frame()
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
        
        #images
        #logo image
        logo_title = Image.open("logo.png")
        logo_resized = logo_title.resize((400,400), Image.LANCZOS)
        logo_final = ImageTk.PhotoImage(logo_resized)

        #Button
        donut_image = Image.open("donut_button.png")
        donut_resized = donut_image.resize((300,300), Image.LANCZOS)
        donut_final = ImageTk.PhotoImage(donut_resized)

        #dictionary for images
        self.images = {"logo":logo_final, "donut":donut_final}


        #window design
        banner = Label(frame, image = self.images["logo"])
        banner.grid(column = 0, row = 0)
        

        button_play = Button(frame, text = "Play", font = "arial 20 bold",
                             command = lambda: self.show_frame("loginpage"))  #gives "loginpage" as name to show_frame method which means when this button is clicked the game frame is raised 
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
        banner_help = Label(frame, text = "Welcome to Donut Clicker!", font = "arial 30 bold")
        banner_help.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        what_label = Label(frame, text = '''This game is a basic clicker game that works by you the user clicking on the big donut to earn sprinkles.
        The aim of the game is to try and have more sprinkles than other players and be top of the leaderboard!
                           
        To start off you can earn 1 sprinkle per click on the donut, however once you save up enough sprinkles you can go to the store to purchase upgrades.
        From the upgrade store you will be able to purchase upgrades that increase your amount of sprinkles earned per click or you could purchase workers 
        that provide you with a passive income of sprinkles''',
                           font = "arial 12")
        what_label.grid(column = 0, row = 1, sticky = "WE", ipadx=20)

        back_button = Button(frame, text = "Back", font = "arial 20 bold",
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        back_button.grid(column = 0, row = 2, pady=10)


        return frame
    

    def login(self):
        with open("donut_clicker_users.json") as file:
            users = json.load(file)
        username = self.username_box.get()
        pass_to_check = self.password_box.get()

        if username in users and users[username]["password"] == pass_to_check:
            self.clickamount = users[username]["click_upgrade"]
            self.user_worker_amount = users[username]["worker_amount"]

            for worker in range(self.user_worker_amount):
                self.worker()
            self.show_frame("gamepage")
        else:
            self.incorrect_label.configure(text = "Incorrect username or password")



    
    def login_frame(self):
        #window
        frame = Frame(self.container)
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(1, weight =1)
        frame.grid_columnconfigure(0, weight =1)

        #window design
        banner_login = Label(frame, text = "Login to Donut Clicker", font = "arial 30 bold")
        banner_login.grid(column = 0, row = 0, sticky = "NSEW", ipadx=20, pady = 60,columnspan = 2)
        

        username_label = Label(frame, text = "Username", font = "arial 20 bold")
        username_label.grid(column = 0, row = 1, sticky = "WE", ipadx=10)

        self.username_box = Entry(frame, borderwidth = 2, relief = "solid")
        self.username_box.grid(column = 1, row = 1, ipadx=10, sticky = "W")

        password_label = Label(frame, text = "Password", font = "arial 20 bold")
        password_label.grid(column = 0, row = 2, sticky = "WE", ipadx=10)

        self.password_box = Entry(frame, borderwidth = 2, relief = "solid")
        self.password_box.grid(column = 1, row = 2, ipadx=10, sticky = "W")

        login_button = Button(frame, text = "Login", font = "arial 20 bold", command = lambda: self.login())
        login_button.grid(column = 0, row = 3, ipadx=20, pady = 10,columnspan = 2)

        back_button = Button(frame, text = "Back", font = "arial 20 bold",
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        back_button.grid(column = 0, row = 4, ipadx=20, pady = 10, columnspan = 2)

        
        self.incorrect_label = Label(frame, text = "", font = "arial 20 bold")
        self.incorrect_label.grid(column = 0, row = 5, ipadx=20, pady = 40,columnspan = 2)

        return frame
    
    def click(self):
            '''This method is used to increase the users sprinkles each time a button is clicked'''
            self.count += self.clickamount#increases count
            self.user_sprinkles_amount.set(self.count) #sets labels textvariable to new count

    def game_frame(self):
        '''This method is the design for the game page and returns "frame" which means when this method is called using the show_frame method, 
        this frame will be raised and displayed to the user'''

        #window
        frame = Frame(self.container)
        frame.grid(row = 0,column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        #setting variables for the users sprinkles count
        self.user_sprinkles_amount = IntVar()
        self.count = 0
        self.user_sprinkles_amount.set(self.count)
        
        
        #window design
        user_sprinkles = Label(frame, 
                              textvariable = self.user_sprinkles_amount, #user_sprinkles_amount is set as a text variable so that when the count changes it can be updated in this label
                              font = "arial 30 bold")
        user_sprinkles.grid(column = 0, row = 0, sticky = "WE", ipadx=20)


        clicker = Button(frame, image = self.images["donut"], borderwidth = 0,
                         command = lambda : self.click()) #click method is called meaning that each time this button is clicked sprinkles is added to the users count
        clicker.grid(column = 0, row = 1, pady = 30)

        home_button = Button(frame, text = "Home", font = "arial 20 bold",
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        home_button.grid(column = 0, row = 2,  pady = 20)


        #upgrade store button
        store_button = Button(frame, text = "Upgrade store", font = "arial 20 bold",
                              command = self.popup)
        store_button.grid(column = 1, row = 3,  pady = 20)

        return frame
    
  
    def popup(self):
        '''Method that makes a popup for the upgrade store'''

        #window
        popup = Toplevel(self.root, bg = "lightblue", borderwidth = 2, relief = "solid")
        popup.overrideredirect(True)
        popup.title("Upgrade Store")
        popup.grid_columnconfigure(0, weight =1)
        popup.geometry("300x200+1100+350")


        #window design
        popup_label = Label(popup, text = "Upgrade Store", font = "arial 20 bold", bg = "lightblue")
        popup_label.grid(column = 0, row = 0, sticky = "NSEW")

        upgrade_button1 = Button(popup, text = "increase sprinkles earned per click", command = self.clickincrease_upgrade)
        upgrade_button1.grid(column = 0, row = 1, pady = 5)

        upgrade_button2 = Button(popup, text = "purchase workers", command = self.worker_upgrade)
        upgrade_button2.grid(column = 0, row = 2, pady = 5)

        close_button = Button(popup, text = "close", command = popup.destroy)
        close_button.grid(column = 0 , row = 3, pady = 20)
    
    #-----------------------------------------------CLICK INCREASE UPGRADE-------------------------------------------------------
    def clickincrease_upgrade(self):
        #window
        self.click_increase_popup = Toplevel(self.root)

        #window design
        increase_label = Label(self.click_increase_popup, text = "How much would you like to earn per click:", font = "arial 10 bold")
        increase_label.grid(column = 0, row = 0, sticky = "NSEW")

        self.entrybox_sprinklesperclick = Entry(self.click_increase_popup, borderwidth = 2, relief = "solid") 
        self.entrybox_sprinklesperclick.grid(column = 0, row = 1, sticky = "NSEW")

        earn_per_click_label = Label(self.click_increase_popup, text = f"current sprinkles earned per click: {self.clickamount}", font = "arial 10 ")
        earn_per_click_label.grid(column = 0, row = 2, sticky = "NSEW")

        self.cost_label = Label(self.click_increase_popup, text = "", font = "arial 10 ")
        self.cost_label.grid(column = 0, row = 3, sticky = "NSEW")

        enter_button = Button(self.click_increase_popup, text = "enter", command = lambda: self.cost_click())
        enter_button.grid(column = 0, row = 4, sticky = "NSEW")
    
    def cost_click(self):
        #variables
        self.cost_amount = int(self.entrybox_sprinklesperclick.get())*10
        self.user_balance = int(self.user_sprinkles_amount.get())

        if int(self.entrybox_sprinklesperclick.get()) <= self.clickamount:
            self.cost_label.configure(text = "cannot enter a value lower than or equal to previous upgrade")
        
        else:
            self.cost_label.configure(text = f"This will cost {self.cost_amount} sprinkles")
            self.confirm_button = Button(self.click_increase_popup, text = "confirm", command = lambda: self.set_click())
            self.confirm_button.grid(column = 0, row = 5, sticky = "NSEW")
        
    def set_click(self):
        #variables
        self.cost_amount = int(self.entrybox_sprinklesperclick.get())*10
        self.user_balance = int(self.user_sprinkles_amount.get())

        if  self.user_balance < self.cost_amount:
            self.cost_label.configure(text = "Insufficient Funds")
            self.confirm_button.destroy() 

        elif int(self.entrybox_sprinklesperclick.get()) <= self.clickamount:
            self.cost_label.configure(text = "cannot enter a value lower than or equal to previous upgrade")
            self.confirm_button.destroy() 
        
        else:
            self.clickamount = int(self.entrybox_sprinklesperclick.get())
            self.count = self.user_balance-self.cost_amount
            self.user_sprinkles_amount.set(self.count)
            self.click_increase_popup.destroy()
    #-----------------------------------------------------------------------------------------------------------------------------


    #-----------------------------------------------WORKER INCREASE UPGRADE-------------------------------------------------------
    def worker_upgrade(self):
        #variables
        self.worker_level = self.user_worker_amount +1 #worker level is one higher than the amount of workers the user has
        self.worker_cost = ( self.worker_level * 5)**2
        self.user_balance = int(self.user_sprinkles_amount.get())

         #window
        self.worker_upgrade_popup = Toplevel(self.root)

        #window design
        self.worker_price_label = Label(self.worker_upgrade_popup, text = f"Next worker will cost {self.worker_cost} sprinkles")
        self.worker_price_label.grid(column = 0, row = 0, sticky = "NSEW")

        purchase_worker = Button(self.worker_upgrade_popup, text = "Purchase", font = "arial 10 bold", command = lambda: self.purchase_worker())
        purchase_worker.grid(column = 0, row = 1, sticky = "NSEW")

    def purchase_worker(self):
        if self.worker_cost > self.user_balance:
            self.worker_price_label.configure(text = "Insufficient Funds")
        else:
            self.worker_upgrade_popup.destroy()
            self.count = self.user_balance-self.worker_cost
            self.user_sprinkles_amount.set(self.count)
            self.user_worker_amount += 1
            self.worker()

    def worker(self):
        self.click()
        self.root.after(1000,self.worker)

    #-----------------------------------------------------------------------------------------------------------------------------
    


    def run(self):
        '''Method to run program'''
        self.show_frame("homepage")
        self.root.mainloop()


app = Game()
app.run()


    
    
