from django.db import models

# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    

class BookCount(models.Model): 
    liveCount = models.IntegerField()

    def __str__(self):
        return 'counter'
