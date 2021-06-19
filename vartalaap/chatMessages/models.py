from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from user.models import User
from groups.models import Groups
from django.utils import timezone

# Create your models here.

class Messages(models.Model):
    sender_id = models.ForeignKey(User, on_delete=CASCADE, related_name = 'sender_id')
    rx_id = models.ForeignKey(User, on_delete=CASCADE, related_name = 'rx_id')
    group_id = models.ForeignKey(Groups, on_delete=CASCADE)
    msg_id = models.IntegerField(primary_key=True)
    content = models.TextField()
    content_type = models.CharField(max_length=10)
    timestamp = models.DateTimeField(default=timezone.now)
    msg_status = models.TextField()
