from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title