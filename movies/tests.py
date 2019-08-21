# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Editor,Article,tags

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