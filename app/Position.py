class Position:

    x = 0
    y = 0

    def __init__(self, x = None, y=None):
        if x != None:
            self.x = x;
        if y != None:
            self.y = y;



    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    __repr__ = __str__

    def move_in_dir(self,direction,amount =None):
        if amount == None:
            amount = 1
        if direction == 0:
            self.y -= amount
        elif direction == 90:
            self.x += amount
        elif  direction == 180:
            self.y += amount
        else:
            self.x -= amount;
