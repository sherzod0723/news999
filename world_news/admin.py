from django.contrib import admin
from .models import *

admin.site.register([CategoryNewsTitle, NewsTitle,
                     EntertainmentPost, BusinessPost,
                     TravelPost, LifeStylePost,
                     CommentNewsTitle, Item,
                     MostPopularPost, FeaturedVideoPost,
                     TagsPost, LatestArticlesPost])
