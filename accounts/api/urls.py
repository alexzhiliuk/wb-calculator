from django.urls import path, include
from accounts.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]