from django.db import models

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return self.tittle

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    