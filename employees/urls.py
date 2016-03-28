from django.conf.urls import url
from .views import employees

urlpatterns = [
	url(r'^list/$', employees, name='employees'),
]