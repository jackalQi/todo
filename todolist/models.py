from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=20)
    create_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_date"]
