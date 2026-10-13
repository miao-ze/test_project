from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm
from django import forms
from django.utils import timezone



# Create your models here.


class User(AbstractUser):
    """
    User模型类
    """
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Article(models.Model):
    """
    Article模型类
    """
    title = models.CharField(max_length=120,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    publish_data = models.DateField(auto_now_add=True, verbose_name="发布日期")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ArticleModelForm(ModelForm):
    content = forms.CharField(
        label='内容',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        min_length=10,
        error_messages={
            'required': '内容不能为空',
            'min_length': '长度不能少于10个字符',
        }
    )

    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_data': forms.DateInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'  # 只读，不可编辑
            }),
        }