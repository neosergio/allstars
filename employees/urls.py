from django.conf.urls import url
from .views import employees
from .views import employeeById

urlpatterns = [
	url(r'^list/$', employees, name='employees'),
	url(r'^getById/(?P<id>.+)$', employeeById, name='employeeById'),
]