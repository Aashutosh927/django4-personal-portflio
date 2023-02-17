from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=280, blank=True, null=True)
    description = models.TextField(max_length=580, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title