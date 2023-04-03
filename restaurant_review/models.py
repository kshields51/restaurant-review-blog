from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=400)
    post_body = models.TextField()
    pub_date = models.DateTimeField('date published')
