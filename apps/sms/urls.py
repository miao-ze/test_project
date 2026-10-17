from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
app_name = 'sms'

urlpatterns = [
    ## 用 csrf_exempt 包裹视图，仅给这个Webhook接口关闭CSRF防护
    path('sms/code/',csrf_exempt(views.SmsMobilePhone.as_view()),name='SmsMobilePhone')
]