from .models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from djsite.settings import EMAIL_HOST_USER
from django.forms.fields import CharField, EmailField
from django.utils.http import urlsafe_base64_decode
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import CustomTokenSerializer


class UserNotFoundException(Exception):
    '''Исключение, возникающее, когда пользователь не найден'''


class EmailSenderMixin:
    
    template_mail = None
    from_email = EMAIL_HOST_USER
    subject_message = None
    verified_url = ''

    
    def send_mail_verify(self, request, to_email: str) -> None:
        try:
            user = User.objects.all().get(email=to_email)
        except:
            raise UserNotFoundException
        url_verification = self.prepare_url_verification(request, user, self.verified_url)
        html_message = render_to_string(self.template_mail, {'url_verification': url_verification, 
                                                            **self.get_extra_context_html_message(request=request, user=user)})
        plain_message = strip_tags(html_message)
        send_mail(subject=self.subject_message, message=plain_message,
                recipient_list=[to_email], from_email=self.from_email, html_message=html_message)
        
        
    def prepare_url_verification(self, request, user: User, *args) -> str:
        domain = get_current_site(request).domain
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        pattern_name = '/'.join(args)
        return f'http://{domain}/{pattern_name}/{uid}/{token}'


    def get_extra_context_html_message(self, *args, **kwargs) -> dict:
        return {}
    
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomTokenSerializer


def user_urlsafe_decode(decode_data: str) -> None|User:
    try:
        user_pk = urlsafe_base64_decode(decode_data).decode()
        user = User.objects.all().get(pk=user_pk)
    except:
        user = None
    return user

