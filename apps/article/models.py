from django.db import models

# Create your models here.


class User(models.Model):
    """
    User模型类
    """
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Article(models.Model):
    """
    Article模型类
    """
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish_data = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title