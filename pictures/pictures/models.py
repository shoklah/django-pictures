from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=130)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='img/')
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return u'{0}'.format(self.title)

class Picture(models.Model):
    title = models.CharField(max_length=130)
    image = models.ImageField(upload_to="img/")
    album_id = models.BigIntegerField(blank=True, default=0)
    user_id = models.CharField(max_length=255)