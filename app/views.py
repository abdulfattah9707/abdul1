from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Abdul!")
def abdul(request):
    return HttpResponse("<h1><marquee>Hey abdul! what's ap?</h1>")
def fattah(request):
    return HttpResponse("<h1><marquee> Success is not built overnight, but rather through the small, consistent choices you make every single day. Every effort you put in—no matter how minor it seems right now—acts as a building block for your future. When you encounter setbacks, view them not as failures, but as valuable lessons that refine your approach and strengthen your resolve. Trust in your unique journey, stay focused on your goals, and remember that patience and persistence will eventually turn your hard work into meaningful achievements.<?h1>")