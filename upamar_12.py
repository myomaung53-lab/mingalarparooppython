
class Point:
    def __init__(self, x, y):
        # print("__init__ work")
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        # print("__getattribute__ work")
        if item == 'x':
            raise ValueError("access denied ... ")

        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        # print("__setattr__ work...")
        if key == 'z':
            raise ValueError("access denied .....")
        super().__setattr__(key, value)

    # def __getattr__(self, item):
    #     # print("__getattr__ work ")
    #     print(item + " don't have ")
    #     return False

    def __delattr__(self, item):
        print("__delattr__ work")


a = Point(5, 6)
print(a.zz)
print(a.__dict__)
del a.x

# print(a.z)
# a_y = a.y
# print("a y = ", a_y)
# print(a.__dict__)
# print(a.__dict__)
# a.y = 15
# print(a.__dict__)
# # print(a.y)
# a.z = 10
# print(a.__dict__)
print("end program...")