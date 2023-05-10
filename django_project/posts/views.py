from django.shortcuts import render

#use of generic views for listing things in our db
from django.views.generic import ListView

from .models import Post

# Create your views here.
class HomePageView(ListView):
    #to use list view we need to specify a model and a template
    model = Post
    template_name = "home.html"