from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('posts', views.ImagePostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('upload/', views.image_upload_view),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("followToggle/<str:author>/", views.follow_toggle, name="followToggle")
]
