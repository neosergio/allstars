from django.conf.urls import url
from .views import employees, employee, categories

urlpatterns = [
    url(r'^category/list/$', categories, name='categories'),
    url(r'^list/$', employees, name='employees'),
    url(r'^(?P<pk>\d+)/$', employee, name='employee'),
]
