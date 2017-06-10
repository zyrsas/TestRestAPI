from django.conf.urls import url
from django.contrib import admin
from tests import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_framework_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tests/$', views.TestsList.as_view()),
    url(r'^tests/(?P<pk>[0-9]+)/$', views.TestDetail.as_view()),
    #url(r'^auth/$', local_views.login_form, name='login_form'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]


urlpatterns = format_suffix_patterns(urlpatterns)