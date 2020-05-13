class Success(object):
    SUCCESS_RESPONSE = "Successful"
    SUCCESS = "Success"


class Error(object):
    ERROR_RESPONSE = "Error"
    SERVER_ERROR_5XX = "SERVER ERROR"
    EXCEPTION = "Some Unexpected Exception Occurred. Error is "

    LOCATION_NOT_EXIST = "No location exists for this time range and license."
    VEHICLE_NOT_EXIST = "No vehicle exists for this time range."
    LOCATION_FINDING_ERROR = "Error in finding the vehicle location."
    VEHICLE_FINDING_ERROR = "Error in finding the vehicle for this time range."

