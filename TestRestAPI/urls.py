from django.conf.urls import url
from django.contrib import admin
from tests import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tests/$', views.tests_list),
    url(r'^tests/(?P<pk>[0-9]+)/$', views.test_detail),

]
