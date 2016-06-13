from django.db import models


class Nation(models.Model):
    name = models.CharField(max_length=20)
    Capital = models.CharField(max_length=20)
    government = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    population = models.IntegerField()
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    location = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    hobbies = models.CharField(max_length=20)
    more_about_me = models.TextField()

    def __str__(self):
        return self.name