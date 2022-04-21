from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView,DetailView
#from django.views import View
#from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    title = "RED-index"
    return render(request,'RED/index.html', {'title': title})

#@login_required
def red_home(request):
    title = "RED-home"
    return HttpResponse('RED/home.html', {'title': title})

def donate(request):
    title = "RED-donate"
    return HttpResponse('RED/donate.html', {'title': title})

def history(request):
    title = "RED-history"
    return render(request,'RED/history.html', {'title': title})
def haddits(request):
    title = "RED-haddits"
    return HttpResponse('RED/haddits.html', {'title': title})

def quran(request):
    title = "RED-quran"
    return render(request,'RED/quran.html', {'title': title})

def science(request):
    title = "RED-science"
    return HttpResponse('RED/science.html', {'title': title})

def local(request):
    title = "Local"
    return render(request, 'RED/local.html', {'title': title})

#@login_required
def about(request):
    title = "About"
    return render(request, 'RED/about.html', {'title': title})



# class product_list_view(ListView):
#     model = auctioned_product 
#     template_name = 'OMart/home.html'
#     context_object_name = 'products'
#     ordering=['-auction_end_dateTime']
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title']='Homepage'
#         title="index"
#         context['current_time'] = timezone.now()
#         return context


# def home(request):
#     title = "Omart-Homepage"
#     return HttpResponse('home.html', {'title': title})

# def home(request):
#     title = "Omart-Homepage"
#     return render(request,'home.html', {'title': title})


