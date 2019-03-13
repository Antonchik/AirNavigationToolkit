from math import sqrt, tan, pi, radians
from geographiclib.geomath import Math as gm
from geographiclib.geodesic import Geodesic
from geopoint import GeoPoint
from polarpoint import PolarPoint

ELLIPSOIDS = {
    # model           major (km)   minor (km)     flattening
    'WGS-84':        (6378.137, 6356.7523142, 1 / 298.257223563),
    'PZ-90.11':      (6378.136, 6356.7513618, 1 / 298.257839303)
}


class NavCalc(object):
    """
    Provides navigation routines.

    """
    ellipsoid_key = 'WGS-84'
    ellipsoid = ELLIPSOIDS[ellipsoid_key]
    geo_task = Geodesic(ellipsoid[0], ellipsoid[2])
    temp_isa = 288.0
    temp_gradient = 0.006496

    def set_ellipsoid(self, ellipsoid_key):
        if ellipsoid_key in ELLIPSOIDS:
            self.ellipsoid = ELLIPSOIDS[ellipsoid_key]
            self.ellipsoid_key = ellipsoid_key

    def direct(start_point: GeoPoint, polar: PolarPoint):
        """Resolves direct geodesic task using Karney's algorithm"""
        lat1 = start_point.latitude()
        lon1 = start_point.longitude()
        azimuth = polar.azimuth()
        distance = polar.distance()
        result = NavCalc.geo_task.Direct(lat1, lon1, azimuth, distance)
        new_geo_point = GeoPoint(latitude=result['lat2'],
                                 longitude=result['lon2'],
                                 datum=NavCalc.ellipsoid_key)
        return new_geo_point
    direct = staticmethod(direct)

    def inverse(start_point: GeoPoint, end_point: GeoPoint, subsequent=False):
        """Resolves inverse geodesic task using Karney's algorithm.
        If 'subsequent' is True it returns azimuth at the end point (i.e.
        considering meridians convergence"""
        lat1 = start_point.latitude()
        lon1 = start_point.longitude()
        lat2 = end_point.latitude()
        lon2 = end_point.longitude()
        result = NavCalc.geo_task.Inverse(lat1, lon1, lat2, lon2)
        new_polar_point = PolarPoint(azimuth=result['azi1'],
                                     distance=result['s12'])
        if subsequent:
            new_polar_point.set_azimuth(result['azi2'])
        return new_polar_point
    inverse = staticmethod(inverse)

    def ias2tas(indicated_airspeed_kmh, altitude_meters, var=15.0):
        """Calculates true air speed for specific altitude"""
        ias = indicated_airspeed_kmh
        tmp_decr = NavCalc.temp_gradient * altitude_meters
        return ias * 171233 * pow((NavCalc.temp_isa + var - tmp_decr), 0.5) / pow((NavCalc.temp_isa - tmp_decr), 2.628)
    ias2tas = staticmethod(ias2tas)

    def knots(airspeed_kmh):
        """Converts airspeed in kilometers per hour to knots"""
        return airspeed_kmh / 1.852
    knots = staticmethod(knots)

    def kmh(airspeed_knots):
        """Converts airspeed in knots to kilometers per hour"""
        return airspeed_knots * 1.852
    kmh = staticmethod(kmh)

    def feet_per_min(meters_per_sec):
        """Converts vertical speed in meters per second to feet per minute"""
        return meters_per_sec * 60.0 / 0.3048
    feet_per_min = staticmethod(feet_per_min)

    def meters_per_sec(feet_per_min):
        """Converts vertical speed in feet per minute to meters per second"""
        return feet_per_min * 0.3048 / 60.0
    meters_per_sec = staticmethod(meters_per_sec)

    def wind_icao(altitude_meters):
        """Calculates standard ICAO wind speed"""
        return 12.0 * altitude_meters * 0.001 + 87.0
    wind_icao = staticmethod(wind_icao)

    def temperature_isa(altitude_meters, var=15.0):
        """Calculates temperature (for International Standard Atmosphere) at specific altitude"""
        tmp_decrease = NavCalc.temp_gradient * altitude_meters
        return NavCalc.temp_isa + var - tmp_decrease
    temperature_isa = staticmethod(temperature_isa)

    def mach(altitude_meters, indicated_airspeed=None, var=15.0):
        """Calculates sound speed in m/s or aircraft speed in a Mach number at specific altitude"""
        sonic_speed = 20.046796 * sqrt(NavCalc.temperature_isa(altitude_meters, var))
        if not indicated_airspeed:
            return sonic_speed
        else:
            tas = NavCalc.ias2tas(indicated_airspeed, altitude_meters, var)
            return tas / (sonic_speed * 3.6)
    mach = staticmethod(mach)

    def turn_rate(true_airspeed, bank=25.0):
        """Calculates rate of turn in degrees/sec"""
        return (6355.0 * tan(radians(bank))) / (pi * true_airspeed)
    turn_rate = staticmethod(turn_rate)

    def turn_radius(true_airspeed, bank=25.0):
        """Calculates radius of turn at designated angle of bank in still air, in km"""
        return true_airspeed / (20.0 * pi * NavCalc.turn_rate(true_airspeed, bank))
    turn_radius = staticmethod(turn_radius)

    def turn_angle(angle_cur, angle_next):
        """Calculates value of angle between current and next """
        if angle_next - angle_cur > 180.0:
            return angle_next - angle_cur - 360.0
        elif angle_cur - angle_next > 180.0:
            return angle_next - angle_cur + 360.0
        else:
            return angle_next - angle_cur
    turn_angle = staticmethod(turn_angle)

    def lta(turn_radius, turn_angle):
        return turn_radius * tan(radians(abs(turn_angle) / 2.0))
    lta = staticmethod(lta)

# print(NavCalc.direct({'latitude': 50.0, 'longitude': 60.0}, {'azimuth': 45.0, 'distance': 65.0}))
# print(NavCalc.geo_task.Direct(50, 60, 45, 50))
# print(NavCalc.geo_task.Inverse(50, 60, 60, 70))