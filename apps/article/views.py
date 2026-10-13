from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Article,ArticleModelForm




def article_list(request):
    # 从新到旧（时间倒序，最新的在最上面）
    articles = Article.objects.all().order_by('-publish_data')
    return render(request,'article_list.html',{'articles':articles})


def year_archive(request,year):
    return HttpResponse(f"year_archive附路径1：接受参数:year:{year}")


def month_archive(request,year,month):
    return HttpResponse(f"month_archive附路径2：接受参数:year:{year},month:{month}")


def article_detail(request,year,month,slug):
    return HttpResponse(f'article_detail附路径3，接受参数：year:{year},month:{month},slug:{slug}')


@login_required
def add_article(request):
    if request.method == 'GET':
        form = ArticleModelForm()
    else:
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            # 核心修改：让表单生成模型实例，但先不保存到数据库 (commit=False)
            article = form.save(commit=False)

            # 将当前登录的用户赋值给文章实例的 user 字段
            # request.user 只有在使用了 @login_required 或已登录状态下才可用
            article.user = request.user

            # 此时所有必填字段都有了，再保存到数据库
            article.save()

            # 1. 添加成功提示信息
            messages.success(request, "评论上传成功！")

            # 2. 重定向到首页（请把 'index' 替换为你首页的真实 url name）
            return redirect('main:index')

            return HttpResponse(f'数据保存成功，验证成功')

    return render(request,'add_article.html',{'form':form})

