
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def my_print(self):
        print(f"({self.x}, {self.y})")

class SegmentLine:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
    
    def my_print(self):
        # print("start point ", self.start_point.x, self.start_point.y)
        # print("end point ", self.end_point.x, self.end_point.y)
        print("line point : ")
        self.start_point.my_print()
        self.end_point.my_print()
    
    def length(self):
        dx = self.end_point.x - self.start_point.x
        dy = self.end_point.y - self.start_point.y
        ans = (dx * dx + dy * dy) ** (1/2)
        return ans

p1 = Point(-2, 0)
p2 = Point(5, 0)
p1.my_print()
p2.my_print()

line_1 = SegmentLine(p1, p2)
line_1.my_print()

ans = line_1.length()
print("line 1 length = ", ans)
