
class GeoPoint:
    """Class Geographic Point.
    Stores name, coordinates in radians and datum information for a geographic point"""
    def __init__(self, name='g.p.', latitude=0.0, longitude=0.0, datum='WGS-84'):
        self.__geo_point = {'name': name,
                            'latitude': latitude,
                            'longitude': longitude,
                            'datum': datum}

    def set_name(self, name):
        """Adds name(code) to geographic point"""
        self.__geo_point['name'] = name

    def set_coordinates(self, coordinates_tuple):
        """Adds list[lat, lon] of coordinates (in radians) to geographic point"""
        lat = coordinates_tuple[0]
        lon = coordinates_tuple[1]
        if float(lat) and float(lon):
            self.__geo_point = {'latitude': lat,
                                'longitude': lon}

    def set_latitude(self, latitude_rad):
        """Adds latitude (in radians) to geographic point"""
        if float(latitude_rad):
            self.__geo_point['latitude'] = latitude_rad

    def set_longitude(self, longitude_rad):
        """Adds longitude (in radians) to geographic point"""
        if float(longitude_rad):
            self.__geo_point['longitude'] = longitude_rad

    def set_datum(self, datum):
        """Adds datum info (WGS-84 by default)"""
        self.__geo_point['datum'] = datum

    def name(self):
        """Returns the name of the geographic point"""
        return self.__geo_point['name']

    def latitude(self):
        """Returns latitude (in radians) of the geographic point"""
        return self.__geo_point['latitude']

    def longitude(self):
        """Returns longitude (in radians) of the geographic point"""
        return self.__geo_point['longitude']

    def datum(self):
        """Returns datum info"""
        return self.__geo_point['datum']

    def coordinates(self):
        """Returns tuple(lat, lon) of coordinates (in radians) of the geographic point"""
        return self.__geo_point['latitude'], self.__geo_point['longitude']
