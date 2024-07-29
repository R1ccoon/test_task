from django.db import models


class Ads(models.Model):
    title = models.CharField(max_length=50)
    ad_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=20)
    views = models.IntegerField()
    pos = models.IntegerField()
