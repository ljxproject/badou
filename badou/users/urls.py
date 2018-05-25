from django.conf.urls import url

from django.contrib.auth import views
from .views import register, person_center, login, hello

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^person/$', person_center, name='person'),
    url(r'^hello/(?P<pk>\d+)/$', hello, name='hello'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^$', login, name='login')
]
