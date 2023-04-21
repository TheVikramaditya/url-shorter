from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

# Create your models here.

class Url(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.CharField(max_length=2000)
    uuid = models.CharField(max_length=1000)
    clickedAt = models.DateTimeField(auto_now_add=True)
    topSearched = models.IntegerField(default=0)

    def increase_topSearched(self,increment=1):
         Url.objects.filter(pk=self.pk).update(topSearched=F('topSearched') + increment)

    
    def __str__(self):
        return self.url

