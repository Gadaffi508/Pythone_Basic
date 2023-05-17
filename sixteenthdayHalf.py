another_variable = 12

class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.user_name = user_name
        

user_1 = User("001","yusuf")

print(user_1.id + " "+ user_1.user_name)

user_2 = User("002","eda")

print(user_2.id + " "+ user_2.user_name)