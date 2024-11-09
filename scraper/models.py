from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=1000, null=True, blank = True)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    external_link = models.URLField()
    