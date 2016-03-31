from django.conf.urls import url
from .views import employees, employee

urlpatterns = [
    url(r'^list/$', employees, name='employees'),
    url(r'^(?P<pk>\d+)/$', employee, name='employee'),
]