import logging

from datetime import datetime

from vehicle_system.models import GeoData
from vehicle_system.serializers import VehicleSerializer, GeoDataSerializer
from vehicle_system.response import SuccessResponse, ErrorResponse
from vehicle_system.constant import Success, Error
from shapely.geometry import Point, Polygon

logger = logging.getLogger(__name__)


def get_polygon_obj():
    # Create a Polygon
    coords = [(73.5598715332623, 18.7128121962049), (73.7795980957623, 18.858427375322),
              (74.0817221191998, 18.8298343351168), (74.1805990723248, 18.6633784989781),
              (74.2575033691998, 18.4420517762916), (74.2025717285748, 18.2569599275397),
              (74.0460165527935, 18.1030009147098), (73.743892529356, 18.0272764656119),
              (73.568111279356, 18.074281691122), (73.4774740723248, 18.2100037896017),
              (73.3538778809185, 18.4733152757346), (73.4088095215435, 18.6659806320587),
              (73.5598715332623, 18.7128121962049)]
    poly = Polygon(coords)
    return poly


def check_polygon(start_time, end_time):
    try:
        poly = get_polygon_obj()

        st = datetime.fromtimestamp(int(start_time)).strftime("%Y-%m-%d %I:%M:%S")
        et = datetime.fromtimestamp(int(end_time)).strftime("%Y-%m-%d %I:%M:%S")

        geo_objs = GeoData.objects.filter(time__gte=st, time__lte=et).select_related(
                    'vehicle_license').distinct('vehicle_license')
        if geo_objs:
            res = []
            for objs in geo_objs:
                lat = objs.latitude
                longt = objs.longitude
                if lat is not None and longt is not None:
                    p1 = Point(longt, lat)
                    if p1.within(poly):
                        serialized_obj = VehicleSerializer(objs.vehicle_license)
                        res.append(serialized_obj.data)

            return SuccessResponse(msg=Success.SUCCESS, results=res)
        else:
            return ErrorResponse(msg=Error.LOCATION_NOT_EXIST)

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        return None


def get_vehicle_location(start_time, end_time, license):
    try:
        st = datetime.fromtimestamp(int(start_time)).strftime("%Y-%m-%d %I:%M:%S")
        et = datetime.fromtimestamp(int(end_time)).strftime("%Y-%m-%d %I:%M:%S")

        geo_objs = GeoData.objects.filter(time__gte=st, time__lte=et, vehicle_license=license)
        if geo_objs:
            result =[]
            for objs in geo_objs:
                serialized_obj = GeoDataSerializer(objs)
                result.append(serialized_obj.data)

            return SuccessResponse(msg=Success.SUCCESS, results=result)
        else:
            return ErrorResponse(msg=Error.LOCATION_NOT_EXIST)

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        return None

