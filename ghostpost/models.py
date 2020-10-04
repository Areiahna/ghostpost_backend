from django.db import models
from django.utils import timezone


class Post (models.Model):

    POST_CHOICES = (
        ("Roast", "Roast"),
        ("Boast", "Boast")
    )
    post = models.CharField(max_length=20, choices=POST_CHOICES)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    text = models.CharField(max_length=150)
    post_date = models.DateTimeField(
        default=timezone.now)

    def vote_score(self):
        return self.upvotes - self.downvotes

    def __str__(self):
        return f'{self.post} - {self.text}'
