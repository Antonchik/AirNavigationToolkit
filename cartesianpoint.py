
class CartesianPoint:
    """Class Cartesian Point.
    Stores x (in meters) and y (in meters)"""
    def __init__(self, x=0.0, y=0.0):
        self.__cartesian_point = {'x': x,
                                  'y': y}

    def set_cartesian_coords(self, xy_tuple):
        """Adds tuple(x, y) of cartesian coordinates to cartesian point"""
        x = xy_tuple[0]
        y = xy_tuple[1]
        if float(x) and float(y):
            self.__cartesian_point = {'x': x,
                                      'y': y}

    def set_x(self, x):
        """Adds x (in meters) of cartesian coordinates to cartesian point"""
        if float(x):
            self.__cartesian_point['x'] = x

    def set_y(self, y):
        """Adds y (in meters) of cartesian coordinates to cartesian point"""
        if float(y):
            self.__cartesian_point['y'] = y

    def x(self):
        """Returns x (in meters) of cartesian coordinates from the cartesian point"""
        return self.__cartesian_point['x']

    def y(self):
        """Returns y (in meters) of cartesian coordinates from the cartesian point"""
        return self.__cartesian_point['y']

    def cartesian_coords(self):
        """Returns tuple(x, y) of cartesian coordinates from the cartesian point"""
        return self.__cartesian_point['x'], self.__cartesian_point['y']
