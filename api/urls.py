from django.conf.urls import include, url
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register('output', views.ConsoleLogViewSet, base_name='output')

urlpatterns = [
    url(r'^', include(router.urls))
]
