from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20)
    project_url = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=100, blank=True)
    image1 = models.CharField(max_length=100, blank=True)
    image2 = models.CharField(max_length=100, blank=True)
    image3 = models.CharField(max_length=100, blank=True)
    image4 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
