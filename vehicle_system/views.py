import logging

from vehicle_system.constant import Error
from vehicle_system.response import ServerErrorResponse, ErrorResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from vehicle_system.utils import check_polygon, get_vehicle_location

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_vehicle_list(request):
    try:
        start_time = request.query_params.get('start_tis', None)
        end_time = request.query_params.get('end_tis', None)

        response = check_polygon(start_time, end_time)

        if not response:
            response = ErrorResponse(msg=Error.VEHICLE_FINDING_ERROR)
            return Response(response.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if response and response.success is False:
            return Response(response.__dict__, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.__dict__, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        response = ServerErrorResponse()
        return Response(response.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_vehicle_activity(request):
    try:
        start_time = request.query_params.get('start_tis', None)
        end_time = request.query_params.get('end_tis', None)
        license = request.query_params.get('license', None)

        response = get_vehicle_location(start_time, end_time, license)

        if not response:
            response = ErrorResponse(msg=Error.LOCATION_FINDING_ERROR)
            return Response(response.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if response and response.success is False:
            return Response(response.__dict__, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.__dict__, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(Error.EXCEPTION + str(e))
        response = ServerErrorResponse()
        return Response(response.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)