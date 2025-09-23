# class and method  and object 

class chatbook:
    
    __user_id = 1   # static variabe outside 
     
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id +=1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False 
        #self.menu()
    
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id( val):
        chatbook.__user_id = val
        
    def get_name(self):
        return self.__name
    
    def set_name( value):
        self.__name = value
        
    
    
    
    
    def menu(self): 
        user_input = input(
            """Welcome to chatbook !! How would you like to proceed?\n"
            "1.Press 1 to signup\n"
            "2.press 2 to signin\n"
            "3.press 3 to write a post\n"
            "4.press 4 to message a friend\n"
            "5-press any other key to exit
              ->  """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sending()
        else: 
            exit()
            

    
    def signup(self):
        email = input("enter your email here ->")
        pwd  = input("setup your password here->")
        self.username = email 
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

     
    def signin(self):
        if self.username =='' and self.password =='':
            print("please singnup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here ->")
            pwd =input("Enter your password 4here ->")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully !!")
                self.loggedin =True
            else:
                print("Please input correct credentials.. !!") 
        print("\n")
        self.menu()    
    def my_post(self):
        if self.loggedin==True:
           txt = input("Enter your message here ->")
           print(f"Following content has been posted -> {txt}") 
        else:
            print(f"you need to signin first to post something..")
            print("\n")
            self.menu()
            
    def sending(self):
      if self.loggedin==True:
            txt = input("Enter your message here ->")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
            
      else:
          print(f"your need to signin first to send message..")
      print("\n")
      self.menu()
       
#user1 = chatbook()   
 
