from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.decorators import login_required
from . forms import *

# Create your views here.
def home(request):
    trending = News.objects.filter(trending = 1)
    trend = Product.objects.filter(trending = 1)[:4]
    context = {'trending':trending,'trend':trend}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')

def leadership(request):
    leader = Stakeholder.objects.all()
    context = {'leader':leader}
    return render(request, 'leadership.html',context)

def mission(request):
    return render(request, 'mission.html')

def values(request):
    return render(request, 'values.html')

def services(request):
    comment = Comment.objects.all().order_by('-date')
    context = {'comment':comment}
    return render(request, 'services.html',context)

def news(request):
    news = News.objects.all().order_by('-date')
    
    context = {'news':news}
    return render(request, 'news.html',context)

@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        form = CommentForms(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author =  request.user
            instance.save()
            return redirect('home')
    else:       
        form = CommentForms()
    
    return render(request,'create.html',{'form':form})


# Back end 

def category(request):
    category = Category.objects.all()
    context={'category':category}
    return render(request, 'backend/category.html',context)

def categoryview(request,slug):
    if(Category.objects.filter(slug =slug)):
        products = Product.objects.filter(category__slug = slug)
        category= Category.objects.filter(slug=slug).first()
        context ={'products':products,'category':category}
        return render(request, 'backend/products.html',context)
    
    else:
        return redirect('category')
    
def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug = cate_slug)):
        if(Product.objects.filter(slug= prod_slug)):
            products = Product.objects.filter(slug= prod_slug).first()
            context ={'products':products}
        else:
            return redirect('category')
    else:
        return redirect('category')
    return render(request,'backend/view.html',context)