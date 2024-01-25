from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name