from django.conf.urls import url
from . import views

app_name = "notifications" #django 2.0일 경우 사용
urlpatterns = [
  url(
    regex=r'^$',
    view=views.Notifications.as_view(),
    name='notifications',
  ),
]
