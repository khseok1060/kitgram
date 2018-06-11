from django.conf.urls import url
from . import views

app_name = "images" #django 2.0일 경우 사용
urlpatterns = [
  url(
    regex=r'^all/$',
    view=views.ListAllImages.as_view(),
    name='all_images',
  ),
]
