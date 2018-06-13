from django.conf.urls import url
from . import views

app_name = "images" #django 2.0일 경우 사용
urlpatterns = [
  url(
    regex=r'^$',
    view=views.Feed.as_view(),
    name='feed',
  ),
]
