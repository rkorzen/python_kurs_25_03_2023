from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Article(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, related_name="articles")