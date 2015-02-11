I = {'color': (0, 215, 255),
     'position': (((0, 2), (1, 2), (2, 2), (3, 2)),
                  ((2, 0), (2, 1), (2, 2), (2, 3)),
                  ((0, 1), (1, 1), (2, 1), (3, 1)),
                  ((1, 0), (1, 1), (1, 2), (1, 3)))}
J = (0, 0, 255)
L = (255, 183, 0)
O = (255, 255, 0)
S = (0, 255, 0)
T = (127, 0, 255)
Z = (255, 0, 0)


class Node(object):
    """
    A single square of the Tetris board.
    """

    def __init__(self, x, y):
        self.color = None
        self.x = x
        self.y = y


class Tableau(object):
    """
    Model of Tetris board
    """

    def __init__(self):
        self.model = [[Node(x, y) for x in xrange(10)] for y in xrange(22)]


class Tetromino(object):

    def __init__(self, kind, table):
        self.kind = kind
        self.table = table
        self.edge = len(table.model[0]) - 1
        self.x = len(table.model[0]) / 2 - 2
        self.y = len(table.model)
        self.rotation = 0

    def clockwise(self):
        self.rotation += 1

    def counterclockwise(self):
        self.rotation += -1

    def left(self, vel=1):
        edge = min((x[0] for x in I['position'][self.rotation]))
        self.x = self.x - vel if self.x - vel + edge >= 0 else 0 - edge

    def right(self, vel=1):
        self.x = self.x + vel if self.x + vel <= self.edge else self.edge


def run(display):
    pass