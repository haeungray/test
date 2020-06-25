class MyInt(type):
    def __call__(cls, *args, **kwds):
        return type.__call__(cls, *args, **kwds)

class int(metaclass = MyInt):
    def __init__(self, x,y):
        self.x = x
        self.y = y

