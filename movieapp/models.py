from django.db import models

# Create your models here.
class cinema_table(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='pics')

