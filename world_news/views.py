from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# def home(request):
#     return render(request, 'front/home.html')

def about(request):
    return render(request, 'front/about.html')

def news_header(request):
    header_post_objs = NewsTitle.objects.all()[:3]
    entertainment_post_objs = EntertainmentPost.objects.all()
    business_post_objs = BusinessPost.objects.all()
    travel_post_objs = TravelPost.objects.all()[:3]
    life_style_post_objs = LifeStylePost.objects.all()
    news_category = CategoryNewsTitle.objects.all()
    most_popular_post_objs = MostPopularPost.objects.all()
    featured_video_post_objs = FeaturedVideoPost.objects.all()
    tags_post_objs = TagsPost.objects.all()
    latest_articles_post_objs = LatestArticlesPost.objects.all()[:6]
    # category = header_post_objs.category.name
    # title = header_post_objs.title
    # photo = header_post_objs.photo
    # header_items = {
    #     "category": category,
    #     "title": title,
    #     "photo": photo,
    # }
    print(header_post_objs)
    return render(request, "front/home.html", context={'post_title': header_post_objs,
                                                       'entertainment': entertainment_post_objs,
                                                       'business': business_post_objs,
                                                       'travel': travel_post_objs,
                                                       'lifestyle': life_style_post_objs,
                                                       'title_category': news_category,
                                                       'most_popular': most_popular_post_objs,
                                                       'featured_video': featured_video_post_objs,
                                                       'tags_post': tags_post_objs,
                                                       'latest_articles': latest_articles_post_objs})

def news_header_detail(request, id):
    detail_post = NewsTitle.objects.get(id=id)
    detail_post.views_count += 1
    detail_post.save()
    comment_count = len(CommentNewsTitle.objects.filter(news_title=detail_post.id))
    return render(request, "front/blog-detail-02.html",
                  {"detail_view": detail_post,
                   "comment_count": comment_count})

def like_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.likes += 1
    item.save()
    return JsonResponse({'likes': item.likes})
