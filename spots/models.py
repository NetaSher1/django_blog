from django.db import models
from django.contrib.auth.models import User

class Levels(models.TextChoices):
    Beginner_Pro = 'BtP'
    Intermediate_Pro = 'ItP'
    Advanced_Pro = 'AtP'
    Pro = 'P'


class SurfSpots(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    thumb = models.ImageField(blank=True)
    level = models.CharField(default=None, max_length=100, choices=Levels.choices)
    best_tide = models.CharField(blank=True, max_length=100)
    sea_bed = models.CharField(blank=True, max_length=100)
    break_type = models.CharField(blank=True, max_length=100)
    youtube_id = models.CharField(default="j_U4niuqUhg", max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(SurfSpots, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post,self.name)





# class SurfSpots(models.Model):
#     title = models.CharField(max_length=100)
#     slug = models.SlugField()
#     body = models.TextField()
#     thumb = models.ImageField(blank=True)
#     level = models.CharField(blank=True, max_length=100)
#     best_tide = models.CharField(blank=True, max_length=100)
#     sea_bed = models.CharField(blank=True, max_length=100)
#     break_type = models.CharField(blank=True, max_length=100)
#     youtube_id = models.CharField(default="j_U4niuqUhg", max_length=100)
#     def __str__(self):
#         return self.title
