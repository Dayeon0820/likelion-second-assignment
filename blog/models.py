from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content= models.TextField()
    writer= models.CharField(max_length=20)
    createAt =models.DateTimeField(auto_now_add=True)
    categories = models.CharField(max_length=50, default="default") #추가한것


    def __str__(self):
        return self.title
    

# Create your models here.
