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
        self.root.resizable(0,0)

        #variables
        self.clickamount = 0
        self.user_worker_amount = 0
        self.count = 0

        with open("donut_clicker_users.json") as file: #opens json file with all users 
            self.users = json.load(file)
        

        #container for frames
        self.container = Frame(self.root)
        self.container.grid(sticky = "NSEW")

        
        #dictionary to hold frames
        self.frames = {}
        self.frames["homepage"] = self.home_frame()
        self.frames["helppage"] = self.help_frame()
        self.frames["loginpage"] = self.login_frame()
        self.frames["createpage"] = self.new_account_frame()
        self.frames["gamepage"] = self.game_frame()

        
   #-----------------------------------------------FRAMES------------------------------------------------------- 
    def show_frame(self, name):
        '''Method to change which frames the user is seeing and using'''

        frame = self.frames[name]  #sets frame variable to chose frame
        frame.tkraise()  #raises chosen frame to the front

        #clears entry boxes on login page
        self.username_box.delete(0,END)
        self.password_box.delete(0,END)

    def home_frame(self):
        '''This method is the design for the home page and returns "frame" which means when this method is called using the show_frame method, 
        this frame will be raised and displayed to the user'''

        #window 
        frame = Frame(self.container, bg = "lightblue")
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)
        
        #images
        #logo image
        logo_title = Image.open("logo.png")
        logo_resized = logo_title.resize((400,400), Image.LANCZOS)
        logo_final = ImageTk.PhotoImage(logo_resized)

        #sprinkles
        sprinkles_1 = Image.open("sprinkles_1.png")
        sprinkles_1_resized = sprinkles_1.resize((100,100), Image.LANCZOS)
        sprinkles_1_final = ImageTk.PhotoImage(sprinkles_1_resized)

        #Button image
        donut_image = Image.open("donut_button.png")
        donut_resized = donut_image.resize((300,300), Image.LANCZOS)
        donut_final = ImageTk.PhotoImage(donut_resized)

        #dictionary for images
        self.images = {"logo":logo_final, "donut":donut_final, "sprinkles_1":sprinkles_1_final}


        #window design
        banner = Label(frame, image = self.images["logo"],bg = "lightblue")
        banner.grid(column = 0, row = 0)
        

        button_play = Button(frame, text = "Play", font = "arial 20 bold", bg = "lightpink" , relief = "solid", 
                             command = lambda: self.show_frame("loginpage"))  #gives "loginpage" as name to show_frame method which means when this button is clicked the game frame is raised 
        button_play.grid(column = 0, row = 1, pady = 10)


        button_help = Button(frame, text = "How to Play", font = "arial 20 bold", bg = "lightpink" , relief = "solid", 
                             command = lambda: self.show_frame("helppage")) #gives "helppage" as name to show_frame method which means when this button is clicked the help frame is raised
        button_help.grid(column = 0, row = 2, pady = 10)

        return frame

    def help_frame(self):
        '''This method is the design for the help page and returns "frame" which means when this method is called using the show_frame method, 
        this frame will be raised and displayed to the user'''

        #window
        frame = Frame(self.container, bg = "lightblue")
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        #window design
        banner_help = Label(frame, text = "Welcome to Donut Clicker!", font = "arial 30 bold", bg = "lightblue")
        banner_help.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        what_label = Label(frame, text = '''This game is a basic clicker game that works by you the user clicking on the big donut to earn sprinkles.
        The aim of the game is to try and have more sprinkles than other players and be top of the leaderboard!
                           
        To start off you can earn 1 sprinkle per click on the donut, however once you save up enough sprinkles you can go to the store to purchase upgrades.
        From the upgrade store you will be able to purchase upgrades that increase your amount of sprinkles earned per click or you could purchase workers 
        that provide you with a passive income of sprinkles''',
                           font = "arial 12", bg = "lightblue")
        what_label.grid(column = 0, row = 1, sticky = "WE", ipadx=20)

        back_button = Button(frame, text = "Back", font = "arial 20 bold", bg = "lightpink" , relief = "solid",
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        back_button.grid(column = 0, row = 2, pady=10)


        return frame

    def login_frame(self):
        '''This method is creating the login frame for the user to login '''

        #window
        frame = Frame(self.container, bg = "lightblue")
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(1, weight =1)
        frame.grid_columnconfigure(0, weight =1)


        #window design
        banner_login = Label(frame, text = "Login to Donut Clicker", font = "arial 30 bold", bg = "lightblue")
        banner_login.grid(column = 0, row = 0, sticky = "NSEW", ipadx=20, pady = 60,columnspan = 2)
        

        username_label = Label(frame, text = "Username", font = "arial 20 bold", bg = "lightblue")
        username_label.grid(column = 0, row = 1, sticky = "WE", ipadx=10)

        self.username_box = Entry(frame, borderwidth = 2, relief = "solid")
        self.username_box.grid(column = 1, row = 1, ipadx=10, sticky = "W")

        password_label = Label(frame, text = "Password", font = "arial 20 bold", bg = "lightblue")
        password_label.grid(column = 0, row = 2, sticky = "WE", ipadx=10)

        self.password_box = Entry(frame, borderwidth = 2, relief = "solid", show ="*")
        self.password_box.grid(column = 1, row = 2, ipadx=10, sticky = "W")

        login_button = Button(frame, text = "Login", font = "arial 20 bold", bg = "lightpink" , relief = "solid", command = lambda: self.login()) #when clicked it initiates the login method
        login_button.grid(column = 0, row = 3, ipadx=20, pady = 10,columnspan = 2)

        home_button = Button(frame, text = "Home", font = "arial 20 bold", bg = "lightpink" , relief = "solid",
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        home_button.grid(column = 0, row = 4, ipadx=20, pady = 10, columnspan = 2)
  
        self.incorrect_label = Label(frame, text = "", font = "arial 20 bold", bg = "lightblue")
        self.incorrect_label.grid(column = 0, row = 5, ipadx=20, pady = 40,columnspan = 2)

        create_account_button = Button(frame, text = "Create New Account", font = "arial 20 bold", bg = "lightpink" , relief = "solid", command = lambda: self.show_frame("createpage"))
        create_account_button.grid(column = 0, row = 6, ipadx=20, pady = 20, columnspan = 2)

        return frame

    def game_frame(self):
        '''This method is the design for the game page and returns "frame" which means when this method is called using the show_frame method, 
        this frame will be raised and displayed to the user'''

        #window
        frame = Frame(self.container, bg = "lightblue")
        frame.grid(row = 0,column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(0, weight =1)

        #setting variables for the users sprinkles count
        self.user_sprinkles_amount = IntVar()
        
        #window design
        user_sprinkles = Label(frame, 
                              textvariable = self.user_sprinkles_amount, #user_sprinkles_amount is set as a text variable so that when the count changes it can be updated in this label
                              font = "arial 30 bold", bg = "lightblue")
        user_sprinkles.grid(column = 0, row = 0, sticky = "WE", ipadx=20)

        sprinkles_image = Label(frame, image = self.images["sprinkles_1"],
                              font = "arial 30 bold", bg = "lightblue")
        sprinkles_image.grid(column = 1, row = 0, sticky = "WE", ipadx=20)


        clicker = Button(frame, image = self.images["donut"], borderwidth = 0, bg = "lightblue", activebackground= "lightblue", #stops the background from changing 
                         command = lambda : self.click()) #click method is called meaning that each time this button is clicked sprinkles is added to the users count
        clicker.grid(column = 0, row = 1, pady = 30)

        leaderboard_button = Button(frame, text = "Leaderboard", font = "arial 30 bold", bg = "lightpink" , relief = "solid", command = self.display_top_players)
        leaderboard_button.grid(column = 0, row = 2, ipadx=20)

        #save button
        save_button = Button(frame, text = "Save & Quit", font = "arial 20 bold", bg = "lightpink" , relief = "solid",command = self.quit)
        save_button.grid(column = 1, row = 3,  pady = 10)


        #upgrade store button
        store_button = Button(frame, text = "Upgrade store", font = "arial 20 bold", bg = "lightpink" , relief = "solid",
                              command = self.popup)
        store_button.grid(column = 1, row = 4,  pady = 10)

        return frame
    
    def new_account_frame(self):
        '''This method is creating the login frame for the user to login '''

        #window
        frame = Frame(self.container, bg = "lightblue")
        frame.grid(row= 0, column = 0, sticky = "NSEW")
        frame.grid_columnconfigure(1, weight =1)
        frame.grid_columnconfigure(0, weight =1)


        #window design
        banner_login = Label(frame, text = "Create Account", font = "arial 30 bold", bg = "lightblue")
        banner_login.grid(column = 0, row = 0, sticky = "NSEW", ipadx=20, pady = 60,columnspan = 2)
        

        username_label = Label(frame, text = "Username", font = "arial 20 bold", bg = "lightblue")
        username_label.grid(column = 0, row = 1, sticky = "WE", ipadx=10)

        self.new_username_box = Entry(frame, borderwidth = 2, relief = "solid")
        self.new_username_box.grid(column = 1, row = 1, ipadx=10, sticky = "W")

        password_label = Label(frame, text = "Password", font = "arial 20 bold", bg = "lightblue")
        password_label.grid(column = 0, row = 2, sticky = "WE", ipadx=10)

        self.new_password_box = Entry(frame, borderwidth = 2, relief = "solid", show ="*")
        self.new_password_box.grid(column = 1, row = 2, ipadx=10, sticky = "W")

        create_button = Button(frame, text = "Create", font = "arial 20 bold", bg = "lightpink" , relief = "solid", 
                               command = lambda: self.new_user()) #when clicked it initiates the new_user() method
        create_button.grid(column = 0, row = 3, ipadx=20, pady = 10,columnspan = 2)

        self.create_label = Label(frame, text = "", font = "arial 20 bold", bg = "lightblue")
        self.create_label.grid(column = 0, row = 5, ipadx=20, pady = 40,columnspan = 2)

        home_button = Button(frame, text = "Home", font = "arial 20 bold", bg = "lightpink" , relief = "solid",
                             command = lambda: self.show_frame("homepage"))  #gives "homepage" as name to show_frame method which means when this button is clicked the home frame is raised
        home_button.grid(column = 0, row = 4, ipadx=20, pady = 10, columnspan = 2)

        login_page_button = Button(frame, text = "Login Page", font = "arial 20 bold", command = lambda: self.show_frame("loginpage"))
        login_page_button.grid(column = 0, row = 6, ipadx=20, pady = 20, columnspan = 2)

        return frame
    
   
        self.username = self.new_username_box.get()
        password = self.new_password_box.get()
        if self.username in self.users:
            self.create_label.configure(text = "username already exists")
        else:
            self.users[self.username] = {
                "password": password,
                "click_upgrade": 1,
                "worker_amount": 0,
                "user_sprinkles": 0
            }
            with open("donut_clicker_users.json", "w") as file:
                json.dump(self.users, file, indent = 4) #saves information to json file

            self.clickamount = self.users[self.username]["click_upgrade"] #sprinkles per click
            self.user_worker_amount = self.users[self.username]["worker_amount"] #amount of workers
            self.count = self.users[self.username]["user_sprinkles"] #users sprinkle balance
            self.user_sprinkles_amount.set(self.count) #sets the display of sprinkles on the game page
    
            self.create_label.configure(text = "Account Created Succesfully!")
            self.show_frame("gamepage")
    
    #-------------------------------------------------------------------------------------------------------------


    #-----------------------------------------------CLICK INCREASE UPGRADE-------------------------------------------------------
    def clickincrease_upgrade(self):
        '''This method creates a popup for the user to increase their sprinkles earned per click'''

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

        enter_button = Button(self.click_increase_popup, text = "Calculate Cost", command = lambda: self.cost_click()) #when clicked initiates the cost_click method
        enter_button.grid(column = 0, row = 4, sticky = "NSEW")
    
    def cost_click(self):
        '''This method is used to show the user how much the upgraade will cost '''
        
        if self.entrybox_sprinklesperclick.get().isdigit():
            #variables
            self.cost_amount = int(self.entrybox_sprinklesperclick.get())*10 #cost of the upgrade
            self.user_balance = int(self.user_sprinkles_amount.get()) #users balance

        
            if int(self.entrybox_sprinklesperclick.get()) <= self.clickamount: #checks value entered is not lower than previous upgrade
                self.cost_label.configure(text = "cannot enter a value lower than or equal to previous upgrade")
            
            else:
                self.cost_label.configure(text = f"This will cost {self.cost_amount} sprinkles") #tells user cost of sprinkles
                self.confirm_button = Button(self.click_increase_popup, text = "Purchase", command = lambda: self.set_click()) #creates confirm button
                self.confirm_button.grid(column = 0, row = 5, sticky = "NSEW")
        else:
             self.cost_label.configure(text = "please enter a number")

        
    def set_click(self):
        '''Method is used to set the users new upgrade'''
        if self.entrybox_sprinklesperclick.get().isdigit():
            #variables
            self.cost_amount = int(self.entrybox_sprinklesperclick.get())*10 #sets cost amount again incase user changes entered value
            self.user_balance = int(self.user_sprinkles_amount.get()) #sets balance again

            if  self.user_balance < self.cost_amount: #checks user can afford upgrade
                self.cost_label.configure(text = "Insufficient Funds")
                self.confirm_button.destroy() 

            elif int(self.entrybox_sprinklesperclick.get()) <= self.clickamount: #checks value is not lower than previous upgrade again
                self.cost_label.configure(text = "cannot enter a value lower than or equal to previous upgrade")
                self.confirm_button.destroy() 
            
            else:#if value is valid then program sets up new upgrade
                self.clickamount = int(self.entrybox_sprinklesperclick.get()) #sets users new sprinkles per click
                self.count = self.user_balance-self.cost_amount #removes cost from balance 
                self.user_sprinkles_amount.set(self.count) #shows new balance
                self.click_increase_popup.destroy() #closes popup
        else: 
            self.cost_label.configure(text = "please enter a number")

    #-----------------------------------------------------------------------------------------------------------------------------


    #-----------------------------------------------WORKER INCREASE UPGRADE-------------------------------------------------------
    def worker_upgrade(self):
        '''This method creates popup frame for the worker upgrade'''

        #variables
        self.worker_level = self.user_worker_amount +1 #worker level is one higher than the amount of workers the user has
        self.worker_cost = ( self.worker_level * 5)**2 #cost of next worker
        self.user_balance = int(self.user_sprinkles_amount.get()) #users sprinkle balance

         #window
        self.worker_upgrade_popup = Toplevel(self.root)

        #window design
        self.worker_price_label = Label(self.worker_upgrade_popup, text = f"Next worker will cost {self.worker_cost} sprinkles")
        self.worker_price_label.grid(column = 0, row = 0, sticky = "NSEW")

        purchase_worker = Button(self.worker_upgrade_popup, text = "Purchase", font = "arial 10 bold", command = lambda: self.purchase_worker()) #when clicked starts purchase_worker() method
        purchase_worker.grid(column = 0, row = 1, sticky = "NSEW")

    def purchase_worker(self):
        '''Method used to purchase worker'''

        if self.worker_cost > self.user_balance: #checks is user can purchase 
            self.worker_price_label.configure(text = "Insufficient Funds") #shows text if user cannot afford 
        else: #if user can afford
            self.worker_upgrade_popup.destroy() #closes popup
            self.count = self.user_balance-self.worker_cost #new balance
            self.user_sprinkles_amount.set(self.count) # displays new balance
            self.user_worker_amount += 1 #increase amount of workers user has
            self.worker() # starts worker() method

    def worker(self):
        '''Method used to generate passive income as a worker'''
        self.count += 1 #each worker increases balance by 1
        self.user_sprinkles_amount.set(self.count) #display increase
        self.working = self.root.after(1000,self.worker) # after 1000 milliseconds themethod will run itself again
    #-----------------------------------------------------------------------------------------------------------------------------
    
    def login(self):
        '''This method is used to check if the entered username and password are valid and then to load the users information in and start the game'''

        

        self.username = self.username_box.get()
        pass_to_check = self.password_box.get()

        if self.username in self.users and self.users[self.username]["password"] == pass_to_check: #checks if username exists and if password entered matches password stored

            #if passsword and username match then these variables are set to the values from the json file
            self.clickamount = self.users[self.username]["click_upgrade"] #sprinkles per click
            self.user_worker_amount = self.users[self.username]["worker_amount"] #amount of workers
            self.count = self.users[self.username]["user_sprinkles"] #users sprinkle balance
            self.user_sprinkles_amount.set(self.count) #sets the display of sprinkles on the game page

            for worker in range(self.user_worker_amount): 
                self.worker() #starts workers

            self.show_frame("gamepage") #shows game page since login was successful

        elif self.username == "" or pass_to_check == "":
            self.incorrect_label.configure(text = "Do not leave fields blank")


        else:
            self.incorrect_label.configure(text = "Incorrect username or password")#if password does not match or username is not valid then this text is shown to user
           
    def save(self):
        self.users[self.username]["click_upgrade"] =  self.clickamount #sprinkles per click
        self.users[self.username]["worker_amount"] =  self.user_worker_amount #amount of workers
        self.users[self.username]["user_sprinkles"] = self.count #users sprinkle balance

        with open("donut_clicker_users.json", "w") as file:
            json.dump(self.users, file, indent = 4) 

    def quit(self):
        ''' this method is used to save users information and exit to home page'''
        if self.user_worker_amount > 0:
            self.root.after_cancel(self.working) #stops workers 
        
        self.save()#save information
        self.show_frame("homepage") #shows home page

    def click(self):
            '''This method is used to increase the users sprinkles each time a button is clicked'''
            self.count += self.clickamount#increases count
            self.user_sprinkles_amount.set(self.count) #sets labels textvariable to new count

    def popup(self):
        '''Method that makes a popup for the upgrade store'''

        #window
        popup = Toplevel(self.root, bg = "lightpink", borderwidth = 2, relief = "solid")
        popup.overrideredirect(True)
        popup.title("Upgrade Store")
        popup.grid_columnconfigure(0, weight =1)
        popup.geometry("300x200+1100+350")


        #window design
        popup_label = Label(popup, text = "Upgrade Store", font = "arial 20 bold", bg = "lightpink")
        popup_label.grid(column = 0, row = 0, sticky = "NSEW")

        upgrade_button1 = Button(popup, text = "increase sprinkles earned per click", command = self.clickincrease_upgrade)
        upgrade_button1.grid(column = 0, row = 1, pady = 5)

        upgrade_button2 = Button(popup, text = "purchase workers", command = self.worker_upgrade)
        upgrade_button2.grid(column = 0, row = 2, pady = 5)

        close_button = Button(popup, text = "close", command = popup.destroy)
        close_button.grid(column = 0 , row = 3, pady = 20)
    
    def run(self):
        '''Method to run program'''
        self.show_frame("homepage")
        self.root.mainloop()

    def top_players(self):
        '''This method is used to sort ther top 5 players'''
        self.balances = [(user, data["user_sprinkles"]) for user, data in self.users.items()]
        self.balances.sort(key = lambda x : x[1], reverse = True)

        return self.balances[:5]

    def display_top_players(self):
        '''Method is used to disply the leaderboard'''
        
        #leaderboard 
        top_5 = self.top_players()
            

        #window
        popup = Toplevel(self.root, bg = "lightpink", borderwidth = 2, relief = "solid")
        popup.overrideredirect(True)
        popup.title("Upgrade Store")
        popup.grid_columnconfigure(0, weight =1)
        popup.geometry("300x200+1100+350")

        #window design

        banner = Label(popup, text = "Leaderboard", font = "arial 20 bold", bg = "lightpink")
        banner.grid(column = 0, row = 0, sticky = "NSEW")


        for i, (user, balance) in enumerate(top_5, start = 1):
            Label(popup, text = f"{i}. {user} - {balance}", bg = "lightpink").grid(column = 0 , row = i+1)

        close_button = Button(popup, text = "close", command = popup.destroy)
        close_button.grid(column = 0 , row = 7, pady = 20)



        top_5 = self.top_players()
   
    def new_user(self):
        self.username = self.new_username_box.get()
        password = self.new_password_box.get()
        if self.username in self.users:
            self.create_label.configure(text = "username already exists")

        elif self.username == "" or password == "":
            self.incorrect_label.configure(text = "Do not leave fields blank")

        else:
            self.users[self.username] = {
                "password": password,
                "click_upgrade": 1,
                "worker_amount": 0,
                "user_sprinkles": 0
            }
            with open("donut_clicker_users.json", "w") as file:
                json.dump(self.users, file, indent = 4) #saves information to json file

            self.clickamount = self.users[self.username]["click_upgrade"] #sprinkles per click
            self.user_worker_amount = self.users[self.username]["worker_amount"] #amount of workers
            self.count = self.users[self.username]["user_sprinkles"] #users sprinkle balance
            self.user_sprinkles_amount.set(self.count) #sets the display of sprinkles on the game page
    
            self.create_label.configure(text = "Account Created Succesfully!")
            self.show_frame("gamepage")





app = Game()
app.run()


    
    
