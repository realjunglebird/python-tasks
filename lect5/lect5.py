class Point:
    counter = 0

    def __init__(this, x, y):
        this.x = x
        this.y = y
        Point.counter += 1
    
    def test():
        print(Point.x)

#Point.test()

def cons(self, x, y):
    self.x = 1
    self.y = 2

# lambda args: expr
# def _(args):
#     return expr

P2d = type('Point2d', (object,),
           dict(__init__=lambda self, x, y: [
               setattr(self, 'x', x),
               setattr(self, 'y', y),
               None][-1]))