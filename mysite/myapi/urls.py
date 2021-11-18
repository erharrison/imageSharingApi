from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *


router = routers.DefaultRouter()
router.register('posts', views.ImagePostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('upload/', image_upload_view),
    path("profile/<str:username>/", profile, name="profile"),
    path('', PhotoListView.as_view(), name='list'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
]
