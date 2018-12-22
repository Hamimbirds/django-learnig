from django.db import models

# Create your models here.



class Post_vedio(models.Model):
    title = models.CharField("title",max_length=100)
    embed_code = models.TextField("embeded")
 
    def __str__(self):
        return self.title

 
    

 

 
     
