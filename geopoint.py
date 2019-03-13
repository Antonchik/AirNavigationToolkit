
class GeoPoint:
    """Class Geographic Point.
    Stores coords in degrees for a geographic point"""
    def __init__(self, latitude=0.0, longitude=0.0):
        self.__geo_point = {'latitude': latitude,
                            'longitude': longitude}

    def set_coordinates(self, coordinates_tuple):
        """Adds list[lat, lon] of coordinates (in degrees) to geographic point"""
        lat = coordinates_tuple[0]
        lon = coordinates_tuple[1]
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
