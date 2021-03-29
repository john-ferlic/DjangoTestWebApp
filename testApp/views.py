from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .external_apis import alphavantage

# from external_apis.alphavantage import getStockOverviewData

# Create your views here.
def index(request):
        if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()    
        return render(request,'createpost.html')

def show_post(request):
    post_obj = Post.objects.all()

    context = {
        "daddy": post_obj
    }

    return render(request, 'show_post.html', context)

def header(request):
        return render(request, 'header.html')

def stockRec(request):
        return render(request, 'stockRecommendation.html')

def stockProcess(request):
        
        stock = request.POST.get('ticker')

        # Make api call to get information on stock
        stock_info = alphavantage.getStockOverviewData(stock)

        context = {
                "stock_info": stock_info
        }

        return render(request, 'stockRecommendation.html', context)