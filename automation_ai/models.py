from django.db import models
from django.utils.text import slugify

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    company = models.CharField(max_length=100)
    message = models.TextField()

    priority = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)
    next_action = models.TextField(blank=True)

    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = slugify(self.name.strip().lower())
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return  self.name

