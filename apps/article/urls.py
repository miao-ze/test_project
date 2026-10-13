from django.urls import path, include

from . import views
app_name = 'article'


urlpatterns = [
    path('articles/',views.article_list),
    path('articles/<int:year>/',views.year_archive),
    path('articles/<int:year>/<int:month>/',views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/',views.article_detail),

    path('articles/add_article/',views.add_article,name='add_article'),
]
