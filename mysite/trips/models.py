from django.db import models

class Post(models.Model):
    user = models.TextField(blank=True, default='Anonymous')
    text = models.TextField(blank=True)
    uid = models.TextField(blank=True)

    def __str__(self):
        return self.user[:50]

class Visit(models.Model):
    passenger = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.passenger)
