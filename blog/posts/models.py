from django.db import models


class Post(models.Model):

    text = models.TextField()
    title = models.CharField(max_length = 120, blank=True)

    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.TextField()
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text   



class PostComment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
