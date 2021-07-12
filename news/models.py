from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# A model is basically a Python class that inherits from the modules.Model class

# Tag Model - This contains details about different Tags contained in an Article.
class Tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

# Article Model - This is the details concerning a news Article
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField() #Charfield to HTMLField because the tinymce editor saves the input as raw html to the database.
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True) #This will automatically save the exact time and date to the database as soon as we save that model.
    article_image = models.ImageField(upload_to = 'articles/',default= "default.jpeg")    
    
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term) #_icontains = This filter will check if any word in the titlefield of our articles matches the search_term.
        return news

# handling subscribers
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
# building restful apis
class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)