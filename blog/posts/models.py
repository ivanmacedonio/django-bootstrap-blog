import uuid
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=35, null=False, blank=False)
    subtitle = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200, null=False, blank=True)
    image = models.ImageField(null=True, blank=True, default="a.jpg")
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    

    def __str__(self):
        return self.title #para que sea legible en la bbdd 
    

