# practical work - 2 The Initializer
class Point:
    """Represents a point in two-dimensional geometric coordinates"""
    color = 'red'
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sayposition(self):
        print(f"({self.x}, {self.y})")
    
    def getposition(self):
        return self.x, self.y
    
    def move_left(self, dx):
        self.x = self.x - dx
    
    def move_right(self, dx):
        self.x += dx
    
    def move(self, xx, yy):
        self.x = xx
        self.y = yy
    
    def reset(self):
        self.move(0, 0)
    
    def calculate_distance(self, other_point):
        dist = ((other_point.x - self.x)**2 + (other_point.y - self.y)**2)**0.5
        return dist

if __name__ == "__main__":

    a = Point(0, 0)
    a.sayposition()
    b = Point(-4, 0)
    print(a.__doc__)
    dist_ab = a.calculate_distance(b)
    print("distance between a and b = ", dist_ab)


    # ax, ay = a.getposition()
    # print("ax = ", ax)
    # print("ay = ", ay)
    # a.move_left(2)
    # a.sayposition()
    # a.move_right(1)
    # a.sayposition()

    # b = Point(5, 3)
    # b.sayposition()
    # b.move(-2, 2)
    # b.sayposition()
    # b.reset()
    # print("-*-"* 10)
    # b.sayposition()




    


