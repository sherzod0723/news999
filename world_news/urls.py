from django.urls import path
from .views import *


urlpatterns = [
    path('', news_header, name="home_page_dirs"),
    path('about/', about, name="about_page_dirs"),
    path('/(?P<id>\d+)/$', news_header_detail, name="news_header_detail_page_dirs"),
    path('like/<int:item_id>/', like_item, name='like_item'),
]
