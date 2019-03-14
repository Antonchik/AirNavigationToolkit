
class GeoPoint:
    """Class Geographic Point.
    Stores coords in degrees for a geographic point"""
    def __init__(self, latitude=0.0, longitude=0.0):
        self.__geo_point = {'latitude': latitude,
                            'longitude': longitude}

    def set_coordinates(self, *args):
        """Adds list[lat, lon] of coordinates (in degrees) to geographic point"""
        lat = args[0]
        lon = args[1]
        if float(lat) and float(lon):
            self.__geo_point = {'latitude': lat,
                                'longitude': lon}

    def set_latitude(self, latitude_deg):
        """Adds latitude (in degrees) to geographic point"""
        if float(latitude_deg):
            self.__geo_point['latitude'] = latitude_deg

    def set_longitude(self, longitude_deg):
        """Adds longitude (in degrees) to geographic point"""
        if float(longitude_deg):
            self.__geo_point['longitude'] = longitude_deg

    def latitude(self):
        """Returns latitude (in degrees) of the geographic point"""
        return self.__geo_point['latitude']

    def longitude(self):
        """Returns longitude (in degrees) of the geographic point"""
        return self.__geo_point['longitude']

    def coordinates(self):
        """Returns tuple(lat, lon) of coordinates (in degrees) of the geographic point"""
        return self.__geo_point['latitude'], self.__geo_point['longitude']


class PolarPoint:
    """Class Polar Point.
    Stores azimuth (in degrees) and distance (in km)"""
    def __init__(self, azimuth=0.0, distance=0.0):
        self.__polar_point = {'azimuth': azimuth,
                              'distance': distance}

    def set_polar(self, *args):
        """Adds tuple(azimuth, distance) of polar coordinates to polar point"""
        azimuth = args[0]
        distance = args[1]
        if float(azimuth) and float(distance):
            self.__polar_point = {'azimuth': azimuth,
                                  'distance': distance}

    def set_azimuth(self, azimuth):
        """Adds azimuth (in degrees) to polar point"""
        if float(azimuth):
            self.__polar_point['azimuth'] = azimuth

    def set_distance(self, distance):
        """Adds distance (in km) to polar point"""
        if float(distance):
            self.__polar_point['distance'] = distance

    def azimuth(self):
        """Returns azimuth (in degrees) of the polar point"""
        return self.__polar_point['azimuth']

    def distance(self):
        """Returns distance (in km) of the polar point"""
        return self.__polar_point['distance']

    def polar(self):
        """Returns tuple(azimuth, distance) of polar coordinates of the polar point"""
        return self.__polar_point['azimuth'], self.__polar_point['distance']


class CartesianPoint:
    """Class Cartesian Point.
    Stores x (in meters) and y (in meters)"""
    def __init__(self, x=0.0, y=0.0):
        self.__cartesian_point = {'x': x,
                                  'y': y}

    def set_cartesian(self, *args):
        """Adds tuple(x, y) of cartesian coordinates to cartesian point"""
        x = args[0]
        y = args[1]
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

    def cartesian(self):
        """Returns tuple(x, y) of cartesian coordinates from the cartesian point"""
        return self.__cartesian_point['x'], self.__cartesian_point['y']
