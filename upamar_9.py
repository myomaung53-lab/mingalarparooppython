class Teacher:
    school = "Mingalar"
    count = 0
    def __init__(self, name,):
        self.count_object()
        self.t_id = self.count
        self.name = name
        
    def get_info(self):
        print("Name -> ", self.name)
        print("Teacher Id -> ", self.t_id)
        print("School Name -> ", self.school)
    
    @classmethod
    def change_schoolName(cls, new_name):
        cls.school = new_name
    
    @classmethod
    def count_object(cls):
        cls.count += 1

t1 = Teacher("mgmg")
t2 = Teacher("mama")
t3 = Teacher("mg")
t4 = Teacher("ma")

# print(t2.t_id)
t2.get_info()
t1.get_info()

# print(t1.__dict__)
# t1.get_info()
# print()
# t2 = Teacher("mama", '77798')
# t2.school = "MMM Education"_
# print(t2.__dict__)
# t2.get_info()
# Teacher.change_schoolName("MMM Education")
# print("After : ")
# t1.get_info()
# print()
# t2.get_info()
# print(Teacher.count)

def is_balanced(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)  # Push to stack
        elif char == ')':
            if not stack:       # Stack အားနေရင် (တွဲစရာ အဖွင့်ကွင်းမရှိရင်)
                return "No"
            stack.pop()         # Stack ထဲက အဖွင့်ကွင်းကို ထုတ်လိုက်ခြင်း
            
    if not stack:               # အကုန်စစ်ပြီးလို့ Stack အားနေမှ Yes
        return "Yes"
    else:
        return "No"

# စမ်းသပ်ချက်များ
print(f"()       -> {is_balanced('()')}")       # Yes
print(f") (      -> {is_balanced(')(')}")       # No
print(f"()()()   -> {is_balanced('()()()')}")   # Yes
print(f"((()))   -> {is_balanced('((()))')}")   # Yes
print(f"(()      -> {is_balanced('(()')}")      # No