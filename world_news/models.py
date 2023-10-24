from django.db import models
from django.contrib.auth.models import User


class CategoryNewsTitle(models.Model):
    name = models.CharField(max_length=255, verbose_name="Title in the category site")

    def __str__(self):
        return self.name


class NewsTitle(models.Model):
    category = models.ForeignKey(CategoryNewsTitle, on_delete=models.CASCADE, verbose_name="Yangilik turi")
    title = models.CharField(max_length=350, verbose_name="Sarlavha")
    powered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_category = models.CharField(max_length=255, verbose_name="Ichki kategoriya", default="Game")
    photo = models.ImageField(upload_to="title/images")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")
    views_count = models.IntegerField(default=0)
    inline_category = models.CharField(max_length=255, null=True, blank=True)
    social_facebook = models.CharField(max_length=255, null=True, blank=True)
    social_twitter = models.CharField(max_length=255, null=True, blank=True)
    social_google = models.CharField(max_length=255, null=True, blank=True)
    social_instagram = models.CharField(max_length=255, null=True, blank=True)


class CommentNewsTitle(models.Model):
    news_title = models.ForeignKey(NewsTitle, on_delete=models.CASCADE)
    comment = models.TextField()


class EntertainmentPost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Entertainment/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title


class BusinessPost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Business/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title


class TravelPost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Business/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title


class LifeStylePost(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="LifeStyle/images")
    inline_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(verbose_name="Yangilik matni")

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class MostPopularPost(models.Model):
    number = models.IntegerField(default=0)
    news_post = models.CharField(max_length=155, verbose_name="Yangi post")
    urls = models.CharField(max_length=375, verbose_name="Havola")

    def __str__(self):
        return self.news_post


class FeaturedVideoPost(models.Model):
    title = models.CharField(max_length=255, default="Clearing form video", serialize=1234)
    author = models.CharField(max_length=22, default="Shavkat Xusenaliyev")
    created_at = models.DateTimeField(auto_now_add=True)
    urls = models.CharField(max_length=255, auto_created="https://www.youtube.com/watch?v=ZCtmmjD0Avs")

    def __str__(self):
        return self.author


class TagsPost(models.Model):
    urls = models.CharField(max_length=375, auto_created=True, serialize=12)
    color = models.CharField(max_length=10, default="black", unique=True)
    background_color = models.CharField(max_length=20, auto_created="yellow", default="yellowgreen", unique=True)

    def __str__(self):
        return self.urls


class LatestArticlesPost(models.Model):
    photo = models.ImageField(upload_to="LatestArticles/images")
    title = models.CharField(max_length=255, default="Let me know if you have any further questions!", serialize=99)
    author = models.CharField(max_length=22, default="Shavkat Xusenaliyev")
    created_at = models.DateField(auto_now=FeaturedVideoPost, auto_created=True)

    def __str__(self):
        return self.author
