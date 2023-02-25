from django.urls import path, include
from tariffs.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', api_views.CategoryViewset)
router.register(r'products', api_views.ProductViewset)


urlpatterns = [
    path('v1/', include(router.urls)),
]