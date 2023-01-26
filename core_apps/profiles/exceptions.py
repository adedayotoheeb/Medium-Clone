from rest_framework.exceptions import APIException


class NotYourProfile(APIException):
    status = 403
    default_detail = "You can't edit a post that doesnt blong to you!"


class CantFollowYourself(APIException):
    status_code=403
    default_detail= "You can't follow yourself."