
class User:
    def __init__(self, name, age):
        if not User.check_age(age):
            raise ValueError("Invalid data : age ....")
        if not self.check_english_name(name):
            raise ValueError("Invalid data : name ....")
        self.name = name
        self.age = age
    
    def say_info(self):
        print(self.name, self.age)
    
    @staticmethod
    def check_age(age):
        if 0 < age < 120:
            return True
        else:
            return False
        
    @staticmethod
    def check_english_name(name):
        for ch in name:
            if not(('A' <= ch <= 'Z') or ('a' <= ch <='z') or ch == ' '):
                return False
            else:
                return True

# a = User('မောင်မောင်', 12) # error
# a = User("mgmg", -12) # error
a = User("mgmg", 20)
a.say_info()
# ans = User.check_age(10)
# ans = a.check_age(-12) # False
# print(ans)  