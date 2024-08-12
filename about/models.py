from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    name = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    social_media = models.ManyToManyField(SocialMedia)

    def __str__(self):
        return self.social_media

class ContactUs(models.Model):
    fullname = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname
