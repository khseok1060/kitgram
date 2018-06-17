from django.conf.urls import url
from . import views

app_name = "images" #django 2.0일 경우 사용
urlpatterns = [
  url(
    regex=r'^$',
    view=views.Feed.as_view(),
    name='feed',
  ),
  url(
    regex=r'^(?P<image_id>[0-9]+)]/$',
    view=views.ImageDetail.as_view(),
    name='image_detail'
  ),
  url(
    regex=r'^(?P<image_id>[0-9]+)/likes/$',
    view=views.LikeImage.as_view(),
    name='like_image'
  ),
  url(
    regex=r'^(?P<image_id>[0-9]+)/unlikes/$',
    view=views.UnLikeImage.as_view(),
    name='unlike_image'
  ),
  url(
    regex=r'^(?P<image_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$',
    view=views.ModerateComments.as_view(),
    name='comment_image'
  ),
  url(
    regex=r'comments/(?P<comment_id>[0-9]+)/$',
    view=views.Comment.as_view(),
    name='comment'
  ),
  url(
    regex=r'^search/$',
    view=views.Search.as_view(),
    name='search'
  ),
]
