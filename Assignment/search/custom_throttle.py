from rest_framework.throttling import UserRateThrottle

class CustomThrottle(UserRateThrottle):
    scope = 'search'
    def allow_request(self, request, view):
        if request.method == 'GET':
            self.scope = 'get_scope'
            self.rate = '5/day'
            return True
        return super().allow_request(request, view)
