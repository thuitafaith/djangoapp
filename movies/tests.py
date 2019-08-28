# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Editor,Article,tags
import datetime as dt 


# Create your tests here.
class EditorTestClass(TestCase):
    # set up method
    def setUp(self):
        self.faith=Editor(first_name='faith',last_name='thuita',email='faith.thuita@moringaschool.com')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.faith,Editor))

    # testing save method
    def test_save_method(self):
        self.faith.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
    
class ArticleTestClass(TestCase):
    def setUp(self):
        # creating a new editor and saving it
        self.faith= Editor(first_name='faith',last_name='thuita',email='faith.thuita@moringaschool.com')
        self.faith.save_editor()

        # creating a new tag saving it
        self.new_tag = tags(name='testing')
        self.new_tag.save()
        
        self.new_article = Article(title='Test Article',post= 'this is a random test post',editor=self.faith)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)
    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)
    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
