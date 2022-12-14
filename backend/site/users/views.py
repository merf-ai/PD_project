from .models import User
from .extra_logic import *
from users.permissions import *
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.


class Register(APIView, EmailSenderMixin):
    '''Регистрация с использованием email'''
    template_mail = r'users/user_verification_message.html'
    subject_message = 'Подтверждение верификации'
    verified_url = r'users/reg/success'

    def post(self, request):
        '''Обработка формы регистрации'''
        group_name = request.data['groups']
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'data': request.data, 'errors': serializer.errors})
        else:
            serializer.save()
            us = User.objects.all().get(email=serializer.validated_data['email'])
            us.groups.add(Group.objects.get(name=group_name))
            super().send_mail_verify(request, us.email)
            return Response({'success_message': 'Вы успешно зарегистрировались, подтвердите почту!'})

    def get_extra_context_html_message(self, *args, **kwargs):
        return {'url_delete': super().prepare_url_verification( kwargs['request'], kwargs['user'], r'users/reg/user_delete')}



class VerifyEmail(APIView):
    '''Пользователю приходит письмо с ссылками, и этот класс для обработки ссылки на подтверждение почты'''
    def get(self, request, *args, **kwargs):
        user = user_urlsafe_decode(kwargs['uid'])
        if user is not None and default_token_generator.check_token(user, kwargs['token']):
            user.email_verified = True
            user.save()
            return Response({'message': f'Ваша почта подтверждена, {user.first_name}!'})
        return Response({'message': f'Ссылка недействительна!'})
        
    
class PasswordReset(APIView, EmailSenderMixin):
    '''Обработка сброса пароля'''
    template_mail = 'users\\password_reset_messege.html'
    subject_message = 'Сброс пароля'
    verified_url = r'users/password_reset/new_password'

    def post(self, request):
        try:
            user = User.objects.all().get(email=request.data['email'])   
            try:
                self.send_mail_verify(request, user.email)         
            except:
                return Response({'message': 'Письмо не было отправлено!'})        
        except:
            return Response({'message': 'Пользователь с таким email не найден!'})
        return Response({'message': 'Сообщение отправлено на почту!'})


class PasswordResetNewPassword(APIView):
    '''Для сброса пароля пользователю приходит письмо ссылкой на страницу с формой для изменения пароля, он переходит на неё и вид форму 
    для сброса пароля, данный класс сохраняет пользователя, если токен валиден, иначе нет'''
    def get(self, request, *args, **kwargs): 
        return Response()

    
    def post(self, request, *args, **kwargs):
        user = user_urlsafe_decode(kwargs['uid'])
        if user is not None and default_token_generator.check_token(user, kwargs['token']):
            user.password = make_password(request.data['password'])
            if user.email_verified is False:
                user.email_verified = True
                user.save()
                return Response({'message': 'Пароль успешно изменён! Ваша почта подтверждена!'})
            user.save()
        else:
            return Response({'message': 'Ссылка недействительна!'})
        return Response({'message': 'Пароль успешно изменён!'})


class UserMistakeRegistration(APIView):
    '''Если пользователь не регистрировался на сайте, ему необходимо перейти по второй ссылке в письме, этот класса 
    отвечает за обработку данной ссылки'''
    def get(self, request, *args, **kwargs): 
        user = user_urlsafe_decode(kwargs['uid'])
        if user is not None and default_token_generator.check_token(user, kwargs['token']):
            User.objects.filter(id=user.id).delete()
        return Response({'message': 'Спасибо за переход по ссылке, если хотите можете зарегистрироваться на нашем сайте!'})


class LoginView(CustomObtainAuthToken):
    '''Класс для входа'''
    pass


class Logout(APIView):
    "Уничтожает токен в бд"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.get(key=request.auth).delete()
        return Response({'message': 'Вы успешно вышли!'})


class TestView(APIView):
    "Вьюха для проверки входа"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEmailVerifedAndUserAuth]

    def post(self, request):
        #print(request.META['Created-By'])
        #ex = TokenAuthentication()
        #print(ex.authenticate(request))
        #print(user)
        #if request.user.is_authenticated:
        #return Response({'message': 'Это успех, братишка!'})
        return Response({'message': 'Вы зарегистрированы!'})
        

class UserProfile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEmailVerifedAndUserAuth]

    def get(self, request):
        user = request.user
        role = user.groups.all()[0]
        user_data = {
                        'first_name': user.first_name, 
                        'last_name': user.last_name, 
                        'role': str(role),
                        'middle_name': user.middle_name,
                        'email': user.email, 
                        'student_group': user.student_group
                    }
        return Response(user_data)


