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
    path('token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('group/', views.GroupView.as_view(), name='group'),
    path('follow/', views.FollowView.as_view(), name='follow'),
    path('', include(router_v1.urls))
]
