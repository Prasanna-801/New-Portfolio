from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    github_link = models.URLField(max_length=200)
    live_demo = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
