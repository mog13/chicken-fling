class Position:
    def __init__(self,x = None,y=None):
        if x == None:
            x = 0
        if y == None:
            y = 0
        self.x = x;
        self.y = y;

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    __repr__ = __str__
