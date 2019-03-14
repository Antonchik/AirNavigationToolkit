from math import sqrt, tan, pi, radians

from geographiclib.geodesic import Geodesic

from points import GeoPoint, PolarPoint


ELLIPSOIDS = {
    # model   major (km)   minor (km)     flattening
    'WGS-84': (6378.137, 6356.7523142, 1 / 298.257223563),
    'PZ-90.11': (6378.136, 6356.7513618, 1 / 298.257839303)
}
TEMP_ISA = 288.0
TEMP_GRADIENT = 0.006496


def geodesic(datum):
    ellipsoid = ELLIPSOIDS[datum]
    geo_task = Geodesic(ellipsoid[0], ellipsoid[2])
    return geo_task


def direct(base: GeoPoint, polar: PolarPoint, datum='WGS-84'):
    """Resolves direct geodesic task using Karney's algorithm"""
    lat1 = base.latitude()
    lon1 = base.longitude()
    azimuth = polar.azimuth()
    distance = polar.distance()
    problem = geodesic(datum)
    result = problem.Direct(lat1, lon1, azimuth, distance)
    new_geo_point = GeoPoint(latitude=result['lat2'],
                             longitude=result['lon2'])
    return new_geo_point


def inverse(start: GeoPoint, end: GeoPoint, datum='WGS-84', subsequent=False):
    """Resolves inverse geodesic task using Karney's algorithm.
    If 'subsequent' is True it returns azimuth at the end point (i.e.
    considering meridians convergence)."""
    lat1 = start.latitude()
    lon1 = start.longitude()
    lat2 = end.latitude()
    lon2 = end.longitude()
    problem = geodesic(datum)
    result = problem.Inverse(lat1, lon1, lat2, lon2)
    polar = PolarPoint(azimuth=result['azi1'],
                       distance=result['s12'])
    if subsequent:
        polar.set_azimuth(result['azi2'])
    return polar


def TAS(IAS_kmh, altitude_meters, var=15.0):
    """Calculates true air speed for specific altitude"""
    ias = IAS_kmh
    tmp_decrease = TEMP_GRADIENT * altitude_meters
    return (ias * 171233 * pow((TEMP_ISA + var - tmp_decrease), 0.5) /
            pow((TEMP_ISA - tmp_decrease), 2.628))


def IAS(TAS_kmh, altitude_meters, var=15.0):
    """Calculates indicated air speed for specific altitude"""
    tas = TAS_kmh
    tmp_decrease = TEMP_GRADIENT * altitude_meters
    return (tas * pow((TEMP_ISA - tmp_decrease), 2.628) /
            (171233 * pow((TEMP_ISA + var - tmp_decrease), 0.5)))


def knots(airspeed_kmh):
    """Converts airspeed in kilometers per hour to knots"""
    return airspeed_kmh / 1.852


def kmh(airspeed_knots):
    """Converts airspeed in knots to kilometers per hour"""
    return airspeed_knots * 1.852


def feet_per_min(meters_per_sec):
    """Converts vertical speed in meters per second to feet per minute"""
    return meters_per_sec * 60.0 / 0.3048


def meters_per_sec(feet_per_min):
    """Converts vertical speed in feet per minute to meters per second"""
    return feet_per_min * 0.3048 / 60.0


def wind_icao(altitude_meters):
    """Calculates standard ICAO wind speed"""
    return 12.0 * altitude_meters * 0.001 + 87.0


def temperature_isa(altitude_meters, var=15.0):
    """Calculates temperature (for International Standard Atmosphere)
    at a specific altitude"""
    tmp_decrease = TEMP_GRADIENT * altitude_meters
    return TEMP_ISA + var - tmp_decrease


def mach(altitude_meters, indicated_airspeed=None, var=15.0):
    """Calculates sound speed in m/s or aircraft speed in a Mach number
    at a specific altitude"""
    sonic_speed = \
        20.046796 * sqrt(temperature_isa(altitude_meters, var))
    if not indicated_airspeed:
        return sonic_speed
    else:
        tas = TAS(indicated_airspeed, altitude_meters, var)
        return tas / (sonic_speed * 3.6)


def turn_rate(true_airspeed, bank=25.0):
    """Calculates rate of turn in degrees/sec"""
    return (6355.0 * tan(radians(bank))) / (pi * true_airspeed)


def turn_radius(true_airspeed, bank=25.0):
    """Calculates radius of turn at designated angle of bank in still air"""
    return true_airspeed / (20.0 * pi * turn_rate(true_airspeed, bank))


def turn_angle(angle_cur, angle_next):
    """Calculates value of angle between current and next"""
    if angle_next - angle_cur > 180.0:
        return angle_next - angle_cur - 360.0
    elif angle_cur - angle_next > 180.0:
        return angle_next - angle_cur + 360.0
    else:
        return angle_next - angle_cur


def LTA(turn_radius, turn_angle):
    return turn_radius * tan(radians(abs(turn_angle) / 2.0))


def MSD():
    pass


def TRD():
    pass
