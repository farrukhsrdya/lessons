from django.db import models


# Create your models here.

class New(models.Model):
    New_name = models.CharField(max_length=64)
    added_date = models.DateTimeField(auto_now_add=True)



class News(models.Model):
    News_name = models.CharField(max_length=256)
    Zogolovok = models.TextField()
    osnovnoy_tekst = models.TextField()
    News_New = models.ForeignKey(New, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)





