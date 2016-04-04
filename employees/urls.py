from django.conf.urls import url
from .views import employees, employee, categories, top_level

urlpatterns = [
    url(r'^category/list/$', categories, name='categories'),
    url(r'^list/$', employees, name='employees'),
    url(r'^list/top/level/(?P<number>\d+)/$', top_level, name='top_level'),
    url(r'^(?P<pk>\d+)/$', employee, name='employee'),
]
