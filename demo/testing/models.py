from django.db import models

# Create your models here.
class Test(models.Model):
    number_field = models.IntegerField(null=True)
    text_field = models.TextField(null=True)