from django.http import JsonResponse # Json 형식일때 result를 딕셔너리(키 밸류)로 가져온다.
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError


class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data':data,
            'message':message, 
        }
        return JsonResponse(result, status)
#class간의 간격은 두줄, class안의 def들의 간격은 한줄

class UserCreateView(BaseView):
    @method_decorator(csrf_exempt)#보통 post할때 문제가생김.
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get('username','')
        if not username:
            return self.response(message='아이디를 입력해주세요.', status=400)
        password = request.POST.get('password', '')
            return self.response(message='패스워드를 입력해주세요.', status=400)
        email = request.POST.get('email', '')
            return self.response(message='올바른 이메일을 입력해주세요.', status=400)

        user = User.objects.create_user(username, email, password)

        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디야.', status=400)

        return self.response({'user.id':user.id})