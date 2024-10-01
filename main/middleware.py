import datetime

class LastLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Memproses request
        response = self.get_response(request)

        # Jika user terautentikasi, set cookie last_login
        if request.user.is_authenticated:
            last_login = request.user.last_login
            if last_login:
                response.set_cookie('last_login', last_login.strftime('%Y-%m-%d %H:%M:%S'))

        return response
