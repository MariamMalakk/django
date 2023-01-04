from django.db import models

# Create your models here.
class booklib(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"