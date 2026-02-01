# practical work - 3 The Initializer

class Time:
    def __init__(self, hh, mm):
        self.hours = hh
        self.minutes = mm
    
    def my_print(self):
        print(f"{self.hours:02}:{self.minutes:02}")
    
    def sethours(self, hh):
        self.hours = hh
    
    def setminutes(self, mm):
        self.minutes = mm
    
    def addminutes(self, mm):
        t_m = self.minutes + mm + self.hours * 60

        new_h = t_m // 60
        new_m = t_m % 60

        self.sethours(new_h)
        self.setminutes(new_m)
    
    def addtime(self, other_time):
        total_min_1 = self.minutes + self.hours * 60
        total_min_2 = other_time.minutes + other_time.hours * 60

        t_m = total_min_1 + total_min_2

        new_h = t_m // 60
        new_m = t_m % 60

        ans = Time(new_h, new_m)
        return ans

    def compare(self, other_time):
        ...
        

if __name__ == "__main__":
    a = Time(12, 25)
    a.my_print()

    b = Time(1, 50)
    b.my_print()

    new_time = a.addtime(b)
    new_time.my_print()


    # a.addminutes(10)
    # a.my_print()
    # a.sethours(10)
    # a.setminutes(50)
    # a.my_print()


