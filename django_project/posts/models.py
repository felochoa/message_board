from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField() #atribute text to store the posts as textfield type

    def __str__(self): 
        #will display the first 50 chars of the textfield
        return self.text[:50]