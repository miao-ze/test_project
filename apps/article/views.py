from django.shortcuts import render
from django.http import HttpResponse

from .models import Article




def article_list(request):
    articles = Article.objects.all()
    return render(request,'article_list.html',{'articles':articles})


def year_archive(request,year):
    return HttpResponse(f"year_archive附路径1：接受参数:year:{year}")


def month_archive(request,year,month):
    return HttpResponse(f"month_archive附路径2：接受参数:year:{year},month:{month}")


def article_detail(request,year,month,slug):
    return HttpResponse(f'article_detail附路径3，接受参数：year:{year},month:{month},slug:{slug}')
