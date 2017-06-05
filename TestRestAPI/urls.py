from django.conf.urls import url
from django.contrib import admin
from tests import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tests/$', views.TestsList.as_view()),
    url(r'^tests/(?P<pk>[0-9]+)/$', views.TestDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)