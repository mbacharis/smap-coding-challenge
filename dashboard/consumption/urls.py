from django.conf.urls import url
from . import views
#url(r'^summary/$', views.summary), removed to simplify the url tree
#detail url modified to accept the dUser_key variable
urlpatterns = [
    url(r'^$', views.summary),
    url(r'^detail/(?P<dUser_key>[0-9]+)/$', views.detail),
]