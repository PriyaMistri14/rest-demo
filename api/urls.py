from django.urls import url, include
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'user',UserViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]
