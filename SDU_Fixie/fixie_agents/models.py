from django.db import models


class FixieAgent(models.Model):
    name = models.CharField(max_length=100)
    iframe_url = models.URLField()

    def __str__(self):
        return self.name
