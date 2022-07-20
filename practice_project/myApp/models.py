from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name + " <-> " + self.dept
