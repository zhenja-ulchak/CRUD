class User:
    def __init__(self, login, passw, todo_list):
        self.login = login
        self.passw = passw
        self.todo_list = todo_list

    def t_list(self):
        return self.todo_list
