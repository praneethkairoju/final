from django.shortcuts import render
from .models import service, client, gallery,blog


# Create your views here.

files1 = service.objects.all()
files2 = client.objects.all()
files3 = blog.objects.all().order_by('-date')


def index(request):    
       
    
    data={
        "serv":files1,
        "clin":files2,
        "blog":files3,
    }
    

    return render(request,'index.html', data)
    



def about(request):

    data ={
        "clin" :files2
    }
    return render(request,'about.html', data)


def gallery(request):
    return render(request,'gallery.html')



def blog(request):
    return render(request,'blog.html')


def service(request):
    return render(request,'services.html')


def contact(request):
    return render(request,'contact.html')


def blogsingle(request):
    return render(request, 'blog-single.html')


def footer(request):
    return render(request, 'footer.html')