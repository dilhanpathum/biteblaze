from django.urls import path, include
from rest_framework import routers
from biteblaze import views
#api verstoning

router = routers.DefaultRouter()
router.register(r'biteblaze', views.TaskView, basename='biteblaze')

urlpatterns = [
    path("api/", include(router.urls))
]

