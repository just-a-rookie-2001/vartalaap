from django.db import models
from django.db.models.deletion import CASCADE
from user.models import User

# Create your models here.

class Groups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=100)
    group_desc = models.TextField()

class GroupMembers(models.Model):
    group_id = models.ForeignKey(Groups, on_delete=CASCADE)
    user_id = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        unique_together = (('group_id','user_id'))      #Since no composite key support by Django
