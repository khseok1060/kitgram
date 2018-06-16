from django.conf.urls import url
from . import views

app_name = "users"
urlpatterns = [
  url(
    regex=r'^explore/$',
    view=views.ExploreUsers.as_view(),
    name='explore_users',
  ),
  url(
    regex=r'^(?P<user_id>[0-9]+)/follow/$',
    view=views.FollowUser.as_view(),
    name='follow_user',
  ),
  url(
    regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
    view=views.UnFollowUser.as_view(),
    name='unfollow_user',
  ),
  url(
    regex=r'^(?P<username>\w+)/followers/$',
    view=views.UserFollowers.as_view(),
    name='user_followers',
  ),
  url(
    regex=r'^(?P<username>\w+)/following/$',
    view=views.UserFollowing.as_view(),
    name='user_following',
  ),
  url(
    regex=r'^search/$',
    view=views.Search.as_view(),
    name='search', #url 순서변경을 통해 search부터 실행하도록 함. 아래 것이 위에 있으면 쿼리에 username으로 인식되어 userprofile을 찾는다
  ),
  url(
    regex=r'^(?P<username>\w+)/$',
    view=views.UserProfile.as_view(),
    name="user_profile"
  ),
]
