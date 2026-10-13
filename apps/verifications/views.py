from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout

from .forms import LoginForm
from apps.article.models import User


class LoginFormView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html',{'form':LoginForm()})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('main:index')
            else:
                return HttpResponse('用户名和密码不匹配')
        else:
            return render(request,'login.html',{'form':LoginForm()})


class Register(View):
    def get(self,request):
        return render(request,'register.html',{'form':LoginForm()})

    def post(self,request):
        form = LoginForm(request.POST)  # 实例化表单对象
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # 这里要注意：你应该用 User.objects.create_user 来创建用户，这样密码会被加密哈希
            User.objects.create_user(username=username, password=password)

            # 注册成功后的跳转逻辑（比如跳转到登录页）
            return redirect('verifications:login')  # 请替换为你实际的登录路由名称

        return render(request, 'register.html', {'form': form})  # 如果表单校验失败，把带错误信息的form传回前


def logout(request):
    django_logout(request)
    return redirect('main:index')