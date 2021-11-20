from django.shortcuts import render
from django.http import HttpResponse

finches = []

# Create your views here.

def home(request):
  return HttpResponse("<h1>Hello!</h1>")

def about(request):
  return render(request, 'about.html')

class Finch:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })
