from django.db import models


# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True, default="")
    owner = models.CharField(max_length=40, blank=True, null=True, default="")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.title
