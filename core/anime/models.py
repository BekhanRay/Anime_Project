from django.db import models
# from django.contrib.auth.models import User


class Anime(models.Model):
    anime_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    age_restrictions = models.IntegerField()
    subtitle = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='anime_covers/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.anime_id + '|' + self.title
        return self.title

    # @staticmethod
    # def get_name():
    #     return 'anime'


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Episode(models.Model):
    series = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=100)
    episode_number = models.PositiveIntegerField()
    release_date = models.DateField()
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.series


class Character(models.Model):
    # character_id = models.ForeignKey('Anime', default=1, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='characters')
    bio = models.TextField()
    image = models.ImageField(upload_to='character_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
