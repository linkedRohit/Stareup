from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
#from Stareup.WebApp import Item

def index(request):
  html = "<H1>Stareup.in</H1><HR>"
  return HttpResponse(html)
  
def item_list(request):
  html = "<H1>Item Lists</H1><HR>"
  return HttpResponse(html)