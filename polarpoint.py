
class PolarPoint:
    """Class Polar Point.
    Stores azimuth (in radians) and distance (in meters)"""
    def __init__(self, azimuth=0.0, distance=0.0):
        self.__polar_point = {'azimuth': azimuth, 'distance': distance}

    def set_polar_coords(self, polar_coords_tuple):
        """Adds tuple(azimuth, distance) of polar coordinates to polar point"""
        azimuth = polar_coords_tuple[0]
        distance = polar_coords_tuple[1]
        if float(azimuth) and float(distance):
            self.__polar_point = {'azimuth': azimuth, 'distance': distance}

    def set_azimuth(self, azimuth):
        """Adds azimuth (in radians) to polar point"""
        if float(azimuth):
            self.__polar_point['azimuth'] = azimuth

    def set_distance(self, distance):
        """Adds distance (in meters) to polar point"""
        if float(distance):
            self.__polar_point['distance'] = distance

    def azimuth(self):
        """Returns azimuth (in radians) of the polar point"""
        return self.__polar_point['azimuth']

    def distance(self):
        """Returns distance (in meters) of the polar point"""
        return self.__polar_point['distance']

    def polar_coords(self):
        """Returns tuple(azimuth, distance) of polar coordinates of the polar point"""
        return self.__polar_point['azimuth'], self.__polar_point['distance']
