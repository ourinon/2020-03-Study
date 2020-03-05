from django.http import JsonResponse # Json 형식일때 result를 딕셔너리(키 밸류)로 가져온다.
from django.views import View


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
    @method-decorator(csrf_exempt)#보통 post할때 문제가생김.
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreatView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')

        user = User.objects.create_user(username, email, password)

        return self.response({'user.id':user.id})