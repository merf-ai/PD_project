class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        response = self.get_response(request)
        response['Created-By'] = "Chris"
        request.META['Created-By'] = "Chris"
        return response