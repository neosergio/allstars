from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    from_user = models.ForeignKey('employees.Employee',
                                       related_name='%(class)s_from')
    to_user = models.ForeignKey('employees.Employee',
                                     related_name='%(class)s_to')
    category = models.ForeignKey('employees.Category')
