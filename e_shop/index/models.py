from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=64)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)




class News(models.Model):
    news_name = models.CharField(max_length=256)
    news_zogolovok = models.TextField()
    news_osnovnoytext = models.TextField()
    news_photo = models.ImageField(upload_to='media')
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_name)


