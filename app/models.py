from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Url = models.URLField()

    def __str__(self):
        return self.Name

class Accessrecord(models.Model):
    Name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Date = models.DateField()
    Author = models.CharField(max_length=199)
    Email = models.EmailField()

    def __str__(self):
        return self.Author