from django.conf.urls import url
from .views import comments

urlpatterns = [
    url(r'^(?P<employee_id>\d+)/category/(?P<category_id>\d+)/$', comments, name='comments'),
]