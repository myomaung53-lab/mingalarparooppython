
# practical work - class method
import random
class Fighter:
    def setup(self, name, health):
        self.name = name
        self.health = health
    
    def showinfo(self):
        print(f"{self.name} --> {self.health}")

    
    def kick(self, other):
        other.health = other.health - 20
        print(f"{self.name} kick {other.name}")
        print(f"{other.name} remain {other.health} health.....")
a = Fighter()
a.setup("mgmg", 100)
a.showinfo()

b = Fighter()
b.setup("koko", 100)
b.showinfo()
print("start battle.......")
while a.health >0 and b.health > 0:
    rn = random.randint(1,2)
    if rn == 1:
        b.kick(a)
    else:
        a.kick(b)

print()
if a.health > b.health:
    print(f"{a.name} is winner....")
else:
    print(f"{b.name} is winner...")


# print("-*-" * 10)
# a.kick(b)
# a.showinfo()
# b.showinfo()




