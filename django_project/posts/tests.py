from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTests(TestCase):
    @classmethod #converts a function to be a class method

    def setUpTestData(cls): #built in method to create test data
        cls.post = Post.objects.create(text = "this tests 1")
    #we only have one item stored as cls.post that can then be referred to in
    #any subsequent tests within the class as self.post.
    

    #only funtions taht starts with test will be run by django test
    def test_model_content(self):
        #content of the field post must match 
        self.assertEqual(self.post.text, "this tests 1")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        #testing the home url
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    
    def test_template_name_correct(self):
        #test for checking that the template used is the correct one
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    
    def test_template_content(self):
        #check that the homepage content shows whats in the test database 
        response = self.client.get(reverse("home"))
        self.assertContains(response, "this tests 1")
