from django.test import TestCase
from .models import Article,Tags
import datetime as dt

# Create your tests here.

# Article class/model Tests
class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new tag and saving it
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post') 
        self.new_article.save()

        self.new_article.tags.add(self.new_tag) #add connects the many to many relationship between articles and tags

    def tearDown(self):
        Tags.objects.all().delete()
        Article.objects.all().delete()


# Get news today
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
#........
    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)