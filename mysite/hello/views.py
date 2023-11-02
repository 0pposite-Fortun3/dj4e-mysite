# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)
from django.http import HttpResponse
from django.views import View

def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    resp = HttpResponse(f'view count={num_visits} 742beee2')
    resp.set_cookie('dj4e_cookie', '742beee2', max_age=1000)
    resp.set_cookie('zap', 42)
    return resp