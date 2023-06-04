def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("simple middleware 1 before response")
        response = get_response(request)
        print("simple middleware 1 after response")

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


class SimpleMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("simple middleware 2 before response")
        response = self.get_response(request)
        print("simple middleware 2 after response")
        # Code to be executed for each request/response after
        # the view is called.

        return response