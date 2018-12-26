from django.db import models
from django.conf import settings
import requests


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    hits = models.PositiveIntegerField(default=0)
    search_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Search Titles"

    def __str__(self):
        return self.title

    # Get data with flicker api.
    def search_title_with_api(self):
        url = settings.FLICKER_API.format(
            api_key=settings.FLICKER_API_KEY,
            tag=self.title
        )
        r = requests.get(url).json()
        return r
