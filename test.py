class Registration:
 
    
    def login(self):
        login_name = input("Please enter login: ")
        password = input("Please enter password: ")
        all_logs_user = str(dict( login=login_name, passw=hash(password)))

        with open("user.txt", "a") as my_file:
            return my_file.write(all_logs_user  + '\n')
      
    def read_user(self):
        login_in = input("Please enter login for Auterisation: ")
        password_in = input("Please enter password for Auterisation: ")
        all_logs_user = str(dict( login=login_in, passw=hash(password_in)))
        open_file = open("user.txt", "r")
        res = {}
        for i in open_file:
           res = i
       
        auth = eval(all_logs_user)
        result_text = eval(res)
        
        if result_text['login'] == auth["login"] or result_text['passw'] == auth["passw"]:
            print('good')
            
            name_file = result_text['login']
            
            if name_file:
                print("""
                    your choose :
                    write number:
                    1: Add text ( num " 1 ")
                    2: Update text ( num " 2 ")
                    3: Read text ( num " 3 ")

                    """)
                res = input(" your choose[ 1 or 2 or 3] :")

                if res == "1":
                    self.create_file_user(name_file)

                if res == "2":
                    self.update_user_text(name_file)

                if res == "3":
                    self.read_user_text(name_file)


    def create_file_user(self ,name_file):
        with open(f"{name_file}.txt", "a") as my_file:
            login_in = input("add tasck: ")
            return my_file.write(login_in  + '\n')
        
    def update_user_text(self, name_file):
        with open(f"{name_file}.txt", "w") as my_file:
            login_in = input("update first tasck: ")
            return my_file.write(login_in  + '\n')
        

    def read_user_text(self, name_file):
        with open(f"{name_file}.txt", "r") as my_file:
            return print(my_file.read())
       
 
       

        
w = Registration()



print(w.read_user())