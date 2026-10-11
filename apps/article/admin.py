from django.contrib import admin
from apps.article.models import Article,User
# Register your models here.


class UserAdmin(admin.ModelAdmin):

    list_display = ('username','email')
    list_filter = ('username','email')
    search_fields = (['username','email'])


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','publish_data')
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(User,UserAdmin)
admin.site.register(Article,ArticleAdmin)