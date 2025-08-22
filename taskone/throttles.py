from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class StandardUserThrottle(UserRateThrottle):
    rate = '20/min'  # 10 requests per minute per user

class StandardAnonThrottle(AnonRateThrottle):
    rate = '15/min'   # 5 requests per minute for anonymous users

