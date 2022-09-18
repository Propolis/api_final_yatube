from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


app_name = "api"

router_v1 = DefaultRouter()
router_v1.register("v1/follow", FollowViewSet, basename="follow")
router_v1.register("v1/groups", GroupViewSet)
router_v1.register("v1/posts", PostViewSet)
router_v1.register(
    r"v1/posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comment"
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
