from django.db import models


# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class AdminUser(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Music(models.Model):
    title = models.CharField(max_length=70,
                             help_text="The title of the book.")
    artist = models.CharField(max_length=100)
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=50,
                            verbose_name="ISBN number of the book.")
    album = models.CharField(max_length=100)

    image = models.ImageField(null=True, blank=True)

    duration = models.CharField(max_length=100)
    audio_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title




