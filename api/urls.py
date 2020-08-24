from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

router_v1 = DefaultRouter()
router_v1.register(r'posts', views.PostViewSet, basename='post')
router_v1.register(r'posts/(?P<id>\d+)/comments',
                   views.CommentViewSet,
                   basename='comment')

urlpatterns = [
    path('v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/group/', views.GroupView.as_view(), name='group'),
    path('v1/follow/', views.FollowView.as_view(), name='follow'),
    path('v1/', include(router_v1.urls))
]
