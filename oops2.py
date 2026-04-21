class Chatbook:
    def __init__(self):
        self.email=""
        self.password=""
        self.loggedin=False
        self.menu()
    
    def menu(self):
        user_input=input("""Welcome to chatbook how should i proceed?
                         1-Press 1 to sign up
                         2-Press 2 to sign in
                         3-Press 3 to write a post
                         4-Press 4 to message a friend
                         5-Press any other key to exit\t""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        email=input("Enter you mail : ")
        password=input("Enter your password : ")
        self.email=email
        self.password=password
        print("Print logged in successfully")
        self.menu()
    
    def signin(self):
        if self.email=="" and self.password=="":
            print("Signup first then sign in")
        else:
            user=input("Enter your mail here : ")
            pwd=input("Enter your pwd here : ")
            if self.email==user and self.password==pwd:
                self.loggedin=True
                print("Signed in success")
            else:
                print("Please enter correct credentials")
        print("\n")
        self.menu()
        


obj=Chatbook()