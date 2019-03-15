from math import sqrt, tan, pi, radians, log, sin, cos, fmod

from geographiclib.geodesic import Geodesic

from points import *


ELLIPSOIDS = {
    # model   major (km)   minor (km)     flattening
    'WGS-84': (6378.137, 6356.7523142, 1 / 298.257223563),
    'PZ-90.11': (6378.136, 6356.7513618, 1 / 298.257839303)
}
TEMP_ISA = 288.15
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
    polar = PolarPoint(azimuth=normalize_angle(result['azi1']),
                       distance=result['s12'])
    if subsequent:
        polar.set_azimuth(result['azi2'])
    return polar


def normalize_angle(angle):
    normalized = angle if angle == 0 else fmod(angle, 360)
    return (normalized + 360 if normalized < 0 else
            (normalized if normalized < 360 else normalized - 360))


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


def turn_angle(heading_start, heading_end):
    """Calculates value of angle between current and next.
    Positive value for RIGHT turn and negative for LEFT turn"""
    if heading_end - heading_start > 180.0:
        angle = heading_end - heading_start - 360.0
    elif heading_start - heading_end > 180.0:
        angle = heading_end - heading_start + 360.0
    else:
        angle = heading_end - heading_start
    return angle


def LTA(turn_radius, turn_angle):
    """Calculates linear turn anticipation"""
    return turn_radius * tan(radians(abs(turn_angle) / 2.0))


def temperature_correction(rwy_elevation, height, var=15.0):
    """Calculates temperature correction value"""
    delta_h = (-var/TEMP_GRADIENT) * log((1.0 + TEMP_GRADIENT * height * (TEMP_ISA + TEMP_GRADIENT * rwy_elevation)))
    return delta_h


def MSD(indicated_airspeed, altitude, heading_start, heading_end, bank=25.0, var=15.0, flyover=False):
    """Calculates minimum stabilizing distance for segment"""
    true_airspeed = TAS(indicated_airspeed, altitude, var)
    theta = abs(turn_angle(heading_start, heading_end))
    theta = 50.0 if theta < 50.0 else theta
    if flyover:
        a = 30.0
        c = 10.0
        r1 = turn_radius(true_airspeed, bank)
        r2 = turn_radius(true_airspeed, 15.0)
        L1 = r1 * sin(radians(theta))
        L2 = r1 * cos(radians(theta)) * tan(radians(a))
        L3 = r1 * (1 / sin(radians(a)) - 2.0 * cos(radians(theta)) / sin(radians(90.0 - a)))
        L4 = r2 * tan(radians(a / 2.0))
        L5 = c * true_airspeed / 3600.0
        return L1 + L2 + L3 + L4 + L5
    else:
        c = 5.0
        r = turn_radius(true_airspeed, bank)
        L1 = r * tan(radians(theta / 2.0))
        L2 = c * true_airspeed / 3600
        return L1 + L2


def TRD(procedure):
    """Calculates full procedure length considering turn anticipation"""
    trd = 0.0
    prev_turn_angle = 0.0
    for i in range(1, len(procedure)):
        if i < (len(procedure) - 1):
            geo_point1 = procedure[i - 1].ref_point()
            geo_point2 = procedure[i].ref_point()
            geo_point3 = procedure[i + 1].ref_point()
            segment1 = inverse(geo_point1.coordinates(), geo_point2.coordinates())
            distance = segment1.distance()
            heading1 = segment1.azimuth()
            segment2 = inverse(geo_point2.coordinates(), geo_point3.coordinates())
            heading2 = segment2.azimuth()
            next_turn_angle = abs(turn_angle(heading1, heading2))
            tas1 = TAS(procedure[i - 1].speed_limit(), procedure[i - 1].max_altitude())
            tas2 = TAS(procedure[i].speed_limit(), procedure[i].max_altitude())
            r1 = turn_radius(tas1)
            r2 = turn_radius(tas2)
            trd += (distance -
                    r1 * tan(radians(prev_turn_angle / 2)) -
                    r2 * tan(radians(next_turn_angle / 2)) +
                    (pi * r1 * prev_turn_angle) / 360 +
                    (pi * r2 * next_turn_angle) / 360
                    )
            prev_turn_angle = next_turn_angle
        else:
            geo_point1 = procedure[i - 1].ref_point()
            geo_point2 = procedure[i].ref_point()
            segment = inverse(geo_point1.coordinates(), geo_point2.coordinates())
            distance = segment.distance()
            next_turn_angle = 0.0
            tas1 = TAS(procedure[i - 1].speed_limit(), procedure[i - 1].max_altitude())
            tas2 = TAS(procedure[i].speed_limit(), procedure[i].max_altitude())
            r1 = turn_radius(tas1)
            r2 = turn_radius(tas2)
            trd += (distance -
                    r1 * tan(radians(prev_turn_angle / 2)) -
                    r2 * tan(radians(next_turn_angle / 2)) +
                    (pi * r1 * prev_turn_angle) / 360 +
                    (pi * r2 * next_turn_angle) / 360
                    )
    return trd
