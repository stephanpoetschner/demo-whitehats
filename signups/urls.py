from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^success/$', views.success, name='success'),
]