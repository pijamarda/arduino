from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'api/^$', views.api_index, name='index'),
    url(r'api/add_temp_test/$', views.add_temp_test, name='add_temp_test'),

]