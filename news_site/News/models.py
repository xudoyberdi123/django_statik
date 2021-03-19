from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to="news_image", null=True)
    text = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Suggestion(models.Model):
    user_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
