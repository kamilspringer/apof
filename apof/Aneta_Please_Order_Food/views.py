from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ListOfRestaurants(TemplateView):
	template_name = 'listofrestaurantsview.html'