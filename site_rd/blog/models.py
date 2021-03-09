from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    is_published = models.BooleanField(default = False)

    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()

    def __str__(self):
        return self.title


