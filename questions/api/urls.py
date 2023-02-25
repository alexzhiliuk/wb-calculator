from django.urls import path, include
from questions.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', api_views.QuestionViewset)


urlpatterns = [
    path('v1/', include(router.urls)),
]