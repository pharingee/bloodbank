from django.db import models

from apps.users.models import Hospital


class Notification(models.Model):

    hospital = models.ForeignKey(Hospital, related_name='notifications')
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    text = models.TextField()


class Event(models.Model):

    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateField()
    is_visible = models.BooleanField(default=False)
