# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Editor,Article,tags
from django.test import TestCase

class EditorTestClass(TestCase):


# Set up method
    def setUp(self):
        self.Mimy= Editor(first_name = 'Mimy', last_name ='Claire', email ='mimy@moringaschool.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Mimy,Editor))

# Create your tests here.
